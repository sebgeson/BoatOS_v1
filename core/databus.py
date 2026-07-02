import time
import math
import psutil

class DataBus:
    def __init__(self):
        self.page = "dashboard"
        self.night_mode = False
        self.dimmed = False
        self.started = time.time()
        self.data = {}

    def update_mock(self):
        t = time.time() - self.started
        self.data.update({
            "speed_kn": max(0, 3.2 + math.sin(t / 6) * 3.1),
            "heading": int((142 + t * 2) % 360),
            "depth_m": 4.6 + math.sin(t / 5) * 0.8,
            "engine_temp": int(65 + math.sin(t / 7) * 8),
            "battery_v": round(12.7 + math.sin(t / 10) * 0.5, 2),
            "cpu_temp": self._cpu_temp(),
            "gps": "VÄNTAR",
            "wifi": "ONLINE",
            "opencpn": "EJ ANSLUTEN",
            "runtime_h": round(t / 3600, 2),
        })

    def _cpu_temp(self):
        try:
            with open('/sys/class/thermal/thermal_zone0/temp') as f:
                return round(int(f.read()) / 1000, 1)
        except Exception:
            return 45.0

    def set_page(self, page):
        self.page = page

    def toggle_night(self):
        self.night_mode = not self.night_mode

    def toggle_dim(self):
        self.dimmed = not self.dimmed
