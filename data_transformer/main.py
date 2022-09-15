import datetime
from flask import Flask, request
from flask import typing as flask_typing

from data_transformer import transform

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer: Transforming data
    """

    input_data: dict = request.json

    if "raw_dir" not in input_data or "stg_dir" not in input_data:
        return {
                   "message": "No path received. 'raw_dir' and 'stg_dir' need to be specified",
               }, 400
    else:
        transform.transform_and_save_data(input_data['raw_dir'], input_data['stg_dir'])

        return {
                   "message": "Data transformed successfully",
               }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8002)
