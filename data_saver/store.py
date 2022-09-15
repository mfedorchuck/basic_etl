import os
import shutil
import json


def clear_data_at_directory(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)

        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def save_local(path: str, data: list) -> None:
    os.makedirs(name=path, exist_ok=True)
    clear_data_at_directory(path)

    with open(f"{path}/data.json", "w") as f:
        json.dump(data, f)

    print(f"data was saved successfully at {path}")
