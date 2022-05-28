from scipy import signal
import numpy as np

class Modulation:
    @staticmethod
    def am_lfo_modulation(osc_val,mod_val,mod_index):
        return (1+mod_val)*osc_val/(int(mod_index)+1)

    @staticmethod
    def am_envelope_modulation(osc_val,mod_val):
        return mod_val*osc_val

    @staticmethod
    def pm_lfo_modulation(osc,amplitude,frequency,mod_val,time,render_rate):
        delta = render_rate * mod_val / (2*np.pi*frequency)
        return osc.get_next_sample(amplitude,frequency,time+delta)

    @staticmethod
    def fm_lfo_modulation(osc,amplitude,frequency,mod_val,time):
        return osc.get_next_sample(amplitude,frequency,time*(1+mod_val/frequency))

    @staticmethod
    def fm_envelope_modulation(osc_val,mod_val):
        return mod_val*osc_val