import keyboard
import pygame

import invader
import leader
from barrier import Barrier
from ship import Spaceship

WIDTH = 800
HEIGHT = 600
BG_COLOR = (0, 0, 0)
SHIP_SPEED = 0.5
ROW_SIZE = 10
COL_SIZE = 5
VELX = 0.05
ORIGINAL_INCOOL = 500
INCOOL = ORIGINAL_INCOOL
SHOOT_SHOT = 0.0001
HEART_SIZE = (40, 40)
HEART = pygame.transform.scale(pygame.image.load('graphics\heart.png'), HEART_SIZE)


def main():
    dimension = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(dimension)
    screen.fill(BG_COLOR)
    pygame.display.flip()
    rocket = Spaceship(screen)
    invaders = []
    y = 10
    for j in range(COL_SIZE):
        row = []
        x = 5
        lead = leader.Leader(0, y, screen)
        for i in range(ROW_SIZE):
            row.append(invader.Invader(x, y, lead, screen))
            x += invader.INVADER_SIZE[0] - 20
        lead.x = x
        row.append(lead)
        y += invader.INVADER_SIZE[1] - 20
        invaders.append(row)

    barriers = []
    barriers.append(Barrier(WIDTH / 20, 5 * HEIGHT / 8, screen))
    barriers.append(Barrier(5 * WIDTH / 20, 5 * HEIGHT / 8, screen))
    barriers.append(Barrier(9 * WIDTH / 20, 5 * HEIGHT / 8, screen))
    barriers.append(Barrier(13 * WIDTH / 20, 5 * HEIGHT / 8, screen))
    barriers.append(Barrier(17 * WIDTH / 20, 5 * HEIGHT / 8, screen))

    running = True
    while running:
        try:
            if keyboard.is_pressed('z'):  # if key 'q' is pressed
                rocket.move(-SHIP_SPEED)
            elif keyboard.is_pressed('x'):
                rocket.move(SHIP_SPEED)
            else:
                rocket.move(0)
            if keyboard.is_pressed(' '):
                rocket.shoot()
        except:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        rocket.update(barriers=barriers, invaders=invaders)
        for rowe in invaders:
            for i in range(ROW_SIZE, 0, -1):
                rowe[i].update(barriers, rocket)

        for barrier in barriers:
            barrier.show()

        for i in range(rocket.lives):
            screen.blit(HEART, (5 + i * HEART_SIZE[0], 5))

        if rocket.lives <= 0:
            break

        pygame.display.update()


if __name__ == '__main__':
    main()
