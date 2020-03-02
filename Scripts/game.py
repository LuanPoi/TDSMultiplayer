import pygame
from pygame.locals import *
from numpy import random
from Objects.spaceship import *
#from Scripts.Objects.spaceship import SpaceShip
from Utils.Direction import *
#from Scripts.Utils.Direction import Direction

#----- start routine -----
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('NotAsteroid')
player = [None, None, None]
player[0] = SpaceShip(300, 300, Direction.RIGHT)
player[1] = pygame.Surface((player[0]).shape[0])
player[1].fill((255, 255, 255))
player[2] = [0, 0, 0, 0]


apple_pos = (random.randint(0,590), random.randint(0,590))
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

clock = pygame.time.Clock()

#----- main loop -----
while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:

            if event.key == K_w:
                player[2][0] = 1

            if event.key == K_a:
                player[2][1] = 1

            if event.key == K_s:
                player[2][2] = 1

            if event.key == K_d:
                player[2][3] = 1

        if event.type == KEYUP:

            if event.key == K_w:
                player[2][0] = 0

            if event.key == K_a:
                player[2][1] = 0

            if event.key == K_s:
                player[2][2] = 0

            if event.key == K_d:
                player[2][3] = 0

        if event.type == KEYUP:

            if event.key == K_w:
                player[2][0] = 0

            if event.key == K_a:
                player[2][1] = 0

            if event.key == K_s:
                player[2][2] = 0

            if event.key == K_d:
                player[2][3] = 0

    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_a]:
        if player[2] == [1, 0, 0, 0]:
            player[0].direction = Direction.UP
        if player[2] == [0, 1, 0, 0]:
            player[0].direction = Direction.LEFT
        if player[2] == [0, 0, 1, 0]:
            player[0].direction = Direction.DOWN
        if player[2] == [0, 0, 0, 1]:
            player[0].direction = Direction.RIGHT
        if player[2] == [1, 0, 0, 1]:
            player[0].direction = Direction.UP_RIGHT
        if player[2] == [0, 0, 1, 1]:
            player[0].direction = Direction.DOWN_RIGHT
        if player[2] == [0, 1, 1, 0]:
            player[0].direction = Direction.DOWN_LEFT
        if player[2] == [1, 1, 0, 0]:
            player[0].direction = Direction.UP_LEFT

        player[0].updateMove()

    screen.fill((0,0,0))

    screen.blit(apple, apple_pos)

    for pos in player[0].shape[1]:
        screen.blit(player[1], pos)

    pygame.display.update()
