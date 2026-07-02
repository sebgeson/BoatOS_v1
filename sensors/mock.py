import math
import time
import threading
import random

class MockSensors(threading.Thread):
    def __init__(self, bus):
        super().__init__(daemon=True)
        self.bus = bus
        self.running = True
        self.start_time = time.time()

    def run(self):
        while self.running:
            t = time.time() - self.start_time
            speed = max(0, 3.2 + math.sin(t / 3) * 3.0)
            heading = int((142 + t * 4) % 360)
            temp = 45 + math.sin(t / 8) * 3
            voltage = 12.7 + math.sin(t / 10) * 0.25
            depth = 4.6 + math.sin(t / 5) * 0.8

            self.bus.set("speed_kn", round(speed, 1))
            self.bus.set("heading_deg", heading)
            self.bus.set("engine_temp", round(temp, 1))
            self.bus.set("battery_v", round(voltage, 2))
            self.bus.set("depth_m", round(depth, 1))
            self.bus.set("gps_status", "VÄNTAR")
            self.bus.set("gps_fix", False)
            self.bus.set("opencpn", "EJ ANSLUTEN")
            self.bus.set("wifi", "ONLINE")
            self.bus.set("cpu_temp", round(42 + random.random() * 5, 1))
            time.sleep(0.5)
