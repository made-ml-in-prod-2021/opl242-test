FROM airflow-ml-base-opl:latest

COPY generate.py /generate.py
COPY config.yaml /config.yaml

ENTRYPOINT ["python", "generate.py"]