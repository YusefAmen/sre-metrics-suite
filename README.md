# sre-metrics-suite

Minimal Prometheus exporter and Grafana dashboard to monitor:
- Database query latency
- Database replication lag
- Backup status

## Components
- **Python exporter**: Exposes custom Prometheus metrics at `/metrics`
- **Prometheus config**: Scrapes the metrics
- **Grafana dashboard**: Visualizes them

## Quickstart

1. Install Python dependencies:

```bash
cd exporter
pip install -r requirements.txt
python metrics_exporter.py

