import math
from themes import current as theme
from widgets.primitives import gradient_vertical, round_rect


def draw(draw, width, height, roll, pitch):
    area_top = 40
    area_bottom = 226
    cx = width // 2
    cy = 132

    horizon_y = cy + int(pitch * 3)
    angle = math.radians(roll)

    length = 720
    dx = math.cos(angle) * length
    dy = math.sin(angle) * length

    x1 = cx - dx
    y1 = horizon_y - dy
    x2 = cx + dx
    y2 = horizon_y + dy

    gradient_vertical(draw, (0, area_top, width, area_bottom), theme.SKY_TOP, theme.SKY_BOTTOM)
    draw.polygon([(0, area_bottom), (width, area_bottom), (x2, y2), (x1, y1)], fill=theme.SEA_BOTTOM)
    draw.polygon([(0, area_bottom), (width, area_bottom), (x2, y2), (x1, y1)], fill=theme.SEA_TOP)
    draw.line((x1, y1, x2, y2), fill=theme.WHITE, width=3)

    # Dekorativ ram runt horisonten
    round_rect(draw, (6, 46, width - 6, area_bottom - 5), radius=12, outline=theme.BORDER, width=1)

    # Rollskala uppe
    for deg in range(-40, 41, 10):
        x = cx + deg * 4
        tick_h = 10 if deg % 20 == 0 else 6
        draw.line((x, 49, x, 49 + tick_h), fill=theme.MUTED, width=1)
        if deg != 0 and deg % 20 == 0:
            draw.text((x - 8, 62), str(abs(deg)), fill=theme.MUTED)

    draw.polygon([(cx, 52), (cx - 8, 42), (cx + 8, 42)], fill=theme.YELLOW)

    # Pitchskala
    for value in range(-20, 21, 10):
        y = cy + value * 3
        draw.line((cx - 28, y, cx + 28, y), fill=theme.WHITE, width=1)
        if value != 0:
            draw.text((cx + 36, y - 7), str(value), fill=theme.WHITE)

    # Båtmarkör
    draw.line((cx - 70, cy, cx - 18, cy), fill=theme.YELLOW, width=5)
    draw.line((cx + 18, cy, cx + 70, cy), fill=theme.YELLOW, width=5)
    draw.polygon([(cx, cy - 16), (cx - 11, cy + 10), (cx + 11, cy + 10)], fill=theme.YELLOW)
    draw.ellipse((cx - 5, cy - 5, cx + 5, cy + 5), outline=theme.WHITE, width=1)
