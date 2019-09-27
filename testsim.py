import numpy as np
from keras.models import load_model
import pygame
import math
lasts = 5
model = load_model('my_model_250e.h5')

pygame.init()
screen = pygame.display.set_mode((1400, 900))
done = False
clock = pygame.time.Clock()

aa = np.loadtxt(f'./data/testdata{1250}.txt', usecols=(1, 2))
aaa = np.diff(aa, axis=0)
aaa = aaa[0:lasts+1]
aaa[0][0] = aa[0][0]
aaa[0][1] = math.sqrt(aa[0][1])*10
checkdata = []
checkdata.append(aaa)

realx = aa[1][0]
realy = aa[1][1]

pr = model.predict(np.array(checkdata))

prx = aa[lasts+1][0] + pr[0][0]
pry = aa[lasts+1][1] + pr[0][1]
print(checkdata)
print((prx, pry))
print(aa[5])

print('\n')
ox=00
oy=100
pygame.draw.circle(screen, (0, 200, 255), (int(prx/2)+ox, int(pry/2)+oy), 3)
for ii in range(40):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for tt in range(lasts - 1):
        aaa[tt+1] = aaa[tt + 2]

    aaa[lasts] = pr

    checkdata = []
    checkdata.append(aaa)

    pr = model.predict(np.array(checkdata))
    print('\n')

    prx += pr[0][0]
    pry += pr[0][1]
    # print((prx,pry))
    # print(aa[lasts+1 + ii])


    realx = aa[ii+1][0]
    realy = aa[ii+1][1]
    if ii<lasts+1:
        pygame.draw.circle(screen, (255,160,20), (int(realx/2)+ox, int(realy/2)+oy), 2)
    else:
        pygame.draw.circle(screen, (183, 0, 255), (int(realx/2)+ox, int(realy/2)+oy), 2)
    pygame.draw.circle(screen, (0, 200, 255), (int(prx/2)+ox, int(pry/2)+oy), 3)

    clock.tick(8)
    pygame.display.flip()
clock.tick(0.5)
