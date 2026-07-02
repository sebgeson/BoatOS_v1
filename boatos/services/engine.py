import math


class EngineService:
    def __init__(self, bus):
        self.bus = bus
        self._t = 0

    def update(self):
        self._t += 1
        temp = round(45 + math.sin(self._t / 8) * 2, 1)
        rpm = 0

        self.bus.publish("engine.temp_c", temp, "engine")
        self.bus.publish("engine.rpm", rpm, "engine", "WARN")
        self.bus.publish("engine.oil_pressure", "OK", "engine")
        self.bus.publish("engine.cooling", "OK", "engine")
