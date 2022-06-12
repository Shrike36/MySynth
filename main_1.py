import rtmidi

from Controller.Controller import Controller
from Modifiers.Detune import Detune, ModulatedDetune
from Modifiers.WaveAdder import WaveAdder as wa, WaveAdder
from Modifiers.Panner import StereoPanner as sp, StereoPanner, ModulatedPanner
from Modulation.ParamsModulation import LFOModulation, ModulationType
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.ModulatedOscillator import ModulatedOscillator
from Oscillators.Oscillator import Oscillator, Type
from Oscillators.WaveGenerator import WaveGenerator
from Synth.Synth import Synth

A_c = 5#float(input('Enter carrier amplitude: '))
f_c = 25#float(input('Enter carrier frquency: '))
A_m = 5#float(input('Enter message amplitude: '))
f_m = 1#float(input('Enter message frquency: '))
modulation_index = 6#float(input('Enter modulation index: '))

render_rate = 30000

print('done')

wave_generator = WaveGenerator(render_rate)

lfo_1 = LFO(Oscillator(Type.sine,wave_generator,render_rate))

envelope_1 = Envelope(0.3,0.2,3.8,0.9,0.8,render_rate)

modulation_1 = LFOModulation(ModulationType.fm)

detune_1 = Detune(1/16)
detune_2 = ModulatedDetune(1/4,lfo_1,2)

wave_adder_1 = WaveAdder(1,1,0.5)

panner_1 = StereoPanner(0.3)
panner_2 = ModulatedPanner(0.2,lfo_1,4)

base_oscillator_1 = Oscillator(Type.sawtooth,wave_generator,render_rate)
base_oscillator_2 = Oscillator(Type.sine,wave_generator,render_rate)
modulated_oscillator = ModulatedOscillator(Type.triangle,wave_generator,lfo_1,3,envelope_1,modulation_1,1,render_rate)

synth = Synth(modulated_oscillator,modulated_oscillator,
              detune=detune_1,
              wave_adder=wave_adder_1,
              stereo_panner=panner_2,
              render_rate=render_rate,
              stereo=False)


midi_in = rtmidi.MidiIn()

def midi_info():
    print("Available MIDI ports:\n")
    available_ports = midi_in.get_ports()
    for i in range(len(available_ports)):
        print("[", i, "]", available_ports[i])
    print("\nPlease select port of a MIDI device:")

def run_synth_no_gui(synth):
    port = None
    while not isinstance(port, int):
        midi_info()
        port = input()
        try:
            port = int(port)
        except ValueError:
            print("Port need to be a number!\n")

    controller = Controller(synth=synth,sample_rate=render_rate)
    controller.change_midi_port(port, midi_in.get_port_count())
    controller.toggle()


run_synth_no_gui(synth)



