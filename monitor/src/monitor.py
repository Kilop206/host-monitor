import time
import socket
import psutil
import json
import paho.mqtt.client as mqtt


BROKER_HOST = "localhost"
BROKER_PORT = 1884
TOPIC = "lab/devices/pc-main/telemetry"
INTERVAL = 5

def collect_metrics():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")

    # Estrutura otimizada em Time Series para o InfluxDB v2
    return {
        "measurement": "host_performance",
        "tags": {
            "hostname": socket.gethostname()
        },
        "fields": {
            "cpu_usage": psutil.cpu_percent(interval=1),
            "ram_usage": memory.percent,
            "ram_available": memory.available,
            "disk_usage": disk.percent,
            "disk_free": disk.free,
            "uptime": time.time() - psutil.boot_time()
        }
    }


def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Succesfully Connected!")
    else:
        print(f"Fail to connect. Error code: {rc}")


cliente = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
cliente.on_connect = on_connect

print("Connecting to broker...")
cliente.connect(BROKER_HOST, BROKER_PORT, 60)


try:
    while True:
        metrics = collect_metrics()
        mensagem_json = json.dumps(metrics)
        cliente.publish(TOPIC, mensagem_json)
        print(
            f"Sent via MQTT | CPU: {metrics['fields']['cpu_usage']}% | "
            f"RAM: {metrics['fields']['ram_usage']}% | "
            f"DISK: {metrics['fields']['disk_usage']}%"
        )
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\nFinishing monitoring")
    cliente.disconnect()

except Exception as e:
    print(f"\nError occurred: {e}")
    cliente.disconnect()
