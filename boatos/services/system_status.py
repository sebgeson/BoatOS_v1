import os
import subprocess


class SystemStatusService:
    def __init__(self, bus):
        self.bus = bus

    def _cpu_temp(self):
        path = "/sys/class/thermal/thermal_zone0/temp"
        try:
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return round(int(f.read().strip()) / 1000, 1)
        except Exception:
            pass
        return "--"

    def _wifi_status(self):
        try:
            result = subprocess.run(["iwgetid", "-r"], capture_output=True, text=True, timeout=1)
            ssid = result.stdout.strip()
            return ssid if ssid else "OFFLINE"
        except Exception:
            return "UNKNOWN"

    def update(self):
        self.bus.publish("system.cpu_temp_c", self._cpu_temp(), "system")
        self.bus.publish("system.wifi", self._wifi_status(), "system")
        self.bus.publish("system.opencpn", "EJ ANSLUTEN", "system", "WARN")
