import numpy as np
from scipy import signal
from Oscillators.BaseOscillator import BaseOscillator

class TriangleOscillator(BaseOscillator):
    def get_values_of_period(self):
        period_len = int(self.sample_rate/self.frequency)
        t = np.linspace(0,1,period_len,endpoint=False)
        return self.amplitude*signal.sawtooth(2*np.pi*t, 0.5)