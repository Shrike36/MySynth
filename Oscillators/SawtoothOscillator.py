import numpy as np
from scipy import signal
from Oscillators.Oscillator import Oscillator


class SawtoothOscillator(Oscillator):
    def get_values_of_period(self):
        # period_len = int(self.sample_rate/self.frequency)
        # t = np.linspace(-period_len/2,period_len/2,period_len)
        # return -2*self.amplitude/(period_len)*t
        period_len = int(self.sample_rate/self.frequency)
        t = np.linspace(0,1,period_len,endpoint=False)
        return self.amplitude*signal.sawtooth(2*np.pi*t, 0)