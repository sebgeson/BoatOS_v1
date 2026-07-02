class Battery:
    def read(self):
        # Mock tills vi kopplar riktig ADC/shunt.
        voltage = 12.8
        status = "OK" if voltage >= 12.2 else "LÅG"
        return {"voltage": voltage, "status": status, "current": 0.0, "power": 0.0}
