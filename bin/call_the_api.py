import os
import time
import requests

BASE_DIR = "path/to/my/dir"
REPORT_DATE = "2022-08-09"

JOB1_PORT = 8001
JOB2_PORT = 8002

RAW_DIR = os.path.join(BASE_DIR, "raw", "sales", REPORT_DATE)
STG_DIR = os.path.join(BASE_DIR, "stg", "sales", REPORT_DATE)


def run_data_saver():
    """job 1"""
    data_to_send = {
        "date": REPORT_DATE,
        "raw_dir": f"{BASE_DIR}/raw/sales/{REPORT_DATE}"
    }

    res = requests.post(f"http://localhost:{JOB1_PORT}/", json=data_to_send)
    print("run_data_saver response:", res.text)


def run_data_transformer():
    """job 2"""
    data_to_send = {
        "raw_dir": RAW_DIR,
        "stg_dir": STG_DIR
    }

    res = requests.post(f"http://localhost:{JOB2_PORT}/", json=data_to_send)
    print("\n\nrun_data_transformer response:", res.text, "run_data_transformer status_code:", res.status_code)


if __name__ == '__main__':

    run_data_saver()
    time.sleep(3)
    run_data_transformer()
