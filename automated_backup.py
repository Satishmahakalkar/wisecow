import os
import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='backup.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define backup details
SOURCE_DIR = '/path/to/source_directory'
REMOTE_USER = 'username'
REMOTE_HOST = 'remote.server.com'
REMOTE_DIR = '/path/to/remote_directory'
RSYNC_OPTIONS = '-avz'

def backup_directory():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    remote_backup_dir = f'{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}/{timestamp}'

    rsync_command = f'rsync {RSYNC_OPTIONS} {SOURCE_DIR} {remote_backup_dir}'
    
    try:
        result = subprocess.run(rsync_command, shell=True, check=True, 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f'Backup successful: {result.stdout.decode("utf-8")}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Backup failed: {e.stderr.decode("utf-8")}')

if __name__ == '__main__':
    backup_directory()
