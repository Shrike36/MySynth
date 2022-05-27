from Modulators.BaseModulator import Modulator


class LFO(Modulator):
    def __init__(self, osc, index):
        self.lfo_osc = osc
        self.index = index

    def get_next_value(self):
        return self.index * self.lfo_osc.get_next_value() / self.lfo_osc.amplitude

    def set_time_to_null(self):
        self.lfo_osc.set_time_to_null()