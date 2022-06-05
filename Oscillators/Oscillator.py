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

    def __init__(self, type : Type, wave_generator, render_rate):
        self._type = type.value
        self._is_working = True
        self.wave_generator = wave_generator
        self._render_rate = render_rate

    def get_next_sample(self,amplitude,frequency,time):
        wave = self.wave_generator.waves[self._type]
        return self.get_next_sample_numba(amplitude,frequency,time,self._render_rate,wave)

    @staticmethod
    @njit(cache=True)
    def get_next_sample_numba(amplitude,frequency,time,render_rate,wave):
        t = (int)((frequency*time) % render_rate)
        return amplitude*wave[t]

    def get_next_integral(self,frequency,time):
        int_wave = self.wave_generator.int_waves[self._type]
        return self.get_next_integral_numba(frequency,time,self._render_rate,int_wave)

    @staticmethod
    @njit(cache=True)
    def get_next_integral_numba(frequency, time, render_rate, int_wave):
        t = (int)((frequency*time) % render_rate)
        return int_wave[t]

    def get_type(self):
        return self._type

    def set_type(self, new_type : Type):
        self._type = new_type

