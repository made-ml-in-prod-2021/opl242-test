from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor


default_args = {
    "owner": "Alexey Opolchenov",
    "email": ["allthisnoise@gmail.com"],
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        dag_id="02_train_model_pipeline",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=days_ago(5),
) as dag:

    data_sensor = FileSensor(
        task_id = "waiting_for_data",
        poke_interval = 10,
        retries = 100,
        filepath = "data/raw/{{ ds }}/data.csv"
    )
    
    target_sensor = FileSensor(
        task_id = "waiting_for_target",
        poke_interval = 10,
        retries = 100,
        filepath = "data/raw/{{ ds }}/target.csv"
    )

    # - подготовить данные для обучения(например, считать из /data/raw/{{ ds }} и положить /data/processed/{{ ds }}/train_data.csv)
    preprocess = DockerOperator(
        image="airflow-preprocess",
        command="--input_dir=/data/raw/{{ ds }} --output_dir=/data/processed/{{ ds }}",
        task_id="docker-airflow-preprocess",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes=['/home/opl/docker/opl242-test/airflow_ml_dags/data/:/data/'],
    )

    # - расплитить их на train/val
    train_test_split = DockerOperator(
        image="airflow-split",
        command="--data_dir=/data/processed/{{ ds }} --output_dir=/data/split/{{ ds }}",
        task_id="docker-airflow-split",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes=['/home/opl/docker/opl242-test/airflow_ml_dags/data/:/data/'],
    )

    # - обучить модель на train (сохранить в /data/models/{{ ds }} 
    train = DockerOperator(
        image="airflow-train",
        command="--data_dir=/data/split/{{ ds }} --model_dir=/data/models/{{ ds }}",
        task_id="docker-airflow-train",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes=['/home/opl/docker/opl242-test/airflow_ml_dags/data/:/data/'],
    )

    # - провалидировать модель на val (сохранить метрики к модельке)
    eval = DockerOperator(
        image="airflow-eval",
        command="--data_dir=/data/split/{{ ds }} --model_dir=/data/models/{{ ds }} --val_dir=/data/validation/{{ ds }}",
        task_id="docker-airflow-eval",
        network_mode = "bridge",
        do_xcom_push = False,
        volumes=['/home/opl/docker/opl242-test/airflow_ml_dags/data/:/data/'],
    )

    [data_sensor, target_sensor] >> preprocess >> train_test_split >> train >> eval