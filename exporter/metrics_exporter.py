from prometheus_client import start_http_server, Gauge
import time
import pymysql  # Example: for MySQL - change to psycopg2 if PostgreSQL
import os

# Metrics
query_latency = Gauge('db_query_latency_seconds', 'Database query latency in seconds')
replication_lag = Gauge('db_replication_lag_seconds', 'Database replication lag in seconds')
backup_status = Gauge('db_backup_success', 'Database backup status (1=success, 0=failure)')

# DB connection parameters
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'yourdb')

# Backup file path to check
BACKUP_FILE_PATH = os.getenv('BACKUP_FILE_PATH', '/path/to/your/backup.sql')

def measure_query_latency():
    start = time.time()
    try:
        connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        connection.close()
        latency = time.time() - start
        query_latency.set(latency)
    except Exception as e:
        print(f"Error measuring query latency: {e}")
        query_latency.set(-1)  # Signal an error

def measure_replication_lag():
    try:
        connection = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SHOW SLAVE STATUS")
            result = cursor.fetchone()
            if result and 'Seconds_Behind_Master' in result:
                lag = result['Seconds_Behind_Master'] or 0
                replication_lag.set(lag)
            else:
                replication_lag.set(-1)
        connection.close()
    except Exception as e:
        print(f"Error measuring replication lag: {e}")
        replication_lag.set(-1)

def check_backup_status():
    try:
        if os.path.exists(BACKUP_FILE_PATH):
            backup_status.set(1)
        else:
            backup_status.set(0)
    except Exception as e:
        print(f"Error checking backup file: {e}")
        backup_status.set(0)

def collect_metrics():
    while True:
        measure_query_latency()
        measure_replication_lag()
        check_backup_status()
        time.sleep(10)

if __name__ == '__main__':
    start_http_server(8000)
    collect_metrics()

