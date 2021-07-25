import pygame
import os
import random

from Bird import Bird

IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))


class Pipe:
    PIPE_IMG = IMG
    GAP = 200
    VEl = 5

    def __init__(self, x: int) -> None:
        self.x: int = x
        self.height: int = 0

        self.top: int = 0
        self.bottom: int = 0
        self.PIPE_TOP: pygame.image = pygame.transform.flip(self.PIPE_IMG, False, True)
        self.PIPE_BOTTOM: pygame.image = self.PIPE_IMG

        self.passed: bool = False
        self.set_height()

    def set_height(self) -> None:
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self) -> None:
        self.x -= self.VEl

    def draw(self, win: pygame.display) -> None:
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird: Bird) -> bool:
        bird_mask: pygame.mask = bird.get_mask()
        top_mask: pygame.mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask: pygame.mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset: tuple = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset: tuple = (self.x - bird.x, self.bottom - round(bird.y))

        b_point: int = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point: int = bird_mask.overlap(top_mask, top_offset)
        if t_point or b_point:
            return True
        return False
