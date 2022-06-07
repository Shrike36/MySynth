from enum import Enum
from scipy import signal
import numpy as np
from numba import njit

class ModulationType(Enum):
    am = 0
    fm = 1
    pm = 2

class LFOModulation:
    def __init__(self, type : ModulationType):
        self.is_working = True
        self.type = type.value

    def get_modulated_sample(self, osc, osc_amplitude, osc_frequency,
                             lfo, lfo_frequencey, mod_index,
                             time, render_rate):
        if(self.type == 0):
            lfo_val = lfo.get_next_value(lfo_frequencey,time)
            osc_val = osc.get_next_sample(osc_amplitude, osc_frequency, time)
            return self.get_new_amplitude_for_am(osc_val,lfo_val,mod_index)
        elif(self.type == 1):
            lfo_val = lfo.get_next_integral(lfo_frequencey,time)
            return osc.get_next_sample(osc_amplitude, osc_frequency,
                                       self.get_new_time_for_fm(time,lfo_val,mod_index,osc_frequency,render_rate))
        else:
            lfo_val = lfo.get_next_value(lfo_frequencey,time)
            return osc.get_next_sample(osc_amplitude, osc_frequency,
                                       self.get_new_time_for_pm(time,lfo_val,mod_index,osc_frequency,render_rate))

    # def get_modulated_sample(self, osc, osc_amplitude, osc_frequency,
    #                          lfo, lfo_frequencey, mod_index,
    #                          time, render_rate):
    #     if(self.type == 0):
    #         lfo_val = lfo.get_next_value(lfo_frequencey,time)
    #         osc_val = osc.get_next_sample(osc_amplitude, osc_frequency, time)
    #         return (1+mod_index*lfo_val)*osc_val/mod_index
    #     elif(self.type == 1):
    #         lfo_val = lfo.get_next_integral(lfo_frequencey,time)
    #         return osc.get_next_sample(osc_amplitude, osc_frequency,
    #                                    time + render_rate * mod_index * lfo_val / osc_frequency)
    #     else:
    #         lfo_val = lfo.get_next_value(lfo_frequencey,time)
    #         return osc.get_next_sample(osc_amplitude, osc_frequency,
    #                                    time + render_rate * mod_index * lfo_val / (2*np.pi*osc_frequency))

    @staticmethod
    @njit
    def get_new_amplitude_for_am(osc_val,lfo_val,mod_index):
        return (1+mod_index*lfo_val)*osc_val/mod_index

    @staticmethod
    @njit
    def get_new_time_for_pm(time,lfo_val,mod_index,frequency,render_rate):
        return time + render_rate * mod_index * lfo_val / (2*np.pi*frequency)

    @staticmethod
    @njit
    def get_new_time_for_fm(time,lfo_val,mod_index,frequency,render_rate):
        return time + render_rate * mod_index * lfo_val / frequency

    # def am_lfo_modulation(osc_val,mod_val,mod_index):
    #     return (1+mod_val)*osc_val/(int(mod_index)+1)

    # @staticmethod
    # def pm_lfo_modulation(osc,amplitude,frequency,mod_val,time,render_rate):
    #     delta = render_rate * mod_val / (2*np.pi*frequency)
    #     return osc.get_next_sample(amplitude,frequency,time+delta)
    #
    # @staticmethod
    # def fm_lfo_modulation(osc,amplitude,frequency,mod_val,time):
    #     return osc.get_next_sample(amplitude,frequency,time*(1+mod_val/frequency))

class EnvelopeModulation:
    def __init__(self, is_working : bool):
        self.is_working = is_working

    @staticmethod
    def get_modulated_sample(osc_val,mod_val):
        return mod_val*osc_val

    # @staticmethod
    # def am_envelope_modulation(osc_val,mod_val):
    #     return mod_val*osc_val