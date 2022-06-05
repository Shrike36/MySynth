import numpy as np
from scipy import signal

class WaveGenerator:
    def __init__(self, render_rate):
        self.render_rate = render_rate
        self.t = np.linspace(0,1,int(self.render_rate),endpoint=False)
        self.sine_wave = self.get_sine_wave()
        self.square_wave = self.get_square_wave()
        self.sawtooth_wave = self.get_sawtooth_wave()
        self.triangle_wave = self.get_triangle_wave()
        self.waves = self.get_waves()
        self.int_waves = self.get_int_waves()


    def get_int_waves(self):
        int_waves = []

        sine_wave_int = [0]*self.render_rate
        square_wave_int = [0]*self.render_rate
        sawtooth_wave_int = [0]*self.render_rate
        triangle_wave_int = [0]*self.render_rate

        for i in range(1,self.render_rate):
            sine_wave_int[i] = np.trapz(self.sine_wave[:i])/self.render_rate
            square_wave_int[i] = np.trapz(self.square_wave[:i])/self.render_rate
            sawtooth_wave_int[i] = np.trapz(self.sawtooth_wave[:i])/self.render_rate
            triangle_wave_int[i] = np.trapz(self.triangle_wave[:i])/self.render_rate

        int_waves.append(np.array(sine_wave_int))
        int_waves.append(np.array(square_wave_int))
        int_waves.append(np.array(sawtooth_wave_int))
        int_waves.append(np.array(triangle_wave_int))

        return int_waves

    def get_waves(self):
        waves = []
        waves.append(self.get_sine_wave())
        waves.append(self.get_square_wave())
        waves.append(self.get_sawtooth_wave())
        waves.append(self.get_triangle_wave())
        return waves

    def get_sine_wave(self):
        return np.sin(2*np.pi*self.t)

    def get_square_wave(self):
        values = np.sin(2*np.pi*self.t)
        for i in range(0,len(values)):
            if values[i] < 0:
                values[i] = -1
            else:
                values[i] = 1
        return values

    def get_sawtooth_wave(self):
        # period_len = int(self.render_rate/self.frequency)
        # t = np.linspace(-period_len/2,period_len/2,period_len)
        # return -2*self.amplitude/(period_len)*t
        return signal.sawtooth(2*np.pi*self.t, 0)

    def get_triangle_wave(self):
        return signal.sawtooth(2*np.pi*self.t, 0.5)