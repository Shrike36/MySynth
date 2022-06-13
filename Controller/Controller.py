import threading
from copy import copy

import pyaudio
from numba import njit

from Controller.midi import MidiInterface
import numpy as np
from scipy.interpolate import interp1d
from multiprocessing import Process

from Synth.Synth import Synth


class Controller:
    def __init__(self, synth, sample_rate = 30000, buffer_size = 256):
        self.midi_port = None
        self.midi_interface = None
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.p = pyaudio.PyAudio()
        self.stream = self.settings(1, self.sample_rate, True, self.buffer_size)
        self.stream.start_stream()

        self.fade_seq = 256#buffer_size/10
        self.smooth_buffer = np.zeros(self.fade_seq)
        self.coefficients = np.linspace(0, 1, self.fade_seq)
        self.coefficientsR = self.coefficients[::-1]

        self.synth = synth

        self.lfo_rate = 1

        self.running = False
        self.pressed = False

        # self.process = threading.Thread(target=self.render,daemon=True)
        self.process = threading.Thread(target=self.render_with_numba,daemon=True)

    def settings(self, channels, rate, output, buffer_size):
        return self.p.open(format=pyaudio.paFloat32,
                           channels=channels,
                           rate=rate,
                           output=output,
                           frames_per_buffer=buffer_size)

    def change_midi_port(self, port, port_count):
        print("midi port changed to:", port)
        if port is not None and port < port_count:
            self.midi_interface = None
            self.midi_interface = MidiInterface(int(port))
            self.midi_interface.midi_in.set_callback(self.midi_interface)
        else:
            self.midi_interface = None

    def toggle(self):
        if self.running:
            print("inactive")
            self.running = False
        elif not self.running:
            print("active")
            self.running = True
            # t = threading.Thread(target=self.render)
            # t.start()
            self.process.start()
            # t = Process(target=self.render)
            # t.start()

    @staticmethod
    @njit(cache=True)
    def smooth(signal,buffer,coef_up,coef_down,fade_len):
        for i in range(0,fade_len):
            signal[i] = coef_up[i] * signal[i] + coef_down[i] * buffer[i]
        return signal


    'Если и прошлый был нажат и этот нажат, но разные ноты, то время не скидывается, а должно'
    def render_with_numba_poly(self):

        start = 0
        end = self.buffer_size

        while self.running:

            freqs = copy(self.midi_interface.currentFreq)

            if len(freqs) > 0:
                time = np.arange(start,end+self.fade_seq)
                samples = np.zeros((len(freqs),self.fade_seq+self.buffer_size))
                i = 0
                for freq in freqs:
                    samples[i] = self.synth.get_next_sample_with_numba(amplitude=0.1,
                                                                   frequency=freq,
                                                                   time=time,
                                                                   render_rate=self.sample_rate,
                                                                   pressed=True)
                    i+=1

                sample = sum(samples)
            else:
                sample = np.zeros(self.fade_seq+self.buffer_size)

            # print(max(sample))
            # sample = self.smooth(sample,self.smooth_buffer,self.coefficients,self.coefficientsR,self.fade_seq)
            self.stream.write(sample[:self.buffer_size].astype(np.float32).tostring())

            start = end
            end += self.buffer_size

            self.smooth_buffer = sample[-self.fade_seq:]


    'Если и прошлый был нажат и этот нажат, но разные ноты, то время не скидывается, а должно'
    def render_with_numba(self):

        start = 0
        end = self.buffer_size
        prev_state = False
        time_up = 0

        while self.running:
            pressed = self.midi_interface.pressed
            currentFreq = self.midi_interface.currentFreq

            if pressed != prev_state:
                if pressed:
                    start = 0
                    end = self.buffer_size
                else:
                    time_up = start

            time = np.arange(start,end)
            sample = self.synth.get_next_sample_with_numba(amplitude=0.1,
                                                           frequency=currentFreq,
                                                           time=time,
                                                           render_rate=self.sample_rate,
                                                           pressed=pressed,time_up=time_up)

            time = np.arange(end,end+self.fade_seq)
            buffer = self.synth.get_next_sample_with_numba(amplitude=0.1,
                                                           frequency=currentFreq,
                                                           time=time,
                                                           render_rate=self.sample_rate,
                                                           pressed=pressed,time_up=time_up)

            sample = self.smooth(sample,self.smooth_buffer,self.coefficients,self.coefficientsR,self.fade_seq)

            self.stream.write(sample.astype(np.float32).tostring())

            start = end
            end += self.buffer_size
            prev_state = pressed

            self.smooth_buffer = buffer

    'Если и прошлый был нажат и этот нажат, но разные ноты, то время не скидывается, а должно'
    def render(self):

        start = 0
        end = self.buffer_size
        prev_state = False
        time_up = 0

        while self.running:

            sample = np.empty(self.buffer_size)
            buffer = np.empty(self.buffer_size)

            pressed = self.midi_interface.pressed
            currentFreq = self.midi_interface.currentFreq

            if pressed != prev_state:
                if pressed:
                    start = 0
                    end = self.buffer_size
                else:
                    time_up = start

            i = 0
            time = start
            while time < end:
                sample[i] = self.synth.get_next_sample(amplitude=0.1,
                                                         frequency=currentFreq,
                                                         time=time,
                                                         pressed=pressed,time_up=time_up)
                i += 1
                time += 1

            i = 0
            time = end
            while i < self.fade_seq:
                buffer[i] = self.synth.get_next_sample(amplitude=0.1,
                                                       frequency=currentFreq,
                                                       time=time,
                                                       pressed=pressed,time_up=time_up)
                i += 1
                time += 1

            sample = self.smooth(sample,self.smooth_buffer,self.coefficients,self.coefficientsR,self.fade_seq)

            self.stream.write(sample.astype(np.float32).tostring())

            start = end
            end += self.buffer_size
            prev_state = pressed

            self.smooth_buffer = buffer

            # if pressed:
            #     currentFreq = self.midi_interface.currentFreq
            #     for t in range(start, end):
            #         sample.append(self.synth.get_next_sample(0.6,currentFreq,t))
            #     start = end
            #     end += self.buffer_size
            # else:
            #     for t in range(0, self.buffer_size):
            #         sample.append(0)
            #     start = 0
            #     end = self.buffer_size

            # self.stream.write(np.array(sample, dtype=np.float32).tostring())
