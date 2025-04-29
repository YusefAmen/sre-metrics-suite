import time
import random
import pymysql
import os

DB_HOST = os.getenv('DB_HOST', 'db')
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'testdb')

def connect_db():
    return pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

def simulate_activity():
    while True:
        try:
            connection = connect_db()
            with connection.cursor() as cursor:
                operation = random.choices(['select', 'insert', 'update', 'heavy_select'], [0.7, 0.15, 0.1, 0.05])[0]

                if operation == 'select':
                    cursor.execute("SELECT * FROM metrics_data ORDER BY RAND() LIMIT 1")
                
                elif operation == 'insert':
                    value = random.randint(1, 1000)
                    cursor.execute("INSERT INTO metrics_data (value) VALUES (%s)", (value,))
                
                elif operation == 'update':
                    value = random.randint(1, 1000)
                    cursor.execute("UPDATE metrics_data SET value = %s ORDER BY RAND() LIMIT 1", (value,))
                
                elif operation == 'heavy_select':
                    cursor.execute("SELECT * FROM metrics_data ORDER BY RAND() LIMIT 50")

                connection.commit()
            connection.close()

        except Exception as e:
            print(f"DB load error: {e}")

        time.sleep(random.uniform(0.2, 2))  # Random delay between 0.2s and 2s

if __name__ == "__main__":
    simulate_activity()

