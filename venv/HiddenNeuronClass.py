import math

class HiddenNeuron:

    def __init__(self):
        self.i = 0
        self.o = 0
        self.delta = 0
        pass

    def inp(self, i):
        self.i = i

    def outp(self):
        x = self.i
        x = round(1 / (1 + math.exp(-x)), 10)
        #x = round( (math.exp(2*x) - 1) / (math.exp(2*x) + 1) ,10)
        self.o = x

    def retOutput(self):
        return self.o

    def delt(self, w, delt):
        self.delta = ((1 - self.o) * self.o) * w * delt

    def retDelt(self):
        return(self.delta)

    def retInput(self):
        return (self.i)