import numpy as np
from Oscillators.BaseOscillator import BaseOscillator

class SquareOscillator(BaseOscillator):
    def __init__(self, frequency, amplitude,  sample_rate, threshold=0):
        self.threshold = threshold
        super().__init__(frequency, amplitude, sample_rate)

    def get_values_of_period(self):
        period_len = int(self.sample_rate/self.frequency)
        t = np.linspace(0,period_len,period_len)
        values = self.amplitude*np.cos(2*np.pi*t)
        for i in range(0,len(values)):
            if values[i] < self.threshold:
                values[i] = -self.amplitude
            else:
                values[i] = self.amplitude
        return values