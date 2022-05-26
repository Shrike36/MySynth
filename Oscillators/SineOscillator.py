import numpy as np
from Oscillators.BaseOscillator import BaseOscillator

class SineOscillator(BaseOscillator):
    def getValuesOfPeriod(self):
        period_len = int(self.sample_rate/self.frequency)
        t = np.linspace(0,period_len,period_len)
        return self.amplitude*np.cos(2*np.pi*t)
