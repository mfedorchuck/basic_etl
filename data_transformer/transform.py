import json
import os
import shutil
from fastavro import writer, parse_schema


def clear_data_at_directory(path: str) -> None:
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete files at {path}; Reason: {e}")


def get_schema() -> dict:
    schema = {
        'doc': 'Sales records',
        'name': 'sales',
        'namespace': 'stage',
        'type': 'record',
        'fields': [
            {'name': 'client', 'type': 'string'},
            {'name': 'purchase_date', 'type': 'string'},
            {'name': 'product', 'type': 'string'},
            {'name': 'price', 'type': 'int'},
        ],
    }

    return parse_schema(schema)


def transform_and_save_data(raw_dir_path: str, stg_dir_path: str) -> str:
    """
    Transforming .json data into .avro format and save it.
    Return status
    """

    # Prepare the path
    os.makedirs(name=stg_dir_path, exist_ok=True)
    clear_data_at_directory(stg_dir_path)

    with open(f'{raw_dir_path}/data.json', 'r') as raw_file:
        data = json.load(raw_file)

    schema = get_schema()

    with open(f"{stg_dir_path}/avro_data.avro", "wb") as stg_file:
        writer(stg_file, schema, data)

    return "Data transformed successfully"
