# BoatOS Full Prototype

En komplett, körbar BoatOS-prototyp för Raspberry Pi + ILI9488 SPI TFT + MPU6050.

## Innehåll
- Dashboard med konstgjord horisont
- Systemskärm
- Menyskärm
- Navigation placeholder
- Motorsida placeholder
- App-motor med skärmhantering
- Sensorsystem för IMU, batteri och systemdata
- Widget-system
- Dag/natt-tema
- Loggning
- Autostart via systemd

## Installera på Pi

Kopiera mappen till:

```bash
/home/sgson/BoatOS
```

Kör:

```bash
cd ~/BoatOS
chmod +x scripts/*.sh
./scripts/install_deps.sh
```

Starta manuellt:

```bash
cd ~/BoatOS
source ~/mpu/bin/activate
python boatos.py
```

Autostart:

```bash
./scripts/install_service.sh
```

Stoppa service för test:

```bash
sudo systemctl stop boatos.service
```
