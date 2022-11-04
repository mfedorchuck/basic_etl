#!/usr/bin/env bash

# Fetching the docker-compose.yaml file (we will be using Airflow v2.4.1)
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.4.1/docker-compose.yaml'

# create infrastructure dirs
mkdir ./dags ./logs ./plugins

# Setting the Airflow user
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# AFTER THAT - ensure you have .env with correct params:
#$ cat .env
#AIRFLOW_UID=501
#AIRFLOW_GID=0
