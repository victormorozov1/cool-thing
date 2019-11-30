from constants import *
from geometry import *
import pygame


if __name__ == '__main__':
    rect = Rectangle(Point(PADDING, PADDING), Point(PADDING, SZ - PADDING), Point(SZ - PADDING, SZ - PADDING), Point(SZ - PADDING, PADDING))
    pygame.init()
    win = pygame.display.set_mode((SZ, SZ))
    pygame.draw.polygon(win, POL_COLOR, rect.to_list(), 1)
    for i in range(N):
        print('rec1 = ', rect)
        rect = gen_new_coords(rect)
        pygame.draw.polygon(win, POL_COLOR, rect.to_list(), 1)
        pygame.display.update()
        print('rect2 = ', rect)
        print('\n' * 5)
        run = True
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        pygame.time.wait(10)
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
