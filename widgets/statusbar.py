import time
from config import BOAT_NAME
from themes import current as theme
from widgets.primitives import round_rect


def _dot(draw, x, y, ok):
    draw.ellipse((x, y, x + 8, y + 8), fill=theme.GREEN if ok else theme.ORANGE)


def draw(draw, width, voltage, cpu_temp, fps, gps_ok=False, imu_ok=False, alarms=0):
    draw.rectangle((0, 0, width, 40), fill=theme.HEADER)
    draw.line((0, 39, width, 39), fill=theme.HEADER_LINE, width=1)

    draw.text((10, 10), "BOATOS", fill=theme.CYAN)
    draw.text((78, 10), BOAT_NAME, fill=theme.WHITE)

    _dot(draw, 178, 16, gps_ok)
    draw.text((190, 13), "GPS", fill=theme.MUTED)
    _dot(draw, 222, 16, imu_ok)
    draw.text((234, 13), "IMU", fill=theme.MUTED)

    round_rect(draw, (272, 7, 323, 31), radius=7, fill=theme.CARD2, outline=theme.BORDER)
    draw.text((281, 13), f"{cpu_temp:.0f}C", fill=theme.MUTED)

    round_rect(draw, (329, 7, 384, 31), radius=7, fill=theme.CARD2, outline=theme.BORDER)
    draw.text((338, 13), f"{voltage:.1f}V", fill=theme.GREEN if voltage >= 12.2 else theme.ORANGE)

    if alarms:
        draw.text((391, 13), f"!{alarms}", fill=theme.ORANGE)

    draw.text((426, 13), time.strftime("%H:%M"), fill=theme.WHITE)
