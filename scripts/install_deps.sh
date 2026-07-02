#!/bin/bash
set -e

sudo apt update
sudo apt install -y python3-venv python3-pil python3-spidev python3-gpiozero python3-smbus i2c-tools

if [ ! -d "/home/sgson/mpu" ]; then
    python3 -m venv --system-site-packages /home/sgson/mpu
fi

source /home/sgson/mpu/bin/activate
pip install smbus2 mpu6050-raspberrypi luma.lcd --no-deps || true

echo "Dependencies installerade."
