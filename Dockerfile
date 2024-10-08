FROM alpine:latest

COPY config/cronjobs /etc/crontabs/root

COPY requirements.txt /etc/requirements/requirements.txt

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-pip make && ln -sf python3 /usr/bin/python

COPY .env /code/.env
COPY api /code/api
COPY auth /code/auth
COPY tweets /code/tweets
COPY Makefile /code/Makefile

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r /etc/requirements/requirements.txt

# start crond with log level 8 in foreground, output to stderr
CMD ["crond", "-f", "-d", "8"]
