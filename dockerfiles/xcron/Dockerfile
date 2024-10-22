FROM alpine:latest

COPY config/cronjobs /etc/crontabs/root

COPY requirements.txt /etc/requirements/requirements.txt

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-pip make bash \
	util-linux vim tzdata && ln -sf python3 /usr/bin/python

ENV TZ Europe/Berlin

COPY .env /code/.env
COPY api /code/api
COPY auth /code/auth
COPY migrations/down /code/migrations/down
COPY migrations/up /code/migrations/up
COPY migrations/down.py /code/migrations/down.py
COPY migrations/up.py /code/migrations/up.py
COPY socialplatforms /code/socialplatforms
COPY Makefile /code/Makefile

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

RUN pip install -r /etc/requirements/requirements.txt

RUN chmod 777 /etc/crontabs/root

WORKDIR /code

CMD ["crond", "-f", "-d", "8"]
