from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


def pos_text(d):
    gps = d.get("gps", {})
    if not gps.get("gps_fix") or gps.get("lat") is None:
        return "INGEN FIX"
    return f"{gps.get('lat'):.5f}, {gps.get('lon'):.5f}"


class NavigationScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(20, 76, 200, 62, "GPS", lambda d: "FIX" if d.get("gps", {}).get("gps_fix") else "VANTAR", theme.GREEN))
        self.add(InfoBox(260, 76, 200, 62, "FART", lambda d: f"{d.get('gps', {}).get('speed_kn', 0):.1f} kn", theme.CYAN))
        self.add(InfoBox(20, 150, 200, 62, "KURS", lambda d: "--- deg" if d.get('gps', {}).get('course') is None else f"{d.get('gps', {}).get('course'):.0f} deg", theme.YELLOW))
        self.add(InfoBox(260, 150, 200, 62, "SAT", lambda d: str(d.get("gps", {}).get("sats", 0)), theme.MUTED))
        self.add(InfoBox(20, 224, 440, 62, "POSITION", pos_text, theme.ORANGE))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)
        statusbar.draw(draw, w, voltage, cpu, fps, data.get("gps", {}).get("gps_fix"), data.get("imu_ok"), len(data.get("alarms", [])))
        draw.text((20, 50), "NAVIGATION", fill=theme.CYAN)
        self.draw_widgets(draw, data)
        return img
