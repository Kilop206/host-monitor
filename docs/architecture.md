# Architecture

## Overview

The project collects host system metrics using Python and
publishes them through MQTT.

```text
Python Monitor
      |
      | MQTT
      v
Aedes Broker
      |
      v
   Node-RED
   |      \
   |       \
   v        v
InfluxDB  Dashboard
```

Metrics

The monitor publishes:

CPU usage
RAM usage
Available RAM
Disk usage
Free disk space
System uptime
MQTT

Topic:

```
host/metrics
```

Example payload:

```json
{
  "cpu_usage": 32.4,
  "ram_usage": 61.2,
  "ram_available": 5368709120,
  "disk_usage": 48.1,
  "disk_free": 335544320000,
  "uptime": 123456
}
```