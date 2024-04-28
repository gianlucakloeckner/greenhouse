# Dockerfile für die Bereitstellung meines FAST API-Backends mit MySQL und InfluxDB

# Verwenden des offiziellen Python-Images als Basisimage
FROM python:3.9-slim

# Setzen des Arbeitsverzeichnisses innerhalb des Containers
WORKDIR /app

# Kopieren der Anforderungen in das Arbeitsverzeichnis
COPY requirements.txt .

# Installation der erforderlichen Python-Pakete
RUN pip install --no-cache-dir -r requirements.txt

# Installation von MySQL Client
RUN apt-get update && apt-get install -y default-mysql-client

# Installation von InfluxDB Client
RUN pip install influxdb

# Kopieren des gesamten Projektinhalts in das Arbeitsverzeichnis
COPY . .

# Exponieren des Ports, auf dem die FastAPI-Anwendung läuft
EXPOSE 8000

# Umgebungsvariablen für MySQL und InfluxDB Konfiguration
ENV MYSQL_HOST=localhost
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=your_password
ENV INFLUXDB_HOST=localhost
ENV INFLUXDB_PORT=8086
ENV INFLUXDB_USER=root
ENV INFLUXDB_PASSWORD=your_password

# Starten der FastAPI-Anwendung beim Ausführen des Containers
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]