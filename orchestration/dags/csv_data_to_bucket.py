from google.cloud import storage

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

from os import path, listdir
from datetime import datetime

BASE_PATH = path.dirname(__file__)


def upload_data(source_file_path: str, bucket_name: str, destination_bucket_path: str) -> None:
    """Upload file to the Google Cloud bucket"""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_bucket_path)
    blob.upload_from_filename(source_file_path)

    print("---", f"File from {source_file_path} uploaded to {destination_bucket_path}.", "---", sep="\n")


def upload_dataset(execution_date: str) -> None:
    """
    execution_date: execution date in format '%Y-%m-%d'
    Getting files and path.
    Run upload_data() function for upload all the files by using `google.cloud` module
    """

    dir_path = path.abspath(path.join(BASE_PATH, "..", "sales", f"{execution_date}"))

    for file_name in listdir(dir_path):
        file_path = path.join(dir_path, file_name)
        destination_path = f"src1/sales/v1/{str(execution_date).split('-')[0]}/" \
                           f"{str(execution_date).split('-')[1]}/" \
                           f"{str(execution_date).split('-')[2]}/" \
                           f"{file_name}"

        upload_data(source_file_path=file_path,
                    bucket_name="sales_raw_data",
                    destination_bucket_path=destination_path)


dag = DAG(
    dag_id="csv_data_to_bucket",
    start_date=datetime(2022, 8, 1),
    end_date=datetime(2022, 8, 3),

    schedule="0 1 * * *",
    catchup=True,
)

start = EmptyOperator(
    task_id="start_task",
    dag=dag,
)

task_1 = PythonOperator(
    task_id="upload_data_for_current_date",
    dag=dag,
    python_callable=upload_dataset,
    op_kwargs={
        "execution_date": "{{ execution_date.strftime('%Y-%m-%d') }}"
    },
)

start >> task_1
