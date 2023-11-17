FROM python:3.11.4-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD admin

WORKDIR /app

RUN pip3 install --upgrade pip
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --email admin@localhost --noinput; \
    python3 manage.py runserver 0.0.0.0:8000

ADD . /app
