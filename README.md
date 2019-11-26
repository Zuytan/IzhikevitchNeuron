# IzhikevitchNeuron
A simple Izhikevitch neuron model using the Runge Kutta method

Introduction
------------
The project allow to create and use Izhikevitch Neurons using the Runge-Kutta method

Usage
-----
The most common way to create them are by importing the neuron factory file  
`from izhikevitchFactory import createIzhikevitchNeuron`  
then, you can use the `createIzhikevitchNeuron` method to create basics spiking neurons.
The neurons you can create are :
 - RS : Regular Spiking
 - IB : Intrinsically Bursting
 - CH : Chattering
 - FS : Fast Spiking
 - LTS : Low-Threshold Spiking  

You can also create a specific neuron type by directly importing the neuron file  
`from izhikevitch_neuron import IzhikevitchNeuron`  
and by creating an Izhikevitch neuron :  
`neuron = IzhikevitchNeuron(a, b, c, d)`  
where :
 - a is the time scale of the membrane recovery variable
 - b is the sensitivity of the membrane recovery variable
 - c is the after-spike reset value of the membrane potential
 - d is the after-spike reset value of the membrane recovery variable
