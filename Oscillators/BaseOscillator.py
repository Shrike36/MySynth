import numpy as np

class BaseOscillator:
    def __init__(self, frequency, amplitude, sample_rate):
        self.frequency = frequency
        self.amplitude = amplitude
        self.sample_rate = sample_rate
        self.period_values = self.get_values_of_period()
        self.seconds = 0
        self.sample = 0

    def get_values_of_period(self):
        t = np.linspace(0,int(self.sample_rate/self.frequency),int(self.sample_rate/self.frequency))
        return self.amplitude*np.cos(2*np.pi*t)

    def get_next_value(self):
        # if(self.sample == self.sample_rate):
        #     self.seconds += 1
        #     self.sample = 0
        # index = self.seconds*self.sample_rate+self.sample
        # index = index % len(self.period_values)
        # self.sample+=1
        index = self.sample % len(self.period_values)
        self.sample+=1
        return self.period_values[index]

    def set_time_to_null(self):
        self.seconds = 0
        self.sample = 0
