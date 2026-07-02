from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class ElectricalScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(20, 76, 200, 62, "STARTBATTERI", lambda d: f"{d.get('battery', {}).get('voltage', 0):.1f} V", theme.GREEN))
        self.add(InfoBox(260, 76, 200, 62, "FORBRUKNING", lambda d: "--.- V", theme.MUTED))
        self.add(InfoBox(20, 150, 200, 62, "STROM", lambda d: f"{d.get('battery', {}).get('current', 0):.1f} A", theme.CYAN))
        self.add(InfoBox(260, 150, 200, 62, "EFFEKT", lambda d: f"{d.get('battery', {}).get('power', 0):.0f} W", theme.YELLOW))
        self.add(InfoBox(20, 224, 440, 62, "LADDNING", lambda d: "GENERATOR EJ ANSLUTEN", theme.ORANGE))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)
        statusbar.draw(draw, w, voltage, cpu, fps, data.get("gps", {}).get("gps_fix"), data.get("imu_ok"), len(data.get("alarms", [])))
        draw.text((20, 50), "ELSYSTEM", fill=theme.CYAN)
        self.draw_widgets(draw, data)
        return img
