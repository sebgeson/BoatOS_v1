class AlarmEngine:
    def evaluate(self, data):
        alarms = []
        battery = data.get("battery", {})
        engine = data.get("engine", {})
        gps = data.get("gps", {})
        system = data.get("system", {})

        voltage = battery.get("voltage", 0)
        if voltage and voltage < 12.0:
            alarms.append({"level": "WARN", "text": "Låg batterispänning"})
        if voltage and voltage < 11.6:
            alarms.append({"level": "CRIT", "text": "Kritiskt batteri"})

        temp = engine.get("temp", 0)
        if temp and temp > 85:
            alarms.append({"level": "WARN", "text": "Motortemperatur hög"})
        if temp and temp > 95:
            alarms.append({"level": "CRIT", "text": "Motor överhettad"})

        if not gps.get("gps_fix"):
            alarms.append({"level": "INFO", "text": "GPS väntar på fix"})

        cpu = system.get("cpu_temp", 0)
        if cpu and cpu > 75:
            alarms.append({"level": "WARN", "text": "CPU varm"})

        return alarms[:4]
