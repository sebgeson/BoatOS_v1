# BoatOS v0.3

Modulär startversion av BoatOS för Raspberry Pi.

## Starta
```bash
cd BoatOS_v03
python3 boatos.py
```

## Struktur
- `boatos/core` - databuss, config, logger
- `boatos/services` - navigation, motor, el, systemstatus
- `boatos/ui` - terminalbaserat dashboard just nu
- `boatos/config/settings.json` - inställningar

Denna version kör med mock-data så att allt fungerar utan sensorer.
