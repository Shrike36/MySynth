import threading
import pyaudio
from Controller.midi import MidiInterface
import numpy as np
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

        self.synth = synth

        self.running = False
        self.pressed = False

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
            t = threading.Thread(target=self.render)
            t.start()


    'Если и прошлый был нажат и этот нажат, но разные ноты, то время не скидывается, а должно'
    def render(self):

        start = 0
        end = self.buffer_size
        prev_state = False
        time_up = 0

        while self.running:

            sample = []

            pressed = self.midi_interface.pressed
            currentFreq = self.midi_interface.currentFreq

            if pressed != prev_state:
                if pressed:
                    start = 0
                    end = self.buffer_size
                else:
                    time_up = start

            for t in range(start, end):
                sample.append(self.synth.get_next_sample(amplitude=0.6,
                                                         frequency=currentFreq,
                                                         time=t,
                                                         pressed=pressed,time_up=time_up))

            self.stream.write(np.array(sample, dtype=np.float32).tostring())

            start = end
            end += self.buffer_size
            prev_state = pressed

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
