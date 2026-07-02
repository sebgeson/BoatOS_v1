# BoatOS Dual Display

HDMI-skärmen kör huvud-UI. 3,5" SPI-touchdisplayen används som kontrollpanel.

## Start
```bash
cd BoatOS_DualDisplay
pip3 install -r requirements.txt
python3 main.py
```

## På Raspberry Pi
- HDMI visar dashboard/navigation/motor/el/larm.
- Kontrollpanelen kan köras på framebuffer om din SPI-skärm är installerad som egen display.
- Justera displaynummer i `config.py` vid behov.

## Tangenter för test på dator/Pi
- 1 Dashboard
- 2 Navigation
- 3 Motor
- 4 El
- 5 Larm
- N Nattläge
- D Dim
- ESC Avsluta
