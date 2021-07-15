FROM python:2.2.10

WORKDIR /code

COPY requirements.txt .

RUN pip install -r /code/requirements.txt

COPY . .

CMD gunicorn test_task_fr.wsgi:application --bind 0.0.0.0:8000