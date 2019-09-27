import numpy as np
from keras import Sequential, optimizers
from keras.layers import Dense, Flatten
import math

inputs = []
outputs = []
lasts = 5


for tnr in range(800):

    d = np.loadtxt(f'./data/testdata{tnr}.txt', usecols=(1, 2))
    dd = np.diff(d, axis=0)
    grav = d[0][0]
    aird = d[0][1]
    for i in range(len(dd) - lasts - 2):
        tmp = dd[i:i + lasts+1]
        tmp[0][0] = grav
        tmp[0][1] = math.sqrt(aird)*10#math.log(aird)+5  #
        inputs.append(tmp)
        outputs.append(dd[i+1 + lasts])


def baseline_model():
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(37, activation='linear', input_shape=(12,)))
    #  model.add(Dense(3, activation='linear'))
    #  model.add(Dense(5, activation='linear'))
    model.add(Dense(2, activation='linear'))
    ada = optimizers.Adadelta()
    model.compile(optimizer=ada, loss="mean_squared_error", metrics=['accuracy'])
    return model


i = np.array(inputs)
o = np.array(outputs)

model = baseline_model()

filename = f'./testresults.txt'
fl = open(filename, 'w')


def check():
    diff1x = 0
    diff1y = 0
    diff3x = 0
    diff3y = 0
    diff10x = 0
    diff10y = 0
    diff30x = 0
    diff30y = 0
    bestid=0
    worstid=0
    bestval=1000000
    worstval=0
    for i in range(100):
        aa = np.loadtxt(f'./data/testdata{1200+i}.txt', usecols=(1, 2))
        aaa = np.diff(aa, axis=0)
        aaa = aaa[0:lasts + 1]
        aaa[0][0] = aa[0][0]
        aaa[0][1] = math.sqrt(aa[0][1])*10
        checkdata = []
        checkdata.append(aaa)

        pr = model.predict(np.array(checkdata))
        realx = aa[lasts][0]
        realy = aa[lasts][1]
        prx = aa[lasts][0] + pr[0][0]
        pry = aa[lasts][1] + pr[0][1]
        for j in range(30):
            realx = aa[lasts + j +1][0]
            realy = aa[lasts + j +1][1]
            errx = realx-prx
            erry = realy-pry
            if j==0:
                diff1x += errx*errx
                diff1y += erry*erry
            if j==2:
                diff3x += errx * errx
                diff3y += erry * erry
            if j == 9:
                tmpx = errx * errx
                tmpy = erry * erry
                tsum = tmpx + tmpy
                diff10x += tmpx
                diff10y += tmpy
                if tsum < bestval:
                    bestval = tsum
                    bestid = 1200+i
                if tsum > worstval:
                    worstval = tsum
                    worstid = 1200+i
            if j == 29:
                diff30x += errx * errx
                diff30y += erry * erry
            for tt in range(lasts - 1):
                aaa[tt + 1] = aaa[tt + 2]

            aaa[lasts] = pr
            checkdataa = []
            checkdataa.append(aaa)
            pr = model.predict(np.array(checkdata))
            prx += pr[0][0]
            pry += pr[0][1]
    diff1x = math.sqrt(diff1x/100)
    diff1y = math.sqrt(diff1y/100)
    diff3x = math.sqrt(diff3x/100)
    diff3y = math.sqrt(diff3y/100)
    diff10x = math.sqrt(diff10x/100)
    diff10y = math.sqrt(diff10y/100)
    diff30x = math.sqrt(diff30x/100)
    diff30y = math.sqrt(diff30y/100)
    fl.write(f'd1x: {diff1x},d1y: {diff1y}\n')
    fl.write(f'd3x: {diff3x},d3y: {diff3y}\n')
    fl.write(f'd10x: {diff10x},d10y: {diff10y}\n')
    fl.write(f'd30x: {diff30x},d30y: {diff30y}\n')

    fl.write(f'worst file: {worstid}({worstval}) best: {bestid}({bestval}) ')
    score=(diff1x*100+diff1y*100+diff3x*30+diff3y*30+diff10x*10+diff10y*10+diff30x+diff30y)/282
    fl.write(f' total:{score}')

model.fit(i, o, epochs=50, shuffle=True)
fl.write(f'epochs: 50 ')
check()
model.save('my_model_50e.h5')

model.fit(i, o, epochs=50, shuffle=True)
fl.write(f'\n\nepochs: 100 ')
check()
model.save('my_model_100e.h5')

model.fit(i, o, epochs=50, shuffle=True)
fl.write(f'\n\nepochs: 150 ')
check()
model.save('my_model_150e.h5')

model.fit(i, o, epochs=50, shuffle=True)
fl.write(f'\n\nepochs: 200 ')
check()
model.save('my_model_200e.h5')

model.fit(i, o, epochs=50, shuffle=True)
fl.write(f'\n\nepochs: 250 ')
check()

fl.close()
model.save('my_model_250e.h5')



#aa = np.loadtxt(f'./data/testdata{1111}.txt', usecols=(1, 2))
#aaa = np.diff(aa, axis=0)
#aaa = aaa[0:lasts+1]
#aaa[0][0] = aa[0][0]
#aa[0][1] = math.log(aa[0][1])+5
#checkdata = []
#checkdata.append(aaa)
#
#pr = model.predict(np.array(checkdata))
#print(checkdata)
#print(pr)
#print(aa[lasts])

#print('\n')
#for ii in range(20):
#
#   for tt in range(lasts - 1):
#        aaa[tt + 1] = aaa[tt + 2]
#
#    aaa[lasts] = pr
#
#    checkdata = []
#    checkdata.append(aaa)
#
#    pr = model.predict(np.array(checkdata))
#   print('\n')
#    print(pr)
#    print(aa[lasts+1 + ii])
