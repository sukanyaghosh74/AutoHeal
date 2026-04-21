# 🔧 SRE Self-Healing System

A production-ready, automated system monitoring and recovery platform that detects service failures and automatically restores them without manual intervention. Built for reliability engineers who need resilient, self-managing infrastructure.

[![Python 3.10](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-brightgreen.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Monitoring & Logs](#monitoring--logs)
- [Deployment](#deployment)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## 🎯 Overview

The SRE Self-Healing System is an autonomous monitoring and recovery solution that:
- **Detects** service failures in real-time
- **Diagnoses** system resource issues (CPU, memory)
- **Recovers** failed services automatically
- **Logs** all events for audit trails and analysis

Perfect for microservices architectures, critical applications, and environments where downtime is costly. This system eliminates the need for manual intervention during common failure scenarios.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **Auto-Recovery** | Automatically restarts crashed services without manual intervention |
| **Resource Monitoring** | Real-time CPU and memory utilization tracking |
| **Intelligent Alerts** | Detects high resource usage and alerts operators |
| **Comprehensive Logging** | Detailed system activity logs with timestamps |
| **dockerized** | Production-ready Docker container configuration |
| **Lightweight** | Minimal dependencies, efficient resource usage |
| **Fault Injection** | Built-in chaos testing for reliability validation |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│       SRE Self-Healing System               │
├─────────────────────────────────────────────┤
│                                             │
│  ┌────────────────────────────────────┐   │
│  │     Monitor (monitor.py)           │   │
│  │  • System resource tracking        │   │
│  │  • Process health checks           │   │
│  │  • Auto-restart logic              │   │
│  │  • Event logging                   │   │
│  └────────────────────────────────────┘   │
│            │                               │
│            │ Tracks & Restarts            │
│            ▼                               │
│  ┌────────────────────────────────────┐   │
│  │    Service (service.py)            │   │
│  │  • Application process             │   │
│  │  • Fault injection (simulated)     │   │
│  │  • Periodic health signals         │   │
│  └────────────────────────────────────┘   │
│            │                               │
│            │ Logs to                       │
│            ▼                               │
│  ┌────────────────────────────────────┐   │
│  │    system.log                      │   │
│  │  • Events & metrics                │   │
│  │  • Restart history                 │   │
│  └────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 📦 Prerequisites

- **Python 3.10+**
- **Docker & Docker Compose** (for containerized deployment)
- **psutil** (automatically installed via requirements)

---

## 🚀 Quick Start

### Option 1: Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sukanyaghosh74/AutoHeal.git
   cd sre-self-healing-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the monitoring system**
   ```bash
   python monitor.py
   ```

4. **Verify it's working**
   ```
   You should see output:
   - Monitoring started...
   - CPU: XX%, Memory: YY%
   - Service running...
   ```

### Option 2: Docker Deployment (Recommended)

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **View logs**
   ```bash
   docker logs -f sre-monitor
   ```

3. **Stop the system**
   ```bash
   docker-compose down
   ```

---

## ⚙️ Configuration

### Monitor Thresholds

Edit `monitor.py` to customize:

```python
# CPU threshold (default: 80%)
if cpu > 80:
    log("High CPU usage detected!")

# Memory threshold (default: shown but not triggered)
# Add conditions as needed

# Check interval (default: 5 seconds)
time.sleep(5)
```

### Service Configuration

Edit `service.py` to adjust:

```python
# Crash frequency (1 in 10 attempts)
if random.randint(1, 10) == 5:
    print("Simulating crash...")
    exit(1)

# Health check interval (default: 3 seconds)
time.sleep(3)
```

---

## 🔍 How It Works

### Monitoring Cycle (5-second intervals)

1. **Health Check** → Verifies if the service process is running
2. **Resource Monitoring** → Collects CPU and memory metrics
3. **Alert Generation** → Detects thresholds (e.g., CPU > 80%)
4. **Auto-Recovery** → If service is down, automatically restarts it
5. **Logging** → Records all events with timestamps

### Failure Scenario Example

```
[2026-04-21 10:15:30.123456] - Monitoring started...
[2026-04-21 10:15:30.654321] - CPU: 45%, Memory: 62%
[2026-04-21 10:15:35.789012] - CPU: 52%, Memory: 65%
[2026-04-21 10:15:40.345678] - Service down! Restarting...
[2026-04-21 10:15:40.456789] - Service restarted.
[2026-04-21 10:15:45.567890] - CPU: 48%, Memory: 64%
```

---

## 📊 Monitoring & Logs

### Accessing Logs

**Local deployment:**
```bash
tail -f system.log
```

**Docker deployment:**
```bash
docker logs -f sre-monitor
```

### Log Format

Each log entry includes:
- **Timestamp** → When the event occurred
- **Metric/Event** → What was monitored (CPU, memory, restarts)
- **Value** → Current measurement or status

### Log Examples

```
2026-04-21 10:15:30.123456 - Monitoring started...
2026-04-21 10:15:35.234567 - CPU: 45%, Memory: 62%
2026-04-21 10:15:40.345678 - Service down! Restarting...
2026-04-21 10:15:40.456789 - Service restarted.
2026-04-21 10:15:50.567890 - High CPU usage detected!
```

### Analyzing Logs

Extract restart events:
```bash
grep "Service restarted" system.log | wc -l
```

Extract high-CPU events:
```bash
grep "High CPU" system.log
```

---

## 🐳 Deployment

### Docker Container Details

- **Base Image:** Python 3.10
- **Working Directory:** `/app`
- **Default Command:** `python monitor.py`
- **Restart Policy:** Always (unless manually stopped)

### Docker Compose Setup

```yaml
version: '3'
services:
  monitor:
    build: .
    container_name: sre-monitor
    restart: always
```

### Production Deployment Options

**Option A: Kubernetes**
```bash
kubectl apply -f k8s-deployment.yaml
```

**Option B: Systemd Service** (Linux)
```bash
sudo cp sre-monitor.service /etc/systemd/system/
sudo systemctl enable sre-monitor
sudo systemctl start sre-monitor
```

**Option C: Docker Swarm**
```bash
docker service create --name sre-monitor --restart-condition any .
```

---

## 👨‍💻 Development

### Project Structure
```
sre-self-healing-system/
├── monitor.py           # Main monitoring loop
├── service.py           # Service to be monitored
├── system.log          # Generated logs
├── Dockerfile          # Container configuration
├── docker-compose.yml  # Multi-container setup
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

### Running Tests

**Manual testing with fault injection:**
```bash
python monitor.py &
python service.py
# Observe monitor detect crash and restart service
```

**Stress testing:**
```bash
# Monitor high load scenarios
docker run -it --rm sre-monitor
# Monitor should handle CPU/memory spikes gracefully
```

### Development Workflow

1. Make changes to `monitor.py` or `service.py`
2. Test locally: `python monitor.py`
3. Test in Docker: `docker-compose up --build`
4. Commit changes: `git commit -am "Description"`
5. Push to main: `git push origin main`

---

## 🆘 Troubleshooting

### Issue: Monitor not detecting crashes

**Solution:** Verify the service process name matches in `monitor.py`
```python
if proc.info['name'] == "python.exe":  # Adjust based on OS
```

### Issue: High memory usage

**Cause:** Logs growing too large
**Solution:** Rotate logs or clear old entries
```bash
> system.log  # Clear logs (Linux/Mac: > system.log)
```

### Issue: Docker container won't start

**Solution:** Check logs and rebuild
```bash
docker-compose down
docker-compose up --build
docker logs sre-monitor
```

### Issue: Permission denied errors

**Solution:** Grant execution permissions
```bash
chmod +x monitor.py service.py
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Make** your changes
4. **Test** thoroughly
5. **Commit** with clear messages (`git commit -m 'Add AmazingFeature'`)
6. **Push** to your branch (`git push origin feature/AmazingFeature`)
7. **Open** a Pull Request

### Areas for Contribution

- [ ] Advanced alerting (Slack, email, PagerDuty integration)
- [ ] Database logging (replace file-based logs)
- [ ] Web dashboard for visualization
- [ ] Custom recovery strategies
- [ ] Windows service support
- [ ] Kubernetes operator
- [ ] Performance benchmarking
- [ ] Unit test coverage

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Support & Questions

- **Issues:** [GitHub Issues](https://github.com/sukanyaghosh74/AutoHeal/issues)
- **Documentation:** Check this README and inline code comments
- **Contributing:** See [Contributing](#contributing) section

---

## 🎓 Learning Resources

- [SRE Principles](https://sre.google/)
- [psutil Documentation](https://psutil.readthedocs.io/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Python Monitoring Tools](https://docs.python.org/3/library/profile.html)

---

**Built by the reliability engineering community** ⚙️
