#!/bin/bash
#set -e
#
#echo "Starting SRE Metrics MVP Stack..."
#
## Start exporter
#echo "Starting Python Exporter..."
#cd exporter
#pip install -r requirements.txt
#nohup python metrics_exporter.py > exporter.log 2>&1 &
#
## Start Prometheus
#echo "Starting Prometheus..."
#cd ../prometheus
#nohup prometheus --config.file=prometheus.yml > prometheus.log 2>&1 &
#
## Start Grafana (assuming it's installed locally)
#echo "Starting Grafana..."
#nohup grafana-server --homepath=/usr/share/grafana --config=/etc/grafana/grafana.ini > grafana.log 2>&1 &
#
#echo "All services started!"
#echo "Visit Prometheus at: http://localhost:9090"
#echo "Visit Grafana at: http://localhost:3000"
#echo "Metrics exposed at: http://localhost:8000/metrics"

#!/bin/bash
set -e

echo "Starting full SRE MVP stack using Docker Compose..."
docker-compose up --build

