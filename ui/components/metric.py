from ui.core.widget import Widget
from themes import current as theme
from widgets.primitives import round_rect, centered_text


class BigMetric(Widget):
    def __init__(self, x, y, width, height, title, value_func, unit="", color=None):
        super().__init__(x, y, width, height)
        self.title = title
        self.value_func = value_func
        self.unit = unit
        self.color = color or theme.CYAN

    def draw(self, draw, data):
        round_rect(draw, (self.x, self.y, self.x + self.width, self.y + self.height), radius=14, fill=theme.CARD, outline=theme.BORDER, width=1)
        draw.text((self.x + 12, self.y + 10), self.title, fill=theme.MUTED)
        value = self.value_func(data)
        centered_text(draw, (self.x + 8, self.y + 26, self.x + self.width - 8, self.y + self.height - 12), f"{value}{self.unit}", self.color)
