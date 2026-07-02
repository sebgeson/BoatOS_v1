from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class MenuScreen(Screen):
    def __init__(self):
        super().__init__()

        self.add(InfoBox(20, 70, 200, 60, "1", lambda d: "DASHBOARD"))
        self.add(InfoBox(260, 70, 200, 60, "2", lambda d: "SYSTEM"))
        self.add(InfoBox(20, 155, 200, 60, "3", lambda d: "NAVIGATION"))
        self.add(InfoBox(260, 155, 200, 60, "4", lambda d: "MOTOR"))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)

        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        draw.text((20, 45), "HUVUDMENY", fill=theme.YELLOW)

        self.draw_widgets(draw, data)
        return img