from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class EngineScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(20, 70, 200, 60, "RPM", lambda d: "0"))
        self.add(InfoBox(260, 70, 200, 60, "TEMP", lambda d: "0 C"))
        self.add(InfoBox(20, 155, 200, 60, "LADDNING", lambda d: "VANTAR"))
        self.add(InfoBox(260, 155, 200, 60, "OLJA", lambda d: "OK"))
        self.add(InfoBox(20, 240, 440, 60, "YANMAR 3GM30F", lambda d: "MOTORDATA EJ ANSLUTEN"))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size

        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        draw.text((20, 45), "MOTOR", fill=theme.YELLOW)
        self.draw_widgets(draw, data)
        return img
