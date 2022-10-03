import os
import time
import requests

BASE_DIR = "path/to/my/dir"
JOB1_PORT = 8001
JOB2_PORT = 8002


def run_data_saver(run_date):
    """job 1"""
    data_to_send = {
        "date": run_date,
        "raw_dir": f"{BASE_DIR}/raw/sales/{run_date}"
    }

    res = requests.post(f"http://localhost:{JOB1_PORT}/", json=data_to_send)
    print("run_data_saver response:", res.text)


def run_data_transformer(run_date):
    """job 2"""
    data_to_send = {
        "raw_dir": os.path.join(BASE_DIR, "raw", "sales", run_date),
        "stg_dir": os.path.join(BASE_DIR, "stg", "sales", run_date)
    }

    res = requests.post(f"http://localhost:{JOB2_PORT}/", json=data_to_send)
    print("\nrun_data_transformer response:", res.text)


if __name__ == '__main__':
    for run_date in ['2022-08-09', '2022-08-10', '2022-08-11']:
        run_data_saver(run_date)
        time.sleep(1)
        run_data_transformer(run_date)
