from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class EngineScreen(Screen):
    def __init__(self):
        super().__init__()
        self.add(InfoBox(20, 80, 200, 62, "RPM", lambda d: "0", theme.CYAN))
        self.add(InfoBox(260, 80, 200, 62, "TEMP", lambda d: "0 C", theme.YELLOW))
        self.add(InfoBox(20, 160, 200, 62, "LADDNING", lambda d: "VANTAR", theme.ORANGE))
        self.add(InfoBox(260, 160, 200, 62, "OLJA", lambda d: "OK", theme.GREEN))
        self.add(InfoBox(20, 240, 440, 62, "STATUS", lambda d: "MOTORDATA EJ ANSLUTEN", theme.MUTED))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)
        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        draw.text((20, 50), "MOTOR / YANMAR 3GM30F", fill=theme.CYAN)
        self.draw_widgets(draw, data)
        return img
