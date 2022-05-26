import numpy as np
from scipy import signal
from Oscillators.BaseOscillator import BaseOscillator

class TriangleOscillator(BaseOscillator):
    def getValuesOfPeriod(self):
        period_len = int(self.sample_rate/self.frequency)
        t = np.linspace(0,period_len,period_len)
        return self.amplitude*signal.sawtooth(2 *np.pi*t, 0.5)