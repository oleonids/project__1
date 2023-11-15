import tkinter
import tkinter as tk
import text_widget
import key_detection
import info_widget
import info
import file_exp

class Window():
    def __init__(self, start_width, start_height):
        self.root = tk.Tk()
        self.root.title("keyboard trainer")
        self.width = start_width
        self.height = start_height
        self.root.minsize(start_width, start_height)
        self.root.geometry("{0}x{1}+{2}+{3}".format(self.width, self.height, 1000, 1000))
        self.canvas = tk.Canvas(self.root, background="#ffd3b5")
        self.canvas.place(x = 0, y = 0)
        self.rel_width = 1.1
        self.log_file = file_exp.FileExp(self.canvas, "sys_log.txt", "choose log file", 1)
        self.text_file = file_exp.FileExp(self.canvas, "sys_text.txt", "choose text file", 2)

        self.text = text_widget.TextWidget(self.canvas, [self.width // 2, self.height // 10],
                                           [int(self.width / self.rel_width), self.height // 30], self.text_file.path)

        self.key_detector = key_detection.KeyDetect(self.root, self.text.text)
        self.speed = info_widget.SpeedWidget(self.canvas, [self.width // 2, self.height // 3],
                                              [int(self.width / self.rel_width), self.height // 20], "SPEED, cpm")
        self.best_attempt = info_widget.SpeedWidget(self.canvas, [self.width // 2, self.height // 2],
                                              [int(self.width / self.rel_width), self.height // 20], "best speed")
        self.error = info_widget.SpeedWidget(self.canvas, [self.width // 2, self.height // 3],
                                             [int(self.width / self.rel_width), self.height // 20], "accuracy, %")
        self.min_error = info_widget.SpeedWidget(self.canvas, [self.width // 2, self.height // 2],
                                                    [int(self.width / self.rel_width), self.height // 20], "average accuracy, %")
        self.info = info.Info(self.log_file.path)

    def update(self):
        if self.height != self.root.winfo_height() or self.width != self.root.winfo_width():
            self.height = self.root.winfo_height()
            self.width = self.root.winfo_width()
        self.canvas.configure(width=self.width, height=self.height)
        if self.key_detector.change:
            self.text.new_text(self.text_file.path)
            self.info.update(self.key_detector.speed, self.key_detector.errors, self.key_detector.click_count)
            self.key_detector.update_text(self.text.text)
        self.text.update([self.width // 2, self.height // 10],
                         [int(self.width / self.rel_width), self.height // 30], self.key_detector.color)
        self.speed.update([self.width // 2, self.height // 2], [int(self.width / self.rel_width), self.height // 7],
                          self.info.speed)
        self.best_attempt.update([self.width // 2, (self.height * 5) // 8], [int(self.width / self.rel_width), self.height // 7],
                          self.info.max_speed)
        self.error.update([self.width // 2, (self.height * 3) // 4], [int(self.width / self.rel_width), self.height // 7],
                          self.info.error)
        self.min_error.update([self.width // 2, (self.height * 7) // 8],
                                 [int(self.width / self.rel_width), self.height // 7],
                                 self.info.min_error)
        self.log_file.update([self.width // 10, self.height // 20], [self.width // 10, self.height // 20])
        self.text_file.update([(9 * self.width) // 10, self.height // 20], [self.width // 10, self.height // 20])
        self.canvas.update()
        self.canvas.delete("all")
