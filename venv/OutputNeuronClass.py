import math

class OutputNeuron:

    def __init__(self):
        pass

    def inp(self, i):
        self.i = i

    def outp(self):
        x = self.i
        x = round( 1 / (1 + math.exp(-x)), 10)
        #x = round((math.exp(2 * x) - 1) / (math.exp(2 * x) + 1), 10)
        self.o = x

    def retOutput(self):
        return(self.o)

    def delt(self, perfect):
        self.delta = (perfect - self.o) * ((1 - self.o) * self.o)

    def retDelt(self):
        return(self.delta)

    def retInput(self):
        return (self.i)