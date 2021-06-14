ARG AIRFLOW_BASE_IMAGE="apache/airflow:2.1.0-python3.8"
FROM ${AIRFLOW_BASE_IMAGE}

RUN pip install --proxy http://proxy.houston.hpecorp.net:8080 --user --no-cache-dir \
    apache-airflow-providers-docker==1.2.0

USER root
ENV PYTHONPATH=/home/airflow/.local/lib/python3.8/site-packages