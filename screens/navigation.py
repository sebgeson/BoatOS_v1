from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class NavigationScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(20, 80, 200, 62, "GPS", lambda d: "VANTAR", theme.ORANGE))
        self.add(InfoBox(260, 80, 200, 62, "FART", lambda d: "0.0 kn", theme.CYAN))
        self.add(InfoBox(20, 160, 200, 62, "KURS", lambda d: "--- deg", theme.YELLOW))
        self.add(InfoBox(260, 160, 200, 62, "POSITION", lambda d: "INGEN FIX", theme.ORANGE))
        self.add(InfoBox(20, 240, 440, 62, "OPENCPN", lambda d: "EJ ANSLUTEN", theme.MUTED))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        draw.text((20, 50), "NAVIGATION", fill=theme.CYAN)
        self.draw_widgets(draw, data)
        return img
