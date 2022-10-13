import os

import requests

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

from datetime import datetime

BASE_DIR = "path/to/my/dir"
JOB1_PORT = 8001
JOB2_PORT = 8002


def run_data_saver(report_date):
    """job 1"""

    params = {
        "date": report_date,
        "raw_dir": f"{BASE_DIR}/raw/sales/{report_date}"
    }

    res = requests.post(f"http://localhost:{JOB1_PORT}/", json=params)
    print(res.text)


def run_data_transformer(report_date):
    """job 2"""

    params = {
        "raw_dir": os.path.join(BASE_DIR, "raw", "sales", report_date),
        "stg_dir": os.path.join(BASE_DIR, "stg", "sales", report_date)
    }

    res = requests.post(f"http://localhost:{JOB2_PORT}/", json=params)
    print(res.text)


dag = DAG(
    dag_id="process_sales",
    start_date=datetime(2022, 8, 8),
    end_date=datetime(2022, 8, 11),

    schedule="0 1 * * *",
    catchup=True,
)

start = EmptyOperator(
    task_id="start_task",
    dag=dag,
)

task1 = PythonOperator(
    task_id="extract_data_from_api",
    dag=dag,
    python_callable=run_data_saver,
    op_kwargs={
        'report_date': "{{ execution_date.strftime('%Y-%m-%d') }}"
    },
)

task2 = PythonOperator(
    task_id="convert_to_avro",
    dag=dag,
    python_callable=run_data_transformer,
    op_kwargs={
        'report_date': "{{ execution_date.strftime('%Y-%m-%d') }}"
    },
)

start >> task1 >> task2
