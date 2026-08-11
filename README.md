# PC IoT Monitor

A Docker-based system monitoring project using Python, MQTT,
Node-RED and InfluxDB.

## Architecture

Python → MQTT/Aedes → Node-RED → InfluxDB
                             ↓
                         Dashboard

## Technologies

- Python
- psutil
- Paho MQTT
- MQTT
- Aedes
- Node-RED
- InfluxDB
- Docker
- Docker Compose

## Metrics

The system monitors:

- CPU usage
- RAM usage
- Available RAM
- Disk usage
- Free disk space
- System uptime

## Running

### 1. Clone

```bash
git clone <repository>
cd PC-IoT-Monitor
```

2. Configure environment
```bash
cp .env.example .env
```

Configure the variables.

3. Start infrastructure
```bash
docker compose up -d
```

4. Run the monitor

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows:

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r monitor/requirements.txt
```

Run:

```bash
python monitor/src/monitor.py
```

Node-RED

http://localhost:1880

Dashboard

http://localhost:1880/dashboard

InfluxDB

http://localhost:8086