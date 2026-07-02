class Battery:
    def __init__(self):
        self.fake_voltage = 12.8

    def read(self):
        return {
            "voltage": self.fake_voltage,
            "status": "OK"
        }
