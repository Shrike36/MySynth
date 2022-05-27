from Modulators.BaseModulator import Modulator
import numpy as np

class Envelope(Modulator):
    def __init__(self, attack_duration, decay_duration, sustain_duration, release_duration,
                 sustain_level, sample_rate):
        self.attack_len = int(attack_duration*sample_rate)
        self.decay_len = int(decay_duration*sample_rate)
        self.sustain_len = int(sustain_duration*sample_rate)
        self.release_len = int(release_duration*sample_rate)
        self.len = self.attack_len+self.decay_len+self.sustain_len+self.release_len
        self.sustain_level = sustain_level
        self.sample_rate = sample_rate

        self.values = self.get_values()

        self.seconds = 0
        self.sample = 0

    def get_values(self):
        att=self.get_attack_values()
        dec=self.get_decay_values()
        sus=self.get_sustain_values()
        rel=self.get_release_values()
        vals = []
        for val1 in att:
            vals.append(val1)
        for val2 in dec:
            vals.append(val2)
        for val3 in sus:
            vals.append(val3)
        for val4 in rel:
            vals.append(val4)
        return vals

    def get_attack_values(self):
        return np.linspace(0,1,self.attack_len)

    def get_decay_values(self):
        return np.linspace(1,self.sustain_level,self.decay_len)

    def get_sustain_values(self):
        return np.linspace(self.sustain_level,self.sustain_level,self.sustain_len)

    def get_release_values(self):
        return np.linspace(self.sustain_level, 0, self.release_len)

    def get_next_value(self):
        # if(self.sample == self.sample_rate):
        #     self.seconds += 1
        #     self.sample = 0
        # index = self.seconds*self.sample_rate+self.sample
        # self.sample+=1
        # if index >= self.len:
        #     return 0
        # return self.values[index]
        index = self.sample
        self.sample+=1
        if index >= self.len:
            return 0
        return self.values[index]


    def set_time_to_null(self):
        self.seconds = 0
        self.sample = 0
