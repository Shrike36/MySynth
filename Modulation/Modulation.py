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
    def pm_lfo_modulation(osc,amplitude,frequency,mod_val,time,sample_rate):
        # delta = mod_val
        # print(mod_val)
        delta = sample_rate * mod_val / (2*np.pi*frequency)
        return osc.get_next_sample(amplitude,frequency,time+delta)
        # len_of_period = len(osc.period_values)
        # delta_samples = (int)(len_of_period * delta / 2*np.pi)
        # old_index = time % len_of_period
        # new_index = old_index + int(delta)
        # return osc.get_next_value(time+delta)

        # t=time/sample_rate
        # return np.cos(2*np.pi*440*t+mod_val)
        # period_len = int(self.sample_rate/self.frequency)
        # t = np.linspace(0,period_len,period_len)
        # return self.amplitude*signal.sawtooth(2 *np.pi*t, 0.5)
        # np.cos(2*np.pi*f_c*t + mod_val)
        # return (1+mod_val )*osc_val/(int(mod_index)+1)

    @staticmethod
    def fm_lfo_modulation(osc,amplitude,frequency,mod_val,time,sample_rate):
        # delta = mod_val
        # print(mod_val)
        return osc.get_next_sample(amplitude,frequency,time*(1+mod_val/frequency))

    @staticmethod
    def fm_envelope_modulation(osc_val,mod_val):
        return mod_val*osc_val