from luma.core.interface.serial import spi
from luma.lcd.device import ili9488
import time
import logging
from pathlib import Path

from config import *
from sensors.imu import IMU
from sensors.battery import Battery
from sensors.system import SystemSensor
from sensors.gps import GPS
from sensors.engine import Engine
from screens.startup import draw_startup
from screens.dashboard import Dashboard
from screens.system_screen import SystemScreen
from screens.menu import MenuScreen
from screens.navigation import NavigationScreen
from screens.engine_screen import EngineScreen
from ui.core.app import App


Path("/home/sgson/BoatOS/logs").mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

serial = spi(port=SPI_PORT, device=SPI_DEVICE, gpio_DC=GPIO_DC, gpio_RST=GPIO_RST, bus_speed_hz=SPI_SPEED)
device = ili9488(serial, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, rotate=DISPLAY_ROTATE)

draw_startup(device)

imu = IMU(address=IMU_ADDRESS, alpha=IMU_SMOOTHING)
battery = Battery()
system = SystemSensor()
gps = GPS()
engine = Engine()

app = App(device)
app.add_screen("dashboard", Dashboard())
app.add_screen("system", SystemScreen())
app.add_screen("menu", MenuScreen())
app.add_screen("navigation", NavigationScreen())
app.add_screen("engine", EngineScreen())

screen_names = ["dashboard", "system", "menu", "navigation", "engine"]

while True:
    try:
        data = {
            **imu.read(),
            "battery": battery.read(),
            "system": system.read(),
            "gps": gps.read(),
            "engine": engine.read()
        }

        screen_index = int(time.time() / SCREEN_SWITCH_SECONDS) % len(screen_names)
        app.set_screen(screen_names[screen_index])

        device.display(app.render(data))
        time.sleep(0.03)

    except KeyboardInterrupt:
        break
    except Exception:
        logging.exception("Fel i huvudloopen")
        time.sleep(1)
