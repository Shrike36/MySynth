import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time
from Modifiers.WaveAdder import WaveAdder as wa
from Modifiers.Panner import StereoPanner as sp
from Modulation.ParamsModulation import ModulationType, LFOModulation
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.Oscillator import Oscillator, Type

class Synth:
    def __init__(self, render_rate, stereo : bool):
        self.render_rate = render_rate
        self.stereo = stereo

        self.oscillator_1 = Oscillator(Type.sine,render_rate)
        self.lfo_osc1 = LFO(Oscillator(Type.sine,render_rate))
        self.lfo_osc1_rate = 3
        self.envelope_osc1 = Envelope(0.3,0.8,3.8,3.9,1,render_rate)
        self.modulation_osc1 = LFOModulation(ModulationType.fm,True)
        self.modulation_osc1_amount = 1

        self.oscillator_2 = Oscillator(Type.sawtooth,render_rate)
        self.lfo_osc2 = LFO(Oscillator(Type.sine,render_rate))
        self.lfo_osc2_rate = 3
        self.envelope_osc2 = Envelope(0.3,0.8,3.8,3.9,0.5,render_rate)
        self.modulation_osc2 = LFOModulation(ModulationType.fm,True)
        self.modulation_osc2_amount = 1

        self.detune = 1/4
        self.detune_lfo = LFO(Oscillator(Type.sine,render_rate))

        self.wave_adder_index = 0.5
        self.wave_adder_lfo = LFO(Oscillator(Type.sine,render_rate))

        self.panner_index = 0.5
        self.panner_lfo = LFO(Oscillator(Type.sine,render_rate))

    def get_next_sample(self,amplitude,frequency,time):
        osc1_value = self.get_osc1_value(amplitude,frequency*(1+self.detune),time)
        osc2_value = self.get_osc2_value(amplitude,frequency*(1-self.detune),time)

        sample = wa.get_sum(osc1_value,osc2_value,0.5)

        return osc1_value, osc2_value, sample


    def get_osc1_value(self,amplitude,frequency,time):
        envelope1_value = self.envelope_osc1.get_next_value(time)
        if(self.modulation_osc1.is_working):
            lfo1_value = self.lfo_osc1.get_next_value(self.lfo_osc1_rate,time)

            osc1_value = self.modulation_osc1.get_modulated_sample(self.oscillator_1,amplitude,frequency,
                                                                   lfo1_value,self.modulation_osc1_amount,
                                                                   time,self.render_rate)
        else:
            osc1_value = self.oscillator_1.get_next_sample(amplitude,frequency,time)
        osc1_value *= envelope1_value
        return osc1_value

    def get_osc2_value(self,amplitude,frequency,time):
        envelope2_value = self.envelope_osc2.get_next_value(time)
        if(self.modulation_osc2.is_working):
            lfo2_value = self.lfo_osc2.get_next_value(self.lfo_osc2_rate,time)

            osc2_value = self.modulation_osc2.get_modulated_sample(self.oscillator_2,amplitude,frequency,
                                                                   lfo2_value,self.modulation_osc2_amount,
                                                                   time,self.render_rate)
        else:
            osc2_value = self.oscillator_2.get_next_sample(amplitude,frequency,time)
        osc2_value *= envelope2_value

        return osc2_value
