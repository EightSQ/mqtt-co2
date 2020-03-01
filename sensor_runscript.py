#!/bin/bash

exec env BROKER_HOST=localhost BROKER_PORT=1883 BROKER_USER=username BROKER_PASS=password python3 /root/bpco2/bp_sensor.py
