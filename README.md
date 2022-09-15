# DE2022

## job 1: data saver <br> 
Getting data from 'https://fake-api-vycpfa6oca-uc.a.run.app' service 

### Run the service:
> source data_saver/venv/bin/activate <br>
> python3 -m data_saver.main

### Call data saver for get and save data:
> params = {
        "date": {report date},
        "raw_dir": {directory for file saving}
    }
> requests.post(f"http://localhost:8001/", json=params)


## job 2: data transformer
Transform data from .json to .avro format

### Run the service:
> source data_transformer/venv/bin/activate <br>
> python3 -m data_transformer.main

### Call data transform service for transform and save data:
> params = {
        "raw_dir": {directory with .json file}, 
        "stg_dir": {directory for .avro file saving}
    }
> requests.post(f"http://localhost:8002/", json=params)