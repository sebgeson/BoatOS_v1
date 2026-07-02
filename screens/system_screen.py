from PIL import Image, ImageDraw
from themes import current as theme
import time


def format_uptime(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def draw_system_screen(device, data):
    img = Image.new("RGB", device.size, theme.BG)
    draw = ImageDraw.Draw(img)

    w, h = device.size
    system = data.get("system", {})
    battery = data.get("battery", {})

    cpu = system.get("cpu_temp", 0.0)
    fps = system.get("fps", 0)
    uptime = system.get("uptime", 0)
    voltage = battery.get("voltage", 0.0)

    draw.rectangle((0, 0, w, 38), fill=theme.HEADER)
    draw.text((10, 10), "BoatOS - SYSTEM", fill=theme.WHITE)
    draw.text((420, 10), time.strftime("%H:%M"), fill=theme.WHITE)

    draw.text((30, 70), f"CPU-temp: {cpu:.1f} C", fill=theme.WHITE)
    draw.text((30, 105), f"FPS:      {fps}", fill=theme.WHITE)
    draw.text((30, 140), f"Batteri:  {voltage:.1f} V", fill=theme.GREEN)
    draw.text((30, 175), f"Uptime:   {format_uptime(uptime)}", fill=theme.WHITE)
    draw.text((30, 210), "IMU:      OK", fill=theme.GREEN)
    draw.text((30, 245), "Display:  OK", fill=theme.GREEN)
    draw.text((30, 280), "Logg:     logs/boatos.log", fill=theme.WHITE)

    return img
