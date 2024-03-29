from paho.mqtt import client as mqtt_client
import random
# from PyQt6 import QtWidgets, uic
#
# app = QtWidgets.QApplication([])
# ui = uic.loadUi("design.ui")
# ui.setWindowTitle("Application for Arduino")
# ui.show()
# app.exec()

broker = '130.193.44.244'
port = 1883
topic = "$devices/areqilcg9djp8id7g4ns/events"
client_id = 'arer7bd08p7qg2h6a8rq'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()