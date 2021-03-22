import math
from tkinter import Tk, Canvas, Frame, BOTH
import boundingBox


class boundingBoxFrame(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.master.title("Bounding Box")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self, width=window_width, height=window_height)

        # canvas.create_rectangle(0, 0, window_width, window_height)
        canvas.create_rectangle(max_min_x[0], max_min_y[0], max_min_x[1], max_min_y[1], fill='lightblue')
        for i in range(number_of_points):
            self.create_point(canvas, points_x[i], points_y[i])

        canvas.pack(fill=BOTH, expand=1)

    def create_point(self, canvas: Canvas, x, y):
        max_dist = math.dist((x_range, y_range), (0, 0))
        point_dist = math.dist((x, y), (0, 0))
        normal_dist = max(min((point_dist / max_dist), 1), 0)

        # r = lambda: random.randint(0, 255)
        # fill = '#%02X%02X%02X' % (r(), r(), r())

        s = int(normal_dist * 255)
        s = hex(s).upper().lstrip('0X')
        if len(s) == 1:
            s = "0" + s
        fill = "#{}{}7F".format(s, s)
        # print(scale)
        thickness = min(scale, 10)
        canvas.create_oval(x - thickness, y - thickness, x + thickness, y + thickness, fill=fill)


def main():
    root = Tk()
    boundingBoxFrame()
    root.mainloop()


def get_input():
    for i in range(number_of_points):
        point = input('Enter point {} coordination: X Y\n'.format(i)).split()
        point_x = float(point[0])
        point_y = float(point[1])
        points_x.append(point_x)
        points_y.append(point_y)


def log_points():
    log_file = open('points.txt', 'w')
    for i in range(number_of_points):
        log_file.write("{} {}\n".format(points_x[i], points_y[i]))
    log_file.close()


if __name__ == '__main__':
    global number_of_points
    number_of_points = int(input('Enter number of points:\n'))

    global points_x
    global points_y
    points_x = []
    points_y = []

    get_input()
    # points_x = boundingBox.number_generator(-10, 10, number_of_points)
    # points_y = boundingBox.number_generator(-10, 10, number_of_points)

    global max_min_x
    global max_min_y
    max_min_x = boundingBox.find_max_and_min(points_x)
    max_min_y = boundingBox.find_max_and_min(points_y)
    print('Maximum X:{}, Minimum X:{}'.format(max_min_x[0], max_min_x[1]))
    print('Maximum Y:{}, Minimum Y:{}'.format(max_min_y[0], max_min_y[1]))

    global scale
    global window_width
    global window_height
    window_width = 1920
    window_height = 1000
    padding = 30

    global x_range
    global y_range
    x_range = max_min_x[0] - max_min_x[1]
    y_range = max_min_y[0] - max_min_y[1]

    if (window_width / window_height) < (x_range / y_range) or y_range == 0:
        scale = (window_width - padding) / x_range
        # print("Scale by X:{}".format(scale))
    else:
        scale = (window_height - padding) / y_range
        # print("Scale by Y:{}".format(scale))

    y_range *= scale
    x_range *= scale

    points_x = [scale * (x - max_min_x[1]) + (window_width - x_range) / 2 for x in points_x]
    points_y = [scale * (y - max_min_y[1]) + padding / 2 for y in points_y]
    points_y = [-y + window_height for y in points_y]

    max_min_x = (x_range + ((window_width - x_range) // 2), ((window_width - x_range) // 2))
    max_min_y = (-(y_range + padding / 2) + window_height, -(padding / 2) + window_height)

    # log_points()

    main()
