FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY metrics_exporter.py .
COPY simulate_backup.py .
COPY db_load_generator.py .

CMD ["sh", "-c", "python simulate_backup.py & python db_load_generator.py & python metrics_exporter.py"]

