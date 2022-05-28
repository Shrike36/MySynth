import numpy as np
from Oscillators.Oscillator import Oscillator

class SineOscillator(Oscillator):
    def get_values_of_period(self):
        period_len = int(self.sample_rate/self.frequency)
        t = np.linspace(0,1,period_len,endpoint=False)
        return self.amplitude*np.cos(2*np.pi*t)
