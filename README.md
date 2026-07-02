# BoatOS v1.0

Modern Pygame-baserad BoatOS för Raspberry Pi.

## Installera

```bash
cd BoatOS_v1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python boatos.py
```

Om du vill köra utan venv:

```bash
pip3 install pygame-ce psutil
python3 boatos.py
```

## Tangenter / touch

- Klicka på knapparna längst ner för sidor.
- Piltangent vänster/höger byter sida.
- ESC avslutar.

## Sidor

- Dashboard
- Navigation
- Motor
- Elsystem
- System
