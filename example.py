from izhikevitchFactory import createIzhikevitchNeuron
import numpy as np
import matplotlib.pyplot as plt


vArr = []
tArr = []
I = 0
time = 100000
dt = 0.01

neuron = createIzhikevitchNeuron("LTS")

for t in range(0, time):
    newV = neuron.process(I, dt)
    vArr.append(newV)
    tArr.append(t)
    if t > time/3:
        I = 10

x = np.array(tArr)
y = np.array(vArr)
plt.plot(x, y)

plt.show()
