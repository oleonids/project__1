import tkinter.filedialog as fd
import tkinter as tk


class FileExp:
    def update_path(self):
        path = fd.askopenfilename(initialdir="/",
                                       title=self.text, filetypes=(("Text files", "*.txt*"), ("All Files", "*.*")))
        try:
            file = open(path, "r")
            file.close()
            self.path = path
            with open(self.sys, "w") as file:
                file.write(self.path)
        except:
            pass

    def __init__(self, canvas: tk.Canvas, sys: str, text:str, num: int):
        self.num = num
        self.coords = []
        self.size = []
        self.text = text
        self.canvas = canvas
        self.path = ""
        self.sys = sys
        with open(self.sys, "r") as file:
            txt = file.readline()
            if txt != "":
                self.path = txt

                try:
                    open(self.path, "r")
                except:
                    self.update_path()
            else:
                self.update_path()

    def update(self, coords, size):
        self.coords = [coords[0] - size[0] // 2, coords[1] - size[1] // 2, coords[0] + size[0] // 2,
                       coords[1] + size[1] // 2]
        self.size = size
        self.canvas.create_rectangle(self.coords[0], self.coords[1], self.coords[2], self.coords[3], fill="#a8e6c3", tags="button"+str(self.num))
        self.canvas.create_text((self.coords[0] + self.coords[2]) // 2,
                                (self.coords[1] + self.coords[3]) // 2, text=self.text, font=("Verdana", int(self.size[0] / (len(self.text) * 0.75))),
                                tags="button"+str(self.num))
        def click(*args):
            self.update_path()
        self.canvas.tag_bind("button{}".format(self.num), "<Button-1>", click)

