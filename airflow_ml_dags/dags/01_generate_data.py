from datetime import timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "Alexey Opolchenov",
    "email": ["allthisnoise@gmail.com"],
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
        dag_id="01_generate_data",
        description="Generate random data",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=days_ago(5),
) as dag:

    generate = DockerOperator(
        task_id="docker-airflow-generate",
        image="airflow-generate",
        command="output_dir=/data/raw/{{ ds }}",
        network_mode="bridge",
        do_xcom_push=False,
        volumes=['/home/opl/docker/opl242-test/airflow_ml_dags/data/:/data/']
    )

    generate
