class Screen:
    def __init__(self):
        self.widgets = []

    def add(self, widget):
        self.widgets.append(widget)
        return widget

    def draw_widgets(self, draw, data):
        for widget in self.widgets:
            if widget.visible:
                widget.draw(draw, data)
