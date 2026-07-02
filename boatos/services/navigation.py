import math
import time


class NavigationService:
    def __init__(self, bus):
        self.bus = bus
        self._t = 0

    def update(self):
        # Mock-data tills riktig GPS kopplas in
        self._t += 1
        speed = round(max(0, 3.2 + math.sin(self._t / 5) * 0.4), 1)
        course = int((142 + self._t) % 360)

        self.bus.publish("gps.status", "VÄNTAR", "navigation", "WARN")
        self.bus.publish("nav.speed_kn", speed, "navigation")
        self.bus.publish("nav.course_deg", course, "navigation")
        self.bus.publish("nav.position", "INGEN FIX", "navigation", "WARN")
        self.bus.publish("nav.satellites", 0, "navigation", "WARN")
