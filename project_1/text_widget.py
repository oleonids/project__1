

class TextUnit():
    def __init__(self, letter: str, canvas, font: tuple):
        self.coords = []
        self.letter = letter
        self.canvas = canvas
        self.font = font

    def update(self, coords, size, font: tuple, color: str):
        self.coords = coords + [coords[0] + size[0], coords[1] + size[1]]
        self.canvas.create_rectangle(self.coords, fill=color, outline="#000")
        self.canvas.create_text((self.coords[0] + self.coords[2]) // 2,
                                (self.coords[1] + self.coords[3]) // 2, text=self.letter, font=font)


class TextWidget():
    def __init__(self, canvas, coords: list, size: list, path: str):
        self.text = ""
        self.coodrs = coords
        self.size = size
        self.canvas = canvas
        self.line = 0
        self.path = path
        with open(self.path, "r") as text_file:
            self.text_array = list(map(lambda x: x.replace("\n", ""), text_file.readlines()))
        self.text = self.text_array[0]
        self.letters = [TextUnit(self.text[i], self.canvas,
                                 ("Verdana", size[0] // (len(self.text) * 1.5))) for i in range(len(self.text))]

    def new_text(self, path: str):
        if self.line >= len(self.text_array) - 1:
            self.line = 0
        else:
            self.line += 1
        self.text = self.text_array[self.line]
        if self.path != path:
            self.path = path
            with open(self.path, "r") as text_file:
                self.text_array = list(map(lambda x: x.replace("\n", ""), text_file.readlines()))
            self.text = self.text_array[0]
            self.line = 0
        self.letters = [TextUnit(self.text[i], self.canvas,
                                 ("Verdana", self.size[0] // (len(self.text) * 1.5))) for i in range(len(self.text))]

    def update(self, coords: list, size: list, color: str):
        font_spacing = 1.8
        size_spacing = 1.3
        for i in range(len(self.text)):
            self.letters[i].update([coords[0] - size[0] // 2 + int(size[0] / len(self.text) * i), coords[1]],
                                   [int(size[0] / (len(self.text) * size_spacing)),
                                    int((size_spacing * size[0]) / (len(self.text) * size_spacing))],
                                   ("Verdana", int(size[0] / (len(self.text) * font_spacing))), color[i])
