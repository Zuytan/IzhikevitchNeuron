# Izhikevitch model :
# v' = 0.04v² + 5v + 140 - u + I
# u' = a(bv-u)
# if v >= 30mv => v <- c
#              => u <- u+d


def membranePotential(v, u, i):
    """
    Function that return the membrane potential value of a neuron.

    Parameters:
    -----------
    v: double
        Previous membrane potential value
    u: double
        Previous membrane recovery value
    i: double
        Current input value of the neuron
    """
    return 0.04 * pow(v, 2) + 5*v+140-u+i


def membraneRecovery(a, b, v, u):
    """
    Function that return the membrane recovery value of a neuron

    Parameters:
    -----------
    a: double
        Time scale of the recovery variable u
    b: double
        Sensitivity of the recovery variable u
    v: double
        Previous membrane potential value
    u: double
        Previous membrane recovery value

    """
    return a*(b*v-u)


class IzhikevitchNeuron:
    """
    A class used to represent an Izhikevitch neuron

    ...

    Attributes
    ----------
    a : double
        Time scale of the recovery variable u
    b : double
        Sensitivity of the recovery variable u
    c : double
        After-spike reset value of the membrane potential
    d : double
        After-spike reset value of the recovery variable u
    v: double
        Membrane potential value
    u: double
        Membrane recovery value
    threshold: double
        Spike threshold before resetting

    Methods
    -------
    process(i, dt)
        Process a new state from an input and a step size and return the new membrane potential (v)
    """

    def __init__(self, a, b, c, d):
        """
        Constructor that create an Izhikevitch neuron from datas given in parameters

        Parameters:
        -----------
        a: double
            Time scale of the recovery variable u
        b: double
            Sensitivity of the recovery variable u
        c: double
            After-spike reset value of the membrane potential
        d: double
            After-spike reset value of the recovery variable u

        """
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__u = 0
        self.__v = 0
        self.threshold = 30

    def __rungeKutta(self, i, dt):
        """
        Apply the runge kutta method and return the new v and new u 

        Parameters:
        -----------
        i: double
            Current input value of the neuron
        dt: double
            Time-step size

        """
        newV = self.__v
        newU = self.__u
        dv = membranePotential(self.__v, self.__u, i)
        k1 = dv * 2 * dt
        dv = membranePotential(self.__v + 0.5 * k1, self.__u, i)*dt
        k2 = dv * 2 * dt
        dv = membranePotential(self.__v + 0.5 * k2, self.__u, i)*dt
        k3 = dv * 2 * dt
        dv = membranePotential(self.__v + k3, self.__u, i)*dt
        k4 = dv * 2 * dt
        newV += (k1 + 2*k2 + 2*k3 + k4)/6

        du = membraneRecovery(self.__a, self.__b, self.__v, self.__u)
        k1 = du * 2 * dt
        du = membraneRecovery(self.__a, self.__b,
                              self.__v, self.__u + 0.5 * k1)*dt
        k2 = du * 2 * dt
        du = membraneRecovery(self.__a, self.__b,
                              self.__v, self.__u + 0.5 * k2)*dt
        k3 = du * 2 * dt
        du = membraneRecovery(self.__a, self.__b, self.__v, self.__u * k3)*dt
        k4 = du * 2 * dt
        newU += (k1 + 2*k2 + 2*k3 + k4)/6

        return newU, newV

    def process(self, i, dt):
        """
        Process a new state from an input and a step size and return the new membrane potential (v) 

        Parameters:
        -----------
        i: double
            Current input value of the neuron
        dt: double
            Time-step size

        """
        newU, newV = self.__rungeKutta(i, dt)
        if(newV >= self.threshold):
            newV = self.__c
            newU += self.__d
        self.__v = newV
        self.__u = newU
        return self.__v
