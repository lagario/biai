import pygame
import math
import random

from simulation import Simulation

pygame.init()
screen = pygame.display.set_mode((1200, 800))
done = False
clock = pygame.time.Clock()
savemode = True

testnr = 0

for i in range(1):

    frame = 0
    filename = f'./data/testdata{1111}.txt'
    fl = open(filename, 'w')
    testnr += 1
    sim = Simulation()

    for j in range(300):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        sim.update()

        clock.tick(5000)
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (183, 0, 255), (int(sim.x), int(sim.y)), 8)
        pygame.display.flip()

        if savemode and frame % 3 == 0 and frame < 300:
            fl.write(f'{frame} {sim.x} {sim.y}\n')

        frame += 1
    fl.close()