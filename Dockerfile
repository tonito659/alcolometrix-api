FROM python:slim
RUN pip3 install gunicorn json-logging-py flask
COPY . /app
WORKDIR /app
EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "/app/gunicorn.conf", "--log-config", "/app/logging.conf", "-b", ":5000", "app:app"]
