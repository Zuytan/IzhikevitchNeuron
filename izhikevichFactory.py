from izhikevich_neuron import IzhikevichNeuron

neuronTypes = {
    "RS": IzhikevichNeuron(0.02, 0.2, -65, 8),
    "IB": IzhikevichNeuron(0.02, 0.2, -55, 4),
    "CH": IzhikevichNeuron(0.02, 0.2, -50, 2),
    "FS": IzhikevichNeuron(0.1, 0.2, -65, 2),
    "LTS": IzhikevichNeuron(0.02, 0.25, -65, 2),
}


def createSpecificIzhikevichNeuron(neuronType):
    """
    Function that return a neuron of a specific type given in parameters.
    If the type is unknown, it will return a regular spiking neuron 
    ...
    Parameters:
    -----------
    neuronType: str
      Type of the neuron that will be returned.
      Available neurons:
        "RS": Regular Spiking
        "IB": Intrinsically Bursting
        "CH": Chattering
        "FS": Fast Spiking
        "LTS": Low Threshold Spiking
    """
    return neuronTypes.get(neuronType, IzhikevichNeuron(0.02, 0.2, -65, 8))


def createIzhikevichNeuron(a, b, c, d):
    return IzhikevichNeuron(a, b, c, d)
