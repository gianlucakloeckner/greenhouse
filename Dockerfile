# Dockerfile für die Bereitstellung meines FAST API-Backends mit MySQL und InfluxDB

# Verwenden des offiziellen Python-Images als Basisimage
FROM python:3.9-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


WORKDIR /app

# Setzen des Arbeitsverzeichnisses innerhalb des Containers
COPY src/ /app/src/
COPY main.py /app
COPY requirements.txt /app
COPY *.json /app



RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

HEALTHCHECK --interval=5s \
    --timeout=5s \
    CMD curl -f http://127.0.0.1:8000 || exit 1

CMD exec python -m uvicorn main:app --host=0.0.0.0 --port=8000
