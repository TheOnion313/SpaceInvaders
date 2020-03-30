import pygame

BARRIER_SIZE = (10, 5)
BLOCK_SIZE = (10, 10)

class Block(object):

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.dead = False

    def show(self):
        if not self.dead:
            self.screen.fill((255, 255, 255), rect=pygame.Rect((self.x, self.y), BLOCK_SIZE))

class Barrier(object):

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.blocks = []
        for i in range(BARRIER_SIZE[0]):
            for j in range(BARRIER_SIZE[1]):
                self.blocks.append(Block(self.x + i * BLOCK_SIZE[0], self.y + j * BLOCK_SIZE[1], screen))

    def show(self):
        for block in self.blocks:
            block.show()