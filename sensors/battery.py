class Battery:
    def __init__(self):
        self.fake_voltage = 12.8

    def read(self):
        # Tillfälligt simulerat värde.
        # Senare ersätts detta med INA219, INA226 eller ADS1115.
        return {
            "voltage": self.fake_voltage,
            "status": "OK"
        }
