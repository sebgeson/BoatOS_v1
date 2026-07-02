from mpu6050 import mpu6050
import math


class IMU:
    def __init__(self, address=0x68, alpha=0.10):
        self.sensor = mpu6050(address)
        self.roll_f = 0.0
        self.pitch_f = 0.0
        self.alpha = alpha

    def read(self):
        accel = self.sensor.get_accel_data()
        gyro = self.sensor.get_gyro_data()

        x = accel["x"]
        y = accel["y"]
        z = accel["z"]

        roll = math.degrees(math.atan2(y, z))
        pitch = math.degrees(math.atan2(-x, math.sqrt(y * y + z * z)))

        self.roll_f += self.alpha * (roll - self.roll_f)
        self.pitch_f += self.alpha * (pitch - self.pitch_f)

        return {
            "roll": self.roll_f,
            "pitch": self.pitch_f,
            "raw_roll": roll,
            "raw_pitch": pitch,
            "raw_accel": accel,
            "raw_gyro": gyro,
            "imu_ok": True
        }
