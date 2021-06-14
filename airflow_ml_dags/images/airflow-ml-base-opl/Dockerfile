FROM python:3.8-slim
RUN mkdir /build/
COPY requirements.txt /build/requirements.txt

RUN pip install --proxy http://proxy.houston.hpecorp.net:8080 -r /build/requirements.txt