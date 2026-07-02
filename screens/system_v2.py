from PIL import Image, ImageDraw
from themes import current as theme
from ui.core.screen import Screen
from ui.components.infobox import InfoBox
from widgets import statusbar


class SystemV2(Screen):
    def __init__(self):
        super().__init__()

        self.add(InfoBox(20, 65, 200, 60, "CPU", lambda d: f"{d.get('system', {}).get('cpu_temp', 0):.1f} C"))
        self.add(InfoBox(260, 65, 200, 60, "FPS", lambda d: f"{d.get('system', {}).get('fps', 0)}"))
        self.add(InfoBox(20, 145, 200, 60, "BATTERI", lambda d: f"{d.get('battery', {}).get('voltage', 0):.1f} V"))
        self.add(InfoBox(260, 145, 200, 60, "IMU", lambda d: "OK" if d.get("imu_ok") else "FEL"))
        self.add(InfoBox(20, 225, 440, 60, "LOGG", lambda d: "logs/boatos.log"))

    def render(self, device, data):
        img = Image.new("RGB", device.size, theme.BG)
        draw = ImageDraw.Draw(img)

        w, h = device.size
        voltage = data.get("battery", {}).get("voltage", 12.8)
        cpu = data.get("system", {}).get("cpu_temp", 0.0)
        fps = data.get("system", {}).get("fps", 0)

        statusbar.draw(draw, w, voltage, cpu, fps)
        draw.text((20, 45), "SYSTEM", fill=theme.YELLOW)

        self.draw_widgets(draw, data)
        return img