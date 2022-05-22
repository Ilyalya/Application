import paho.mqtt.client as mqtt

mqtt_broker = "mqtt.cloud.yandex.net"
mqtt_broker_port = 8883
mqtt_client_id = f"ozna_ds_publisher_{random.randint(0, 1000000)}"
mqtt_keepalive = 5 * 60

client = mqtt_client.Client(mqtt_client_id)
client.tls_set("C:/Works/mqtt-rest-bridge/cert.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True)
client.connect(mqtt_broker, mqtt_broker_port, keepalive=mqtt_keepalive)