import random

import math


class Simulation:
    def __init__(self):
        self.x = 300 + random.random() * 600
        self.y = 300 + random.random() * 400
        self.gravityf = random.random() * 0.5
        self.speedx = pow(random.random(), 2) * 40 - 20
        self.speedy = pow(random.random(), 2) * 40 - 20
        self.air_density = pow(0.1, random.random() * 4 + 1)

    def calc_air_res(self):
        speed = math.sqrt(pow(self.speedx, 2) + pow(self.speedy, 2))
        force = pow(speed, 2) * self.air_density
        a = force / speed
        self.speedx /= (1 + a)
        self.speedy /= (1 + a)

    def update(self):
        self.x += self.speedx
        self.y += self.speedy
        self.speedy += self.gravityf
        self.calc_air_res()