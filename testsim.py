import numpy as np
from keras.models import load_model
import pygame

lasts = 5
model = load_model('my_model.h5')

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
done = False
clock = pygame.time.Clock()

aa = np.loadtxt(f'./data/testdata{1111}.txt', usecols=(1, 2))
aaa = np.diff(aa, axis=0)
aaa = aaa[0:lasts]
checkdata = []
checkdata.append(aaa)

realx = aa[0][0]
realy = aa[0][1]

pr = model.predict(np.array(checkdata))

prx = aa[lasts-1][0] + pr[0][0]
pry = aa[lasts-1][1] + pr[0][1]
print(checkdata)
print((prx, pry))
print(aa[5])

print('\n')
pygame.draw.circle(screen, (0, 200, 255), (int(prx), int(pry)), 4)
for ii in range(90):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for tt in range(lasts - 1):
        aaa[tt] = aaa[tt + 1]

        aaa[lasts - 1] = pr

    checkdata = []
    checkdata.append(aaa)

    pr = model.predict(np.array(checkdata))
    print('\n')

    prx += pr[0][0]
    pry += pr[0][1]
    print((prx,pry))
    print(aa[lasts+1 + ii])


    realx = aa[ii][0]
    realy = aa[ii][1]
    if ii<lasts:
        pygame.draw.circle(screen, (255,160,20), (int(realx), int(realy)), 2)
    else:
        pygame.draw.circle(screen, (183, 0, 255), (int(realx), int(realy)), 2)
    pygame.draw.circle(screen, (0, 200, 255), (int(prx), int(pry)), 4)

    clock.tick(10)
    pygame.display.flip()
