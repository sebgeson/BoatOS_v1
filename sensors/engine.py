class Engine:
    def read(self):
        # Mock tills varvräknare/temp/laddning kopplas.
        return {
            "rpm": 0,
            "temp": 45,
            "charging": False,
            "oil": "OK",
            "hours": 0.0,
            "coolant": "OK",
        }
