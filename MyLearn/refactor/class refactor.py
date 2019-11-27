import pygame as py
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:

    def __init__(self, x_or_pair, y=None):
        if y is None:
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        else:
            self.x = x_or_pair
            self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        if isinstance(k, Vec2d):
            return self.x * k.x + self.y * k.y
        return Vec2d(self.x * k, self.y * k)

    def __getitem__(self, item):
        return self.int_pair()[item]

    def len(self):
        return math.sqrt(self.x ^ 2 + self.y ^ 2)

    def vec(self, other):
        return other - self

    def int_pair(self):
        return int(self.x), int(self.y)


class Polyline:

    def __init__(self):
        if not None:
            self.points = []
            self.speeds = []

    def add_point(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] += self.speeds[p]
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = Vec2d(- self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = Vec2d(self.speeds[p][0], -self.speeds[p][1])

    def draw_points(self, points, width=3, color=(255, 255, 255)):
        for point in points:
            py.draw.circle(gameDisplay, color, point.int_pair(), width)


class Knot(Polyline):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def add_point(self, point, speed):
        super().add_point(point, speed)
        self.get_knot()

    def set_points(self):
        super().set_points()
        self.get_knot()

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg]*alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)

    def get_points(self, base_points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
            res.extend(self.get_points(ptn))
        return res

    def draw_points(self, points, width=3, color=(255, 255, 255)):
        for p_n in range(-1, len(points) - 1):
            py.draw.line(gameDisplay, color, points[p_n].int_pair(), points[p_n + 1].int_pair(), width)


def draw_help():
    gameDisplay.fill((50, 50, 50))
    font1 = py.font.SysFont("courier", 24)
    font2 = py.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])
    py.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
                      (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    py.init()
    gameDisplay = py.display.set_mode(SCREEN_DIM)
    py.display.set_caption("MyScreenSaver")
    steps = 35
    working = True
    polyline = Polyline()
    knot = Knot(steps)
    show_help = False
    pause = True
    hue = 0
    coef_speed = 1
    color = py.Color(0)
    while working:
        for event in py.event.get():
            if event.type == py.QUIT:
                working = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    working = False
                if event.key == py.K_r:
                    polyline = Polyline()
                    knot = Knot(steps)
                if event.key == py.K_p:
                    pause = not pause
                if event.key == py.K_s:
                    steps += 1
                if event.key == py.K_F1:
                    show_help = not show_help
                if event.key == py.K_m:
                    steps -= 1 if steps > 1 else 0
                if event.key == py.K_z:
                    coef_speed += 0.5
                    print(coef_speed)
                if event.key == py.K_x:
                    coef_speed -= 0.5
                    print(coef_speed)

            if event.type == py.MOUSEBUTTONDOWN:
                polyline.add_point(Vec2d(event.pos[0], event.pos[1]), Vec2d(random.random() * coef_speed,
                                                                            random.random() * coef_speed))
                knot.add_point(Vec2d(event.pos[0], event.pos[1]), Vec2d(random.random() * 2, random.random() * 2))
        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        polyline.draw_points(polyline.points)
        knot.draw_points(knot.get_knot(), 3, color)
        if not pause:
            polyline.set_points()
            knot.set_points()
        if show_help:
            draw_help()
        py.display.flip()
    py.display.quit()
    py.quit()
    exit(0)
