

class Info:
    def update_file(self, path):
        self.path = path
        flag = False
        with open(self.path, "r") as log_file:
            lines = log_file.readlines()
            if len(lines) == 0:
                flag = True
            else:
                self.max_speed = int(lines[-1].split()[0])
                self.min_error = int(100 * int(lines[-1].split()[1]) / int(lines[-1].split()[2]))

        if flag:
            with open(self.path, "w") as log_file:
                log_file.write("0 0 1 0\n")

    def __init__(self, path):
        self.speed = 0
        self.max_speed = 0
        self.error = 0
        self.min_error = 0
        self.total_error = 0
        self.total_click_count = 0
        self.path = path
        self.update_file(self.path)

    def update(self, speed, error_count, click_count):
        self.max_speed = max(self.max_speed, speed)
        self.speed = speed
        self.error = 100 - int(100 * error_count / click_count)

        self.total_click_count += click_count
        self.total_error += error_count
        self.min_error = 100 - int(100 * self.total_error / self.total_click_count)

        lines = []
        with open(self.path, "r") as log_file:
            lines = log_file.readlines()
        with open(self.path, "w") as log_file:
            lines[-1] = ("Speed: {} chars per minute; Errors made: {}; Clicks made: {}; Accuracy: {}%\n".format(speed, error_count,
                                                                                          click_count, 100 - int(100 * error_count / click_count)))
            lines.append("{} {} {}\n".format(self.max_speed, self.total_error, self.total_click_count))
            log_file.writelines(lines)