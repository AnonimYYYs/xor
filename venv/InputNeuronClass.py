class InputNeuron:

    def __init__(self):
        pass

    def inp(self, i):
        self.i = i

    def outp(self):
        self.o = self.i

    def retOutput(self):
        return(self.o)

    def retInput(self):
        return(self.i)