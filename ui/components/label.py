from ui.core.widget import Widget
from themes import current as theme


class Label(Widget):
    def __init__(self, x, y, text="", color=None):
        super().__init__(x, y)
        self.text = text
        self.color = color or theme.WHITE

    def draw(self, draw, data):
        draw.text((self.x, self.y), self.text, fill=self.color)