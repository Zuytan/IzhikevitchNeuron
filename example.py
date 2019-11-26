from izhikevichFactory import createIzhikevichNeuron
import numpy as np
import matplotlib.pyplot as plt


vArr = []
uArr = []
tArr = []
I = 0
time = 5000
dt = 0.1
neuron = createIzhikevichNeuron(0.02, 0.25, -50, 1.5)

for t in range(0, time):
    newV, newU = neuron.process(I, dt)
    vArr.append(newV)
    uArr.append(newU)
    tArr.append(t)
    if t > time/5:
        I = 10

x = np.array(tArr)
y = np.array(vArr)
y2 = np.array(uArr)
_, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y2)
ax.set(xlabel='time steps', ylabel='voltage (mV)')
plt.show()
