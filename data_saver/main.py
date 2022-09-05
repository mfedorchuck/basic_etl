import os
import datetime
from flask import Flask, request
from flask import typing as flask_typing

from data_saver import store
from data_saver import api

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://fake-api-vycpfa6oca-uc.a.run.app"
AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer: Extract data
    """

    input_data: dict = request.json
    if "raw_dir" not in input_data:
        path = f"default_path/raw/sales/{datetime.date.today().isoformat()}"
        print("Expected 'raw_dir'. No path received. Default path set:", path)
    else:
        path = f"{input_data['raw_dir']}"

    if 'date' not in input_data:
        return {"message": "No 'date' param received. 'date' is obligatory field"}, 400
    else:
        sales_date = input_data["date"]

    # Get all the sales data (up to 100 pages from API service) in one list
    sales_data_list = api.get_sales(url=BASE_URL, token=AUTH_TOKEN, sales_date=sales_date)

    # Save that sales data local: {path}
    store_message = store.save_local(path=path, data=sales_data_list)

    return {
               "message": store_message,
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8001)
