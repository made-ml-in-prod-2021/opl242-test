FROM airflow-ml-base-opl:latest

COPY preprocess.py /preprocess.py
COPY class_codes.csv /class_codes.csv
COPY color_codes.csv /color_codes.csv

ENTRYPOINT ["python", "preprocess.py"]