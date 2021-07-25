import pygame
import os

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))


class Base:
    VEl: int = 5
    WIDTH: int = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self, y: int) -> None:
        self.y = y
        self.x1: int = 0
        self.x2: int = self.WIDTH

    def move(self) -> None:
        self.x1 -= self.VEl
        self.x2 -= self.VEl

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win: pygame.display) -> None:
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
