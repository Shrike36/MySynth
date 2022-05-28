import numpy as np
import enum
from Oscillators.WaveGenerator import WaveGenerator

class Type(enum.Enum):
    sine=0
    square=1
    sawtooth=2
    triangle=3

class Oscillator:

    def __init__(self, type : Type, sample_rate):
        self.type = type.value
        self.wave_generator = WaveGenerator(sample_rate)
        self.sample_rate = sample_rate

    def get_next_sample(self,amplitude,frequency,time):
        t = (int)((frequency*time)%self.sample_rate)
        wave = self.wave_generator.waves[self.type]
        return amplitude*wave[t]
        # wave=0
        # if(type == 1):
        #     wave = self.wave_generator.sine_wave
        # elif(type == 2):
        #     wave = self.wave_generator.square_wave
        # elif(type==3):
        #     wave = self.wave_generator.sawtooth_wave
        # else:
        #     wave = self.wave_generator.triangle_wave
        # return amplitude*wave[t]


        # if(self.sample == self.sample_rate):
        #     self.seconds += 1
        #     self.sample = 0
        # index = self.seconds*self.sample_rate+self.sample
        # index = index % len(self.period_values)
        # self.sample+=1
        # index = self.sample % len(self.period_values)
        # self.sample+=1
        # return self.period_values[index]
        # return self.period_values[time % len(self.period_values)]

