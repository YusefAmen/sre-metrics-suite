import os
import time
import random

BACKUP_PATH = '/backup/backup.sql'

def create_backup():
    with open(BACKUP_PATH, 'w') as f:
        f.write('FAKE BACKUP DATA')

def remove_backup():
    if os.path.exists(BACKUP_PATH):
        os.remove(BACKUP_PATH)

if __name__ == "__main__":
    while True:
        action = random.choice(['create', 'remove'])
        if action == 'create':
            print("Simulating backup creation.")
            create_backup()
        else:
            print("Simulating backup removal.")
            remove_backup()

        time.sleep(random.randint(30, 60))  # Every 30-60 seconds

