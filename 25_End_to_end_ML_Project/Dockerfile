FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update -y && apt-get install -y awscli

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]