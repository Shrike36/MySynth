import numpy as np
import enum
from Oscillators.WaveGenerator import WaveGenerator

class Type(enum.Enum):
    sine=0
    square=1
    sawtooth=2
    triangle=3

class Oscillator:

    def __init__(self, type : Type, render_rate):
        self.type = type.value
        self.wave_generator = WaveGenerator(render_rate)
        self.render_rate = render_rate

    def get_next_sample(self,amplitude,frequency,time):
        t = (int)((frequency*time)%self.render_rate)
        wave = self.wave_generator.waves[self.type]
        return amplitude*wave[t]


