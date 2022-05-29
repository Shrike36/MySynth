import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time

from Modifiers.Detune import Detune
from Modifiers.WaveAdder import WaveAdder as wa
from Modifiers.Panner import StereoPanner as sp
from Modulation.ParamsModulation import ModulationType, LFOModulation
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.Oscillator import Oscillator, Type

class Synth:
    def __init__(self, *oscillators : Oscillator, detune : Detune, render_rate : int, stereo : bool):
        self.render_rate = render_rate
        self.stereo = stereo

        self.oscillators = oscillators

        self.detune = detune
        self.detune.set_ratio(len(oscillators))

        self.detune_lfo = LFO(Oscillator(Type.sine,render_rate))

        self.wave_adder_index = 0.5
        self.wave_adder_lfo = LFO(Oscillator(Type.sine,render_rate))

        self.panner_index = 0.5
        self.panner_lfo = LFO(Oscillator(Type.sine,render_rate))

    def get_next_sample(self,amplitude,frequency,time):
        osc_values = []
        for oscillator in self.oscillators:
            if self.detune.is_working:
                detune_value = self.detune.get_next_value(time)
            else:
                detune_value = 0
            osc_values.append(oscillator.get_next_sample(amplitude,
                                                         frequency*(1+detune_value),
                                                         time))
        # sample = wa.get_sum(osc1_value,osc2_value,0.5)

        return osc_values
