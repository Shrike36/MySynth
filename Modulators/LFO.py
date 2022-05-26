from Modulators.BaseModulator import Modulator


class LFO(Modulator):
    def __init__(self, osc, index):
        self.lfo_osc = osc
        self.index = index

    def getNextValue(self):
        return