import pygame

import main
import shot

from shot import Shot

COOLDOWN = 200
LIVES = 3
ROCKSIZE = (60, 60)
ROCKET = pygame.transform.scale(pygame.image.load('graphics/rocket.png'), ROCKSIZE)


class Spaceship(object):

    def __init__(self, screen: pygame.display):
        size = screen.get_size()
        self.x = (size[0] - ROCKSIZE[0]) / 2
        self.y = 7 * (size[1] - ROCKSIZE[1]) / 8
        self.velx = 0
        self.cooldown = 0
        self.shots = []
        self.lives = LIVES
        self.screen = screen

    def move(self, vel):
        self.velx = vel

    def show(self):
        self.screen.blit(ROCKET, (self.x, self.y))

    def update(self, barriers, invaders):
        self.x += self.velx
        if self.x + ROCKSIZE[0] > main.WIDTH:
            self.x = main.WIDTH - ROCKSIZE[0]
        elif self.x < 0:
            self.x = 0
        self.cooldown -= 1

        for shot in self.shots:
            if shot.update(barriers, invaders):
                self.shots.remove(shot)
        self.show()

    def shoot(self):
        if self.cooldown <= 0:
            self.shots.append(Shot(self.x - shot.SHOT_SIZE[0] / 8, self.y, self.screen))
            self.cooldown = COOLDOWN
