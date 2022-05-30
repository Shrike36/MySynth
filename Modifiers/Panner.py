from Modulators.LFO import LFO
from numba import njit


class StereoPanner:
    def __init__(self,index : float):
        self.index = index

    '0 <= index <= 1'
    def get_stereo_sample(self,sample,time):
        return [(1-self.index)*sample, self.index*sample]
        # stereo_sample = [(1+index)*sample,(1-index)*sample]
        # left_sample = (1+index)*sample
        # right_sample = (1-index)*sample
        # stereo_sample.append(left_sample)
        # stereo_sample.append(right_sample)

class ModulatedPanner(StereoPanner):
    def __init__(self,index : float, lfo : LFO, lfo_rate : float):
        super().__init__(index)
        self.lfo = lfo
        self.lfo_rate = lfo_rate

    '0 <= index <= 1'
    def get_stereo_sample(self,sample,time):
        x = self.lfo.get_next_value(self.lfo_rate,time)
        y = x * (self.index-0.5) + 0.5
        return [(1-y)*sample, y*sample]


