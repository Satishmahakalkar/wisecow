import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk_space():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Low Disk space available: {disk_info.percent}% used')
    return disk_usage

def check_running_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name'])]
    return processes

def log_system_health():
    cpu_usage = check_cpu_usage()
    memory_usage = check_memory_usage()
    disk_usage = check_disk_space()
    processes = check_running_processes()
    
    logging.info(f'CPU Usage: {cpu_usage}%')
    logging.info(f'Memory Usage: {memory_usage}%')
    logging.info(f'Disk Usage: {disk_usage}%')
    logging.info(f'Running Processes: {len(processes)}')

if __name__ == '__main__':
    log_system_health()
