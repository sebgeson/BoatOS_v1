# BoatOS v1.0 Prototype

BoatOS är en marin instrumentpanel för Raspberry Pi med 4.0" SPI TFT-display och MPU6050.

## Funktioner
- Startskärm
- Konstgjord horisont
- Krängning / roll
- Stampning / pitch
- Batteriruta med simulerat värde
- CPU-temp och FPS
- Dashboard och systemskärm
- Modulär struktur med widgets, screens, sensors och themes
- Systemd-autostart

## Testad hårdvara
- Raspberry Pi Zero W / Zero 2 W
- 4.0" SPI TFT 480x320, ILI9488
- MPU6050 via I2C adress 0x68

## Starta manuellt

```bash
cd ~/BoatOS
source ~/mpu/bin/activate
python boatos.py
```

## Installera autostart

```bash
chmod +x scripts/install_service.sh
./scripts/install_service.sh
```

## Stoppa service vid manuell testning

```bash
sudo systemctl stop boatos.service
```

## Starta service

```bash
sudo systemctl restart boatos.service
```
