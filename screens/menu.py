from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class MenuScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(20, 76, 200, 62, "01", lambda d: "DASHBOARD", theme.CYAN))
        self.add(InfoBox(260, 76, 200, 62, "02", lambda d: "NAVIGATION", theme.GREEN))
        self.add(InfoBox(20, 150, 200, 62, "03", lambda d: "MOTOR", theme.YELLOW))
        self.add(InfoBox(260, 150, 200, 62, "04", lambda d: "ELSYSTEM", theme.ORANGE))
        self.add(InfoBox(20, 224, 440, 62, "05", lambda d: "SYSTEM / LARM / DIAGNOSTIK", theme.MUTED))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)
        statusbar.draw(draw, w, voltage, cpu, fps, data.get("gps", {}).get("gps_fix"), data.get("imu_ok"), len(data.get("alarms", [])))
        draw.text((20, 50), "HUVUDMENY", fill=theme.CYAN)
        self.draw_widgets(draw, data)
        return img
