import pygame
import barrier
import invader
import main
import ship

SHOT_SIZE = (80, 80)
SHOT = pygame.transform.scale(pygame.image.load('graphics/Bullet.png'), SHOT_SIZE)
BULLETVEL = -0.9


class Shot(object):

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.vely = BULLETVEL
        self.screen = screen

    def show(self):
        self.screen.blit(SHOT, (self.x, self.y))

    def update(self, barriers, invaders):
        self.y += self.vely
        self.show()
        dead = False
        if self.y < 0:
            dead = True
        for barrier in barriers:
            for block in barrier.blocks:
                if self.collides_block(block) and not block.dead and not dead:
                    dead = True
                    block.dead = True
        for row in invaders:
            for invade in row:
                if not dead and not invade.dead and self.collides_invader(invade):
                    dead = True
                    invade.dead = True
        return dead

    def collides_block(self, block):
        x = self.x + 20
        return block.x <= self.x + 40 <= block.x + barrier.BLOCK_SIZE[0] and block.y <= self.y <= block.y + \
               barrier.BLOCK_SIZE[1]

    def collides_invader(self, invade):
        x = self.x + SHOT_SIZE[0] / 2
        return invade.x <= x <= invade.x + invader.INVADER_SIZE[0] and invade.y <= self.y <= invade.y + \
               invader.INVADER_SIZE[1]

INVADER_SHOT_SIZE = (40, 40)
INVADER_SHOT = pygame.transform.scale(pygame.image.load('graphics/InvaderBullet.png'), INVADER_SHOT_SIZE)
INVADER_BULLETVEL = 0.3


class InvaderShot(object):

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.vely = INVADER_BULLETVEL
        self.screen = screen

    def show(self):
        self.screen.blit(INVADER_SHOT, (self.x, self.y))

    def update(self, barriers, spaceship):
        self.y += self.vely
        self.show()
        dead = False
        if self.y + INVADER_SHOT_SIZE[1] > main.HEIGHT:
            dead = True
        for barrier in barriers:
            for block in barrier.blocks:
                if self.collides_block(block) and not block.dead and not dead:
                    dead = True
                    block.dead = True
        if (spaceship.x <= self.x + INVADER_SHOT_SIZE[0] / 2 <= spaceship.x + ship.ROCKSIZE[0]) and \
                (spaceship.y <= self.y + INVADER_SHOT_SIZE[1] <= spaceship.y + ship.ROCKSIZE[1])and (not dead):
            dead = True
            spaceship.lives -= 1
        return dead

    def collides_block(self, block):
        x = self.x + 20
        return block.x <= x <= block.x + barrier.BLOCK_SIZE[0] and block.y <= self.y + INVADER_SHOT_SIZE[1] <= block.y + \
               barrier.BLOCK_SIZE[1]
