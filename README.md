# BoatOS Premium v0.4

Grafisk BoatOS-version för Raspberry Pi + ILI9488 + MPU6050.

## Nytt i v0.4

- DataHub: gemensam databuss för alla sensorer
- AlarmEngine: första larmmotorn
- Ny dashboard med fart/kurs/motor/batteri
- Ny elsystem-sida
- Statusrad med GPS/IMU/larm
- IMU kraschar inte längre appen om sensorn saknas
- Mock-läge för GPS, motor och batteri tills riktiga sensorer kopplas in

## Kör

```bash
cd ~/BoatOS
source ~/mpu/bin/activate
python boatos.py
```

## Installera som service

```bash
chmod +x scripts/*.sh
./scripts/install_service.sh
```

## Nästa steg

1. Koppla riktig GPS/NMEA0183.
2. Koppla batterispänning via ADC.
3. Koppla motorvarv/temp.
4. Bygga pek/touch-navigation i stället för automatisk sidväxling.
