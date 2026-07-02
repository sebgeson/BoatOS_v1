import time


class SystemSensor:
    def __init__(self):
        self.last_time = time.time()
        self.frames = 0
        self.fps = 0
        self.start_time = time.time()

    def read_cpu_temp(self):
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r", encoding="utf-8") as f:
                return int(f.read()) / 1000
        except Exception:
            return 0.0

    def read(self):
        self.frames += 1
        now = time.time()
        if now - self.last_time >= 1:
            self.fps = self.frames
            self.frames = 0
            self.last_time = now

        return {
            "cpu_temp": self.read_cpu_temp(),
            "fps": self.fps,
            "uptime": int(now - self.start_time)
        }
