from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar, horizon


class Dashboard(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(8, 240, 148, 72, "KRANGNING", lambda d: f"{d['roll']:5.1f}°", theme.CYAN))
        self.add(InfoBox(166, 240, 148, 72, "STAMPNING", lambda d: f"{d['pitch']:5.1f}°", theme.YELLOW))
        self.add(InfoBox(324, 240, 148, 72, "BATTERI", lambda d: f"{d.get('battery', {}).get('voltage', 0):.1f} V", theme.GREEN))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size

        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        horizon.draw(draw, w, h, data["roll"], data["pitch"])
        draw.rectangle((0, 228, w, h), fill=theme.PANEL)
        self.draw_widgets(draw, data)
        return img
