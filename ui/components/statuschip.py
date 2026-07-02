from ui.core.widget import Widget
from themes import current as theme
from widgets.primitives import round_rect


class StatusChip(Widget):
    def __init__(self, x, y, width, label, value_func, color_func=None):
        super().__init__(x, y, width, 28)
        self.label = label
        self.value_func = value_func
        self.color_func = color_func

    def draw(self, draw, data):
        value = self.value_func(data)
        color = self.color_func(data) if self.color_func else theme.GREEN
        round_rect(draw, (self.x, self.y, self.x + self.width, self.y + self.height), radius=8, fill=theme.CARD2, outline=theme.BORDER)
        draw.ellipse((self.x + 8, self.y + 9, self.x + 16, self.y + 17), fill=color)
        draw.text((self.x + 24, self.y + 8), f"{self.label} {value}", fill=theme.WHITE)
