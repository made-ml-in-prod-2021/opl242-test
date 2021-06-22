from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor
from airflow.models import Variable

default_args = {
    "owner": "Alexey Opolchenov",
    "email": ["allthisnoise@gmail.com"],
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
        dag_id="03_inference",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:

    path_to_model = Variable.get("PATH_TO_MODEL", "/data/models/{{ ds }}")

    data_sensor = FileSensor(
        task_id = "waiting_for_data",
        poke_interval = 5,
        retries = 100,
        filepath = "data/raw/{{ ds }}/data.csv"
    )
        
    model_sensor = FileSensor(
        task_id = "waiting_for_model",
        poke_interval = 5,
        retries = 100,
        filepath = path_to_model + "/model.pkl"
    )

    inference = DockerOperator(
        task_id="docker-airflow-predict",
        image="airflow-predict",
        command="--input_dir=/data/raw/{{ ds }} --output_dir=/data/predictions/{{ ds }}"\
            f" --model_dir={path_to_model}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=['/home/opl/docker/opl242-test/airflow_ml_dags/data/:/data/'],
    )

    [data_sensor, model_sensor] >> inference
