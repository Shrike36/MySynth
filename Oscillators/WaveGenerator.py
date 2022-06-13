import numpy as np
from numba import njit
from scipy import signal

class WaveGenerator:
    def __init__(self, render_rate):
        self.render_rate = render_rate
        self.t = np.linspace(0,1,int(self.render_rate),endpoint=False)
        self.sine_wave = self.get_sine_wave(self.t)
        self.square_wave = self.get_square_wave(self.t)
        self.sawtooth_wave = self.get_sawtooth_wave(self.t)
        self.triangle_wave = self.get_triangle_wave(self.t)
        self.waves = self.get_waves()
        self.int_waves = self.get_int_waves()


    def get_int_waves(self):
        int_waves = []

        sine_wave_int = np.zeros(self.render_rate)
        square_wave_int = np.zeros(self.render_rate)
        sawtooth_wave_int = np.zeros(self.render_rate)
        triangle_wave_int = np.zeros(self.render_rate)

        for i in range(1,self.render_rate):
            sine_wave_int[i] = self.get_int_wave(self.sine_wave,i,self.render_rate)#np.trapz(self.sine_wave[:i])/self.render_rate
            square_wave_int[i] = self.get_int_wave(self.square_wave,i,self.render_rate)#np.trapz(self.square_wave[:i])/self.render_rate
            sawtooth_wave_int[i] = self.get_int_wave(self.sawtooth_wave,i,self.render_rate)#np.trapz(self.sawtooth_wave[:i])/self.render_rate
            triangle_wave_int[i] = self.get_int_wave(self.triangle_wave,i,self.render_rate)#np.trapz(self.triangle_wave[:i])/self.render_rate

        int_waves.append(np.array(sine_wave_int))
        int_waves.append(np.array(square_wave_int))
        int_waves.append(np.array(sawtooth_wave_int))
        int_waves.append(np.array(triangle_wave_int))

        return int_waves

    def get_waves(self):
        waves = []
        waves.append(self.sine_wave)
        waves.append(self.square_wave)
        waves.append(self.sawtooth_wave)
        waves.append(self.triangle_wave)
        return waves

    @staticmethod
    @njit(cache=True)
    def get_int_wave(wave,i,render_rate):
        return np.trapz(wave[:i])/render_rate

    @staticmethod
    @njit(cache=True)
    def get_sine_wave(t):
        return np.sin(2*np.pi*t)


    @staticmethod
    @njit(cache=True)
    def get_square_wave(t):
        values = np.sin(2*np.pi*t)
        for i in range(0,len(values)):
            if values[i] < 0:
                values[i] = -1
            else:
                values[i] = 1
        return values

    @staticmethod
    def get_sawtooth_wave(t):
        # period_len = int(self.render_rate/self.frequency)
        # t = np.linspace(-period_len/2,period_len/2,period_len)
        # return -2*self.amplitude/(period_len)*t
        return signal.sawtooth(2*np.pi*t, 0)

    @staticmethod
    def get_triangle_wave(t):
        return signal.sawtooth(2*np.pi*t, 0.5)