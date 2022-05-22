import paho.mqtt.client as mqtt
import time

HOST = "mqtt.cloud.yandex.net"
PORT = 8883


def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    client = mqtt.Client(client_id)  # ClientId не может быть повторен, поэтому используйте текущее время
    client.username_pw_set("arer7bd08p7qg2h6a8rq", "Parolparol3214")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("A")


def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload.decode("utf-8"))


if __name__ == '__main__':
    client_loop()