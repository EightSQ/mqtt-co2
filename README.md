# MQTT-connected MH-Z19B co2 & temperature sensor

## Requirements
- Raspberry Pi 1+ B or compatible
- MH-Z19B sensor (you can find them for less than 20$ on [aliexpress](https://www.aliexpress.com/wholesale?SearchText=mh+z19b))
- python 3 with pip

## Setup
- Enable the serial port hardware. (guides for [raspbian](https://github.com/UedaTakeyuki/mh-z19/wiki/How-to-Enable-Serial-Port-hardware-on-the-Raspberry-Pi) and [arch](https://logicalgenetics.com/serial-on-raspberry-pi-arch-linux/))
- Hook up the sensor according to the [mh-z19 library readme](https://github.com/UedaTakeyuki/mh-z19#cabling).
- `pip install -r requirements.txt`
- Run `bp_sensor.py` priviledged (for serial communication). Use `BROKER_HOST`, `BROKER_PORT`, `BROKER_USER` and `BROKER_PASS` environment variables to set up.
- Modify the topics to publish to inside the main function to fit your needs.

## Running as daemon
- Install and enable the `co2.service` in systemd. Modify it to match your installation path.
