import numpy as np
from scipy import signal
from Oscillators.BaseOscillator import BaseOscillator


class SawtoothOscillator(BaseOscillator):
    def get_values_of_period(self):
        # period_len = int(self.sample_rate/self.frequency)
        # t = np.linspace(-period_len/2,period_len/2,period_len)
        # return -2*self.amplitude/(period_len)*t
        period_len = int(self.sample_rate/self.frequency)
        t = np.linspace(0,period_len,period_len)
        return self.amplitude*signal.sawtooth(2 *np.pi*t, 0)