from izhikevitch_neuron import IzhikevitchNeuron

neuronTypes = {
    "RS": IzhikevitchNeuron(0.02, 0.2, -65, 8),
    "IB": IzhikevitchNeuron(0.02, 0.2, -55, 4),
    "CH": IzhikevitchNeuron(0.02, 0.2, -50, 2),
    "FS": IzhikevitchNeuron(0.1, 0.2, -65, 2),
    "LTS": IzhikevitchNeuron(0.02, 0.25, -65, 2),
}


def createIzhikevitchNeuron(neuronType):
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
    return neuronTypes.get(neuronType, IzhikevitchNeuron(0.02, 0.2, -65, 8))
