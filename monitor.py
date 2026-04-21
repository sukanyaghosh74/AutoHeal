import psutil
import subprocess
import time
import os
from datetime import datetime

LOG_FILE = "system.log"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")
    print(message)

def is_service_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == "python.exe":
            return True
    return False

def start_service():
    subprocess.Popen(["python", "service.py"])
    log("Service restarted.")

def monitor():
    log("Monitoring started...")
    while True:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent

        log(f"CPU: {cpu}%, Memory: {mem}%")

        if not is_service_running():
            log("Service down! Restarting...")
            start_service()

        if cpu > 80:
            log("High CPU usage detected!")

        time.sleep(5)

if __name__ == "__main__":
    monitor()
