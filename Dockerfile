FROM python:3.10-buster

WORKDIR /var/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install --break-system-packages gunicorn

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:80