class GPS:
    def read(self):
        # Mock tills GPS/NMEA kopplas.
        return {
            "gps_fix": False,
            "speed_kn": 0.0,
            "course": None,
            "lat": None,
            "lon": None,
            "sats": 0,
            "hdop": None,
        }
