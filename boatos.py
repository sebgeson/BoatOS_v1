from luma.core.interface.serial import spi
from luma.lcd.device import ili9488
import time
import logging
from pathlib import Path

from config import *
from sensors.imu import IMU
from sensors.battery import Battery
from sensors.system import SystemSensor
from screens.startup import draw_startup
from screens.dashboard_v2 import DashboardV2
from screens.system_v2 import SystemV2
from ui.core.app import App


LOG_DIR = Path("/home/sgson/BoatOS/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_DIR / "boatos.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

serial = spi(
    port=SPI_PORT,
    device=SPI_DEVICE,
    gpio_DC=GPIO_DC,
    gpio_RST=GPIO_RST,
    bus_speed_hz=SPI_SPEED
)

device = ili9488(
    serial,
    width=DISPLAY_WIDTH,
    height=DISPLAY_HEIGHT,
    rotate=DISPLAY_ROTATE
)

draw_startup(device)

imu = IMU(address=IMU_ADDRESS, alpha=IMU_SMOOTHING)
battery = Battery()
system = SystemSensor()

app = App(device)
app.add_screen("dashboard", DashboardV2())
app.add_screen("system", SystemV2())

while True:
    try:
        imu_data = imu.read()
        battery_data = battery.read()
        system_data = system.read()

        data = {
            **imu_data,
            "battery": battery_data,
            "system": system_data
        }

        if int(time.time() / SCREEN_SWITCH_SECONDS) % 2 == 0:
            app.set_screen("dashboard")
        else:
            app.set_screen("system")

        img = app.render(data)

        if img:
            device.display(img)

        time.sleep(0.03)

    except KeyboardInterrupt:
        break

    except Exception:
        logging.exception("Fel i huvudloopen")
        time.sleep(1)