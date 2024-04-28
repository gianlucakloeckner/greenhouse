# Dockerfile für die Bereitstellung meines FAST API-Backends mit MySQL und InfluxDB

# Verwenden des offiziellen Python-Images als Basisimage
FROM python:3.9-slim

# Setzen des Arbeitsverzeichnisses innerhalb des Containers
COPY src/ /app/src/
COPY main.py /app
COPY requirements.txt /app
COPY *.json /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD exec python -m uvicorn main:app --host=0.0.0.0 --port=8000
