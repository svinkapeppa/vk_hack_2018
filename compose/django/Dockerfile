FROM python:3.6-stretch

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -qq -y install libgdal-dev

COPY ./requirements /requirements
RUN pip install -r /requirements/requirements.txt

COPY ./compose/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/django/start /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
