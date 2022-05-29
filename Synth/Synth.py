import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time

from Modifiers.Detune import Detune
from Modifiers.WaveAdder import WaveAdder
from Modifiers.Panner import StereoPanner
from Modulation.ParamsModulation import ModulationType, LFOModulation
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.Oscillator import Oscillator, Type

class Synth:
    def __init__(self, *oscillators : Oscillator,
                 detune : Detune,
                 wave_adder : WaveAdder,
                 stereo_panner : StereoPanner,
                 render_rate : int, stereo : bool):
        self.render_rate = render_rate
        self.stereo = stereo

        self.oscillators = oscillators

        self.detune = detune
        self.detune.set_ratio(len(oscillators))

        self.wave_adder = wave_adder

        self.stereo_panner = stereo_panner

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
        sample = self.wave_adder.get_sum(osc_values)

        if(self.stereo):
            stereo_sample = self.stereo_panner.get_stereo_sample(sample,time)

        return osc_values,sample,stereo_sample
