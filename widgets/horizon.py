import math
from themes import current as theme


def draw(draw, width, height, roll, pitch):
    cx = width // 2
    cy = 135

    horizon_y = cy + int(pitch * 3)
    angle = math.radians(roll)

    length = 700
    dx = math.cos(angle) * length
    dy = math.sin(angle) * length

    x1 = cx - dx
    y1 = horizon_y - dy
    x2 = cx + dx
    y2 = horizon_y + dy

    draw.polygon([(0, 38), (width, 38), (x2, y2), (x1, y1)], fill=theme.SKY)
    draw.polygon([(0, 230), (width, 230), (x2, y2), (x1, y1)], fill=theme.SEA)
    draw.line((x1, y1, x2, y2), fill=theme.WHITE, width=4)

    # Fast båtmarkör
    draw.line((cx - 60, cy, cx - 15, cy), fill=theme.YELLOW, width=5)
    draw.line((cx + 15, cy, cx + 60, cy), fill=theme.YELLOW, width=5)
    draw.polygon(
        [(cx, cy - 15), (cx - 10, cy + 10), (cx + 10, cy + 10)],
        fill=theme.YELLOW
    )

    # Enkel pitchskala
    for value in range(-20, 21, 10):
        y = cy + value * 3
        draw.line((cx - 25, y, cx + 25, y), fill=theme.WHITE, width=1)
        if value != 0:
            draw.text((cx + 32, y - 7), str(value), fill=theme.WHITE)
