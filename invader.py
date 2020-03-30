import random

import pygame

import main
import ship
import shot

INVADER_SIZE = ship.ROCKSIZE

INVADER = pygame.transform.scale(pygame.image.load('graphics\invader.png'), INVADER_SIZE)


class Invader(object):

    def __init__(self, x, y, leader, screen):
        self.x = x
        self.y = y
        self.dead = False
        self.velx = 0
        self.leader = leader
        self.screen = screen
        self.cooldown = main.INCOOL
        self.shots = []

    def show(self):
        if not self.dead:
            self.screen.blit(INVADER, (self.x, self.y))

    def update(self, barriers, spaceship):
        self.cooldown -= 1
        self.velx = self.leader.velx
        y = self.y
        self.y = self.leader.y
        if self.cooldown <= 0 and self.y == y:
            self.cooldown = main.INCOOL
            self.x += self.velx * main.ORIGINAL_INCOOL
        elif self.y != y:
            self.cooldown = main.INCOOL

        if random.random() < main.SHOOT_SHOT:
            self.shoot()

        for shot in self.shots:
            if shot.update(barriers, spaceship):
                self.shots.remove(shot)

        self.show()

    def shoot(self):
        self.shots.append(shot.InvaderShot(self.x + INVADER_SIZE[0] / 7, self.y + INVADER_SIZE[1], self.screen))
