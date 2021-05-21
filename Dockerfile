FROM python:3.9-slim
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN adduser ml
WORKDIR /home/ml
COPY docker_requirements.txt ./requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install --proxy http://proxy.houston.hpecorp.net:8080 -r requirements.txt
RUN venv/bin/pip install --proxy http://proxy.houston.hpecorp.net:8080 gunicorn

RUN mkdir models
COPY models models
RUN mkdir -p online_inference/app
COPY online_inference/app online_inference/app
COPY online_inference/online_inference.py online_inference
COPY online_inference/__init__.py online_inference
COPY online_inference/setup.py online_inference
COPY online_inference/setup.py ./	
COPY boot.sh ./

RUN python -m venv venv

RUN chmod +x boot.sh
RUN chown -R ml:ml online_inference
RUN chown -R ml:ml models
USER ml

EXPOSE 5000
# ENTRYPOINT ["./boot.sh"]
