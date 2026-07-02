import time


class DataHub:
    """Gemensam databuss för BoatOS.

    Alla sensorer skriver hit. Alla skärmar läser härifrån.
    Det gör systemet enklare att bygga ut med GPS, batteri, NMEA och larm.
    """

    def __init__(self):
        self.data = {
            "roll": 0.0,
            "pitch": 0.0,
            "imu_ok": False,
            "battery": {"voltage": 12.8, "status": "OK", "current": 0.0},
            "system": {"cpu_temp": 0.0, "fps": 0, "uptime": 0},
            "gps": {"gps_fix": False, "speed_kn": 0.0, "course": None, "lat": None, "lon": None, "sats": 0},
            "engine": {"rpm": 0, "temp": 0, "charging": False, "oil": "OK", "hours": 0.0},
            "alarms": [],
            "last_update": time.time(),
        }

    def update(self, **sections):
        for key, value in sections.items():
            if isinstance(value, dict) and isinstance(self.data.get(key), dict):
                self.data[key].update(value)
            else:
                self.data[key] = value
        self.data["last_update"] = time.time()
        return self.data

    def snapshot(self):
        return self.data
