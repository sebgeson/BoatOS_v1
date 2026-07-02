import math


class IMU:
    def __init__(self, address=0x68, alpha=0.10):
        self.alpha = alpha
        self.roll_f = 0.0
        self.pitch_f = 0.0
        self.sensor = None
        self.error = None
        try:
            from mpu6050 import mpu6050
            self.sensor = mpu6050(address)
        except Exception as exc:
            self.error = str(exc)

    def read(self):
        if self.sensor is None:
            return {"roll": self.roll_f, "pitch": self.pitch_f, "imu_ok": False, "imu_error": self.error}

        try:
            accel = self.sensor.get_accel_data()
            gyro = self.sensor.get_gyro_data()
            x, y, z = accel["x"], accel["y"], accel["z"]
            roll = math.degrees(math.atan2(y, z))
            pitch = math.degrees(math.atan2(-x, math.sqrt(y*y + z*z)))
            self.roll_f += self.alpha * (roll - self.roll_f)
            self.pitch_f += self.alpha * (pitch - self.pitch_f)
            return {
                "roll": self.roll_f,
                "pitch": self.pitch_f,
                "raw_accel": accel,
                "raw_gyro": gyro,
                "imu_ok": True,
            }
        except Exception as exc:
            self.error = str(exc)
            return {"roll": self.roll_f, "pitch": self.pitch_f, "imu_ok": False, "imu_error": self.error}
