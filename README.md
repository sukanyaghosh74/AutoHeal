# Self-Healing Monitoring System

## Features
- Monitors CPU and memory
- Detects service crashes
- Automatically restarts failed service
- Logs system activity
- Dockerized
- CI/CD enabled

## Run locally
pip install -r requirements.txt
python monitor.py

## Run with Docker
docker-compose up --build

## Fault Injection
The service randomly crashes to simulate failures.
The monitor detects and restarts it automatically.
