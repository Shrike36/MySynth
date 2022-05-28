import numpy as np
from scipy import signal

class WaveGenerator:
    def __init__(self, sample_rate):
        self.sample_rate = sample_rate
        self.t = np.linspace(0,1,int(self.sample_rate),endpoint=False)
        self.sine_wave = self.get_sine_wave()
        self.square_wave = self.get_square_wave()
        self.sawtooth_wave = self.get_sawtooth_wave()
        self.triangle_wave = self.get_triangle_wave()

    def get_sine_wave(self):
        return np.cos(2*np.pi*self.t)

    def get_square_wave(self):
        values = np.cos(2*np.pi*self.t)
        for i in range(0,len(values)):
            if values[i] < 0:
                values[i] = -1
            else:
                values[i] = 1
        return values

    def get_sawtooth_wave(self):
        # period_len = int(self.sample_rate/self.frequency)
        # t = np.linspace(-period_len/2,period_len/2,period_len)
        # return -2*self.amplitude/(period_len)*t
        return signal.sawtooth(2*np.pi*self.t, 0)

    def get_triangle_wave(self):
        return signal.sawtooth(2*np.pi*self.t, 0.5)