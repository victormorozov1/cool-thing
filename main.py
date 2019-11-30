from game import Game
from math import sqrt
import pygame

K = 0.8
N = 100
POL_COLOR = (123, 234, 243)
SZ = 500
PADDING = 10


def abs(p):
    if p < 0:
        return p * -1
    return p


def diff(start, end):
    a, b = start.x - end.x, start.y - end.y
    return sqrt(a ** 2 + b ** 2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_list(self):
        return [self.x, self.y]

    def __str__(self):
        return '(x {} y {}'.format(self.x, self.y)

class Rectangle:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p3 = p3
        self.p2 = p2
        self.p4 = p4
        self.ln = abs(p1.x - self.p3.x)

    def to_list(self):
        return [self.p1.to_list(), self.p2.to_list(), self.p3.to_list(), self.p4.to_list()]

    def __str__(self):
        return '({}) ({}) ({}) ({})'.format(str(self.p1), str(self.p2), str(self.p3), str(self.p4))


def coord_on_line(start, end, ln):
    k = ln / diff(start, end)
    p = start
    p.x += (end.x - start.x) * k
    p.y += (end.y - start.y) * k
    return p


def gen_new_coords(oldrect):
    a1 = oldrect.ln
    a2 = a1 * K
    print('len1={} len2={}'.format(a1, a2))
    D = 4 * a1 ** 2 - 8 * (a1 ** 2 - a2 ** 2)
    x = (2 * a1 + sqrt(D)) / 4
    return Rectangle(coord_on_line(oldrect.p1, oldrect.p2, x), coord_on_line(oldrect.p2, oldrect.p3, x),
                     coord_on_line(oldrect.p3, oldrect.p4, x), coord_on_line(oldrect.p4, oldrect.p1, x))


if __name__ == '__main__':
    rect = Rectangle(Point(PADDING, PADDING), Point(PADDING, SZ - PADDING), Point(SZ - PADDING, SZ - PADDING), Point(SZ - PADDING, PADDING))
    pygame.init()
    win = pygame.display.set_mode((SZ, SZ))
    for i in range(N):
        print('rec1 = ', rect)
        pygame.draw.polygon(win, POL_COLOR, rect.to_list(), 1)
        rect = gen_new_coords(rect)
        pygame.display.update()
        print('rect2 = ', rect)
        run = True
        while run:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                if i.type == pygame.KEYDOWN:
                    run = False
                    break
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
