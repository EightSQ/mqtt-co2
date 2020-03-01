#!/usr/bin/env python

import os
import signal
import time
import paho.mqtt.client as mqttc
import mh_z19

# set sensor settings
mh_z19.detection_range_5000()
mh_z19.abc_on()

mc = mqttc.Client()

def handle_exit(signum, frame):
    global mc
    mc.loop()
    mc.loop_stop()
    mc.disconnect()
    print("Stopping sensoring")
    exit(0)

def setup_mqtt():
    global mc
    host = os.getenv("BROKER_HOST", "localhost")
    port = int(os.getenv("BROKER_PORT", 1883))
    username = os.getenv("BROKER_USER")
    password = os.getenv("BROKER_PASS")
    if username and password:
        mc.username_pw_set(username, password)
    if not port == 1883:
        mc.tls_set_context()
    mc.connect(host, port, 60)
    print(f"Connected to {host}:{port}")
    mc.loop_start()

def warmup():
    print("mh-z19 sensor warmup started.")
    # read for 60seconds in 10s intervals
    for i in range(6):
        mh_z19.read_all()
        time.sleep(10)
    print("mh-z19 sensor warmup complete!")

def main():
    print("Starting sensoring")
    if not os.getenv("NOWARMUP"):
        warmup()
    setup_mqtt()

    # define SIGTERM handler to close the connection gracefully when we get closed with C-c or systemctl stop co2
    signal.signal(signal.SIGTERM, handle_exit)

    while True:
        rs = mh_z19.read_all()
        ts = int(time.time()) # unix gmt timestamp
        mc.publish("hpi/bptf/co2", str({"type": "carbon", "ts": ts, "value": rs["co2"]}), 1, True)
        mc.publish("hpi/bptf/temp", str({"type": "temperature", "ts": ts, "value": rs["temperature"]}), 1, True)
        time.sleep(10)

if __name__ == "__main__":
    main()
