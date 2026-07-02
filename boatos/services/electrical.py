import math


class ElectricalService:
    def __init__(self, bus):
        self.bus = bus
        self._t = 0

    def update(self):
        self._t += 1
        start_batt = round(12.6 + math.sin(self._t / 10) * 0.1, 2)
        house_batt = round(12.4 + math.sin(self._t / 12) * 0.08, 2)

        self.bus.publish("battery.start_v", start_batt, "electrical")
        self.bus.publish("battery.house_v", house_batt, "electrical")
        self.bus.publish("charging.status", "AV", "electrical", "WARN")
        self.bus.publish("power.current_a", "--", "electrical")
