import random
import main
import pygame
import ship
import invader
import shot

INVADER_SIZE = ship.ROCKSIZE
INVADER = pygame.transform.scale(pygame.image.load('graphics\invader.png'), INVADER_SIZE)


class Leader(object):

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.dead = False
        self.velx = main.VELX
        self.screen = screen
        self.cooldown = main.INCOOL
        self.flip = False
        self.shots = []

    def update(self, barriers, spaceship):
        self.cooldown -= 1
        if (self.x + invader.INVADER_SIZE[0] + self.velx * self.cooldown >= main.WIDTH - 5 and self.velx > 0) or (
                self.x <= main.ROW_SIZE * (invader.INVADER_SIZE[0] - 25) + 5 and self.velx < 0):
            self.flip = True
            self.velx *= -1
            main.INCOOL *= 0.9
        if self.flip and self.cooldown <= 0:
            self.y += invader.INVADER_SIZE[1] * 0.25
            self.flip = False
            self.cooldown = main.INCOOL
        elif self.cooldown <= 0:
            self.cooldown = main.INCOOL
            self.x += self.velx * main.ORIGINAL_INCOOL

        if random.random() < main.SHOOT_SHOT:
            self.shoot()

        for shot in self.shots:
            if shot.update(barriers, spaceship):
                self.shots.remove(shot)


        self.show()

    def show(self):
        if not self.dead:
            self.screen.blit(INVADER, (self.x, self.y))

    def shoot(self):
        self.shots.append(shot.InvaderShot(self.x + shot.INVADER_SHOT_SIZE[0] / 7, self.y + shot.INVADER_SHOT_SIZE[1], self.screen))
