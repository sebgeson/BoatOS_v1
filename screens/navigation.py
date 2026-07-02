from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class NavigationScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(20, 70, 200, 60, "GPS", lambda d: "VANTAR"))
        self.add(InfoBox(260, 70, 200, 60, "FART", lambda d: "0.0 kn"))
        self.add(InfoBox(20, 155, 200, 60, "KURS", lambda d: "--- deg"))
        self.add(InfoBox(260, 155, 200, 60, "POSITION", lambda d: "INGEN FIX"))
        self.add(InfoBox(20, 240, 440, 60, "OPENCPN", lambda d: "EJ ANSLUTEN"))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size

        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        draw.text((20, 45), "NAVIGATION", fill=theme.YELLOW)
        self.draw_widgets(draw, data)
        return img
