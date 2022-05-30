import numpy as np
import enum
from Oscillators.WaveGenerator import WaveGenerator
from numba import njit

class Type(enum.Enum):
    sine=0
    square=1
    sawtooth=2
    triangle=3

class Oscillator:

    def __init__(self, type : Type, render_rate):
        self._type = type.value
        self._is_working = True
        self._wave_generator = WaveGenerator(render_rate)
        self._render_rate = render_rate

    def get_next_sample(self,amplitude,frequency,time):
        wave = self._wave_generator.waves[self._type]
        return self.get_next_sample_numba(amplitude,frequency,time,self._render_rate,wave)

    @staticmethod
    @njit(cache=True)
    def get_next_sample_numba(amplitude,frequency,time,render_rate,wave):
        t = (int)((frequency*time) % render_rate)
        return amplitude*wave[t]

    def get_type(self):
        return self._type

    def set_type(self, new_type : Type):
        self._type = new_type

