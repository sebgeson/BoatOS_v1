from PIL import Image, ImageDraw
import time

from themes import current as theme
from config import BOAT_NAME


def draw_startup(device):
    img = Image.new("RGB", device.size, theme.BG)
    draw = ImageDraw.Draw(img)

    w, h = device.size
    cx = w // 2

    draw.text((cx - 45, 80), "BoatOS", fill=theme.YELLOW)
    draw.text((cx - 70, 115), BOAT_NAME, fill=theme.WHITE)
    draw.text((cx - 95, 155), "MARINE COMPUTER", fill=theme.WHITE)
    draw.rectangle((90, 220, 390, 235), outline=theme.WHITE, width=2)

    for i in range(0, 300, 20):
        draw.rectangle((92, 222, 92 + i, 233), fill=theme.GREEN)
        device.display(img)
        time.sleep(0.05)

    draw.text((cx - 45, 250), "STARTAR...", fill=theme.WHITE)
    device.display(img)
    time.sleep(0.7)
