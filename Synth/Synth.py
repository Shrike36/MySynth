import sys

import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from scipy.io import wavfile
import time

from Modifiers.Detune import Detune
from Modifiers.WaveAdder import WaveAdder
from Modifiers.Panner import StereoPanner
from Modulation.ParamsModulation import ModulationType, LFOModulation
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.Oscillator import Oscillator, Type
from Oscillators.WaveGenerator import WaveGenerator
from Synth.Parameters import SynthParams


class Synth:
    def __init__(self, *oscillators : Oscillator,
                 detune : Detune,
                 wave_adder : WaveAdder,
                 stereo_panner : StereoPanner,
                 params : SynthParams,
                 render_rate : int, stereo : bool):
        self.render_rate = render_rate
        self.stereo = stereo

        self.oscillators = oscillators

        self.detune = detune
        self.detune.set_ratio(len(oscillators))

        self.wave_adder = wave_adder

        self.stereo_panner = stereo_panner

        self.wave_gen = self.oscillators[0].wave_generator

        self.params = params

    def get_next_sample(self,amplitude,frequency,time,pressed=True,time_up=sys.maxsize/2):
        osc_values = []
        for oscillator in self.oscillators:
            if self.detune.is_working:
                detune_value = self.detune.get_next_value(time)
            else:
                detune_value = 0
            osc_values.append(oscillator.get_next_sample(amplitude=amplitude,
                                                         frequency=frequency*(1+detune_value),
                                                         time=time,
                                                         pressed=pressed,
                                                         time_up=time_up))
        sample = self.wave_adder.get_sum(osc_values)

        if(self.stereo):
            stereo_sample = self.stereo_panner.get_stereo_sample(sample,time)

        return sample
        # return osc_values,sample#,stereo_sample

    def get_next_sample_with_numba(self,amplitude,frequency,time,render_rate,pressed=True,time_up=sys.maxsize/2):

        return self.decor(amplitude, frequency, time,
                          self.params.osc_1_type, self.params.osc_1_is_working,
                          self.params.mod_1_is_working, self.params.mod_1_type, self.params.mod_1_index,
                          self.params.lfo_1_type, self.params.lfo_1_frequency,
                          self.params.osc_2_type, self.params.osc_2_is_working,
                          self.params.mod_2_is_working, self.params.mod_2_type, self.params.mod_2_index,
                          self.params.lfo_2_type, self.params.lfo_2_frequency,
                          self.params.osc_1_adder_index, self.params.osc_2_adder_index,
                          self.params.detune_is_working, self.params.detune_index,
                          self.params.panner_is_working, self.params.panner_index,
                          self.params.panner_modulation_is_working,self.params.lfo_panner_type,self.params.lfo_panner_frequency,
                          render_rate,
                          pressed, time_up,
                          self.wave_gen.waves, self.wave_gen.int_waves)

    @staticmethod
    @njit(cache=True)
    def decor(amplitude,frequency,time,
              oscillator_1_type,oscillator_1_is_working,modulation_1_is_working,modulation_1_type,modulation_1_index,lfo_1_type,lfo_1_frequency,
              oscillator_2_type,oscillator_2_is_working,modulation_2_is_working,modulation_2_type,modulation_2_index,lfo_2_type,lfo_2_frequency,
              oscillator_1_adder_index,oscillator_2_adder_index,
              detune_is_working,detune_index,
              panner_is_working,panner_index,
              panner_modulation_is_working,lfo_panner_type,lfo_panner_frequency,
              render_rate,
              pressed=True,time_up=sys.maxsize/2,
              waves=np.array([]),integrals=np.array([])):

        oscillator_1_wave = waves[oscillator_1_type]
        lfo_1_wave = waves[lfo_1_type]
        lfo_1_int = integrals[lfo_1_type]
        oscillator_1_frequency = frequency

        oscillator_2_wave = waves[oscillator_2_type]
        lfo_2_wave = waves[lfo_2_type]
        lfo_2_int = integrals[lfo_2_type]
        oscillator_2_frequency = frequency

        if detune_is_working:
            minus = []
            plus = []
            max = int(2/2)+1
            for i in range(1,max):
                minus.append(detune_index*(-1/i))
                plus.append(detune_index*(1/(max-i)))
            if not (2 % 2 == 0):
                minus.append(0)
            detune_values = minus + plus

            oscillator_1_frequency = detune_values[0] + oscillator_1_frequency
            oscillator_2_frequency = detune_values[1] + oscillator_2_frequency

        sample = np.zeros(len(time))


        if pressed:
            i = 0
            t = 0
            while i < len(time):
                t = time[i]

                if oscillator_1_is_working:
                    if modulation_1_is_working:
                        lfo_1_t = (int)((lfo_1_frequency*t) % render_rate)
                        if modulation_1_type == 0:
                            osc_1_t = (int)((oscillator_1_frequency*t) % render_rate)
                            lfo_val = lfo_1_wave[lfo_1_t]
                            osc_val = oscillator_1_wave[osc_1_t]
                            oscillator_1_value = (1+modulation_1_index*lfo_val)*osc_val/modulation_1_index
                        elif modulation_1_type == 1:
                            lfo_val = lfo_1_int[lfo_1_t]
                            osc_1_t = t + render_rate * modulation_1_index * lfo_val / oscillator_1_frequency
                            osc_1_t = (int)((oscillator_1_frequency*osc_1_t) % render_rate)
                            oscillator_1_value = oscillator_1_wave[osc_1_t]
                        else:
                            lfo_val = lfo_1_wave[lfo_1_t]
                            osc_1_t = t + render_rate * modulation_1_index * lfo_val / (2*np.pi*oscillator_1_frequency)
                            osc_1_t = (int)((oscillator_1_frequency*osc_1_t) % render_rate)
                            oscillator_1_value = oscillator_1_wave[osc_1_t]
                    else:
                        osc_1_t = (int)((oscillator_1_frequency*t) % render_rate)
                        oscillator_1_value = oscillator_1_wave[osc_1_t]
                else:
                    oscillator_1_value = 0

                if oscillator_2_is_working:
                    if modulation_2_is_working:
                        lfo_2_t = (int)((lfo_2_frequency*t) % render_rate)
                        if modulation_2_type == 0:
                            osc_2_t = (int)((oscillator_2_frequency*t) % render_rate)
                            lfo_val = lfo_2_wave[lfo_2_t]
                            osc_val = oscillator_2_wave[osc_2_t]
                            oscillator_2_value = (1+modulation_2_index*lfo_val)*osc_val/modulation_2_index
                        elif modulation_2_type == 1:
                            lfo_val = lfo_2_int[lfo_2_t]
                            osc_2_t = t + render_rate * modulation_2_index * lfo_val / oscillator_2_frequency
                            osc_2_t = (int)((oscillator_2_frequency*osc_2_t) % render_rate)
                            oscillator_2_value = oscillator_2_wave[osc_2_t]
                        else:
                            lfo_val = lfo_2_wave[lfo_2_t]
                            osc_2_t = t + render_rate * modulation_2_index * lfo_val / (2*np.pi*oscillator_2_frequency)
                            osc_2_t = (int)((oscillator_2_frequency*osc_2_t) % render_rate)
                            oscillator_2_value = oscillator_2_wave[osc_2_t]
                    else:
                        osc_2_t = (int)((oscillator_2_frequency*t) % render_rate)
                        oscillator_2_value = oscillator_2_wave[osc_2_t]
                else:
                    oscillator_2_value = 0

                oscillator_1_value = amplitude*oscillator_1_value
                oscillator_2_value = amplitude*oscillator_2_value

                sample_val = (oscillator_1_adder_index*oscillator_1_value + oscillator_2_adder_index*oscillator_2_value) \
                             / (oscillator_1_adder_index+oscillator_2_adder_index)

                sample[i] = sample_val

                i = i + 1

        stereo_sample = np.empty((2,len(time)))
        if not panner_is_working:
            stereo_sample[0] = 1*sample
            stereo_sample[1] = 1*sample
        else:
            if not panner_modulation_is_working:
                stereo_sample[0] = (1-panner_index)*sample
                stereo_sample[1] = panner_index*sample
            else:
                lfo_panner_wave = waves[lfo_panner_type]
                i = 0
                t = 0
                while i < len(time):
                    t = time[i]
                    lfo_panner_t = (int)((lfo_panner_frequency*t) % render_rate)
                    lfo_panner_val = lfo_panner_wave[lfo_panner_t]
                    amp = lfo_panner_val * (panner_index-0.5) + 0.5
                    stereo_sample[0][i] = (1 - amp) * sample[i]
                    stereo_sample[1][i] = amp * sample[i]
                    i = i + 1

        return stereo_sample
