import pygame
import math
import random

from simulation import Simulation

pygame.init()
screen = pygame.display.set_mode((1200, 800))
done = False
clock = pygame.time.Clock()
savemode = True

for i in range(100):

    frame = 0
    filename = f'./data/testdata{1200+i}.txt'
    fl = open(filename, 'w')

    sim = Simulation()
    fl.write(f'{i} {sim.gravityf} {sim.air_density}\n')
    for j in range(150):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        sim.update()

        clock.tick(5000)
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (183, 0, 255), (int(sim.x), int(sim.y)), 8)
        pygame.display.flip()

        if savemode and frame % 3 == 0 and frame < 150:
            fl.write(f'{frame} {sim.x} {sim.y}\n')

        frame += 1
    fl.close()
