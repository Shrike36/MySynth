import numpy as np
import enum

from Modulation.ParamsModulation import LFOModulation
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.Oscillator import Oscillator, Type
from Oscillators.WaveGenerator import WaveGenerator

class ModulatedOscillator(Oscillator):

    def __init__(self, type : Type, wave_generator, lfo : LFO, lfo_rate : float, envelope : Envelope,
                 modulation : LFOModulation, modulation_amount : float, render_rate):
        super().__init__(type, wave_generator, render_rate)
        self.lfo = lfo
        self.lfo_rate = lfo_rate
        self.modulation_amount = modulation_amount
        self.envelope = envelope
        self.modulation = modulation

    def get_next_sample(self,amplitude,frequency,time):
        if(self.modulation.is_working):
            # lfo_value = self.lfo.get_next_value(self.lfo_rate,time)
            osc_value = self.modulation.get_modulated_sample(super(), amplitude, frequency,
                                                             self.lfo, self.lfo_rate, self.modulation_amount,
                                                             time, self._render_rate)
        else:
            osc_value = super().get_next_sample(amplitude,frequency,time)
        # if(self.envelope.is_working):
        #     osc_value *= self.envelope.get_next_value(time)
        return osc_value