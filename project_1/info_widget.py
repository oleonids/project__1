import text_widget


class SpeedWidget():
    def __init__(self, canvas, coords, size, text):
        self.coords = coords
        self.size = size
        self.canvas = canvas
        self.rel_size = 1.3
        self.text = text
        self.mark = text_widget.TextUnit(self.text, self.canvas, ("Kenia", int(self.size[0] // (self.rel_size * (len(self.text) + 3)))))
        self.speed = text_widget.TextUnit("", self.canvas, ("Kenia", self.canvas, int(self.size[0] / ((len(text) + 3) * self.rel_size))))

    def update(self, coords, size, speed):
        self.coords = coords
        self.size = size
        self.mark.update([self.coords[0] - self.size[0] // 2, self.coords[1] - self.size[1] // 2],
                         [self.size[0] // 2, self.size[1] // 2], ("Kenia",
                                                                  min(int(self.size[0] / ((len(self.text) + 3) * self.rel_size)),
                                                                      int(self.size[1] / 3))), "#faa")
        self.speed.letter = speed
        self.speed.update([self.coords[0] + (self.size[0] * 2 // 3) - self.size[0] // 2, self.coords[1] - self.size[1] // 2],
                         [self.size[0] // 3, self.size[1] // 2], ("Kenia",
                                                                  min(int(self.size[0] / ((len(self.text) + 3) * self.rel_size)),
                                                                      int(self.size[1] / 3))), "#faa")
