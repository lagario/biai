import numpy as np
from keras import Sequential, optimizers
from keras.layers import Dense, Flatten

inputs = []
outputs = []
lasts = 5

for tnr in range(1000):

    d = np.loadtxt(f'./data/testdata{tnr}.txt', usecols=(1, 2))
    dd = np.diff(d, axis=0)

    for i in range(len(dd) - lasts - 1):
        inputs.append(dd[i:i + lasts])
        outputs.append(dd[i + lasts])


def baseline_model():
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(lasts*2, activation='linear', input_dim=1))
    model.add(Dense(6, activation='linear'))
    model.add(Dense(2, activation='linear'))
    ada = optimizers.Adadelta()
    model.compile(optimizer=ada, loss="mean_squared_error", metrics=['accuracy'])
    return model


i = np.array(inputs)
o = np.array(outputs)

model = baseline_model()
model.fit(i, o, epochs=50, shuffle=True)

model.save('my_model.h5')

aa = np.loadtxt(f'./data/testdata{1111}.txt', usecols=(1, 2))
aa = np.diff(aa, axis=0)
aaa = aa[0:lasts]
checkdata = []
checkdata.append(aaa)

pr = model.predict(np.array(checkdata))
print(checkdata)
print(pr)
print(aa[lasts])

print('\n')
for ii in range(20):

    for tt in range(lasts-1):
        aaa[tt] = aaa[tt+1]

        aaa[lasts-1] = pr

    checkdata = []
    checkdata.append(aaa)

    pr = model.predict(np.array(checkdata))
    print('\n')
    print(pr)
    print(aa[lasts+1 + ii])
