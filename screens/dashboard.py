from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from ui.components.metric import BigMetric
from widgets import statusbar, horizon


class Dashboard(Screen):
    def __init__(self):
        super().__init__()
        self.add(BigMetric(8, 228, 112, 84, "FART", lambda d: f"{d.get('gps', {}).get('speed_kn', 0):.1f}", " kn", theme.CYAN))
        self.add(BigMetric(128, 228, 112, 84, "KURS", lambda d: "---" if d.get('gps', {}).get('course') is None else f"{d.get('gps', {}).get('course'):.0f}", "°", theme.YELLOW))
        self.add(InfoBox(248, 228, 106, 84, "MOTOR", lambda d: f"{d.get('engine', {}).get('temp', 0):.0f} C", theme.ORANGE))
        self.add(InfoBox(362, 228, 110, 84, "BATTERI", lambda d: f"{d.get('battery', {}).get('voltage', 0):.1f} V", theme.GREEN))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)
        alarms = data.get("alarms", [])

        statusbar.draw(draw, w, voltage, cpu, fps, data.get("gps", {}).get("gps_fix"), data.get("imu_ok"), len(alarms))
        horizon.draw(draw, w, h, data.get("roll", 0.0), data.get("pitch", 0.0))
        draw.rectangle((0, 220, w, h), fill=theme.PANEL)
        self.draw_widgets(draw, data)
        return img
