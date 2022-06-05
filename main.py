# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import math
# import librosa
# import itertools
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# def plot(xy, r=1,c=1,i=1,title="", xlabel="",ylabel="",yticks=None, xticks=None,**plot_kwargs):
#     plt.subplot(r,c,i)
#     plt.title(title)
#     if len(xy) == 2:
#         plt.plot(*xy, **plot_kwargs)
#     else:
#         plt.plot(xy, **plot_kwargs)
#
#     if xticks is not None: plt.xticks(xticks)
#     if yticks is not None: plt.yticks(yticks)
#     plt.ylabel(ylabel)
#     plt.xlabel(xlabel)
#
# class SineOscillator():
#     def __init__(self, freq):
#         self.freq = freq
#
#     def gatValue(self, t):
#         return math.sin(math.radians(2*math.pi*self.freq*t))
#
# class LFO():
#     def getValueAm(self, osc, lfo, t):
#         return osc.gatValue(t)*lfo.gatValue(t)
#
# osc = SineOscillator(10)
# lfo = SineOscillator(2)
# mod = LFO()
# values_osc = []
# values_lfo = []
# values_mod = []
#
# for t in range (0,5000):
#     values_osc.append(osc.gatValue(t))
#     values_lfo.append(lfo.gatValue(t))
#     values_mod.append(mod.getValueAm(osc,lfo,t))
#
# fig = plt.figure(figsize=(8*2,4*2))
#
# plot(values_osc, label=f"Sine Wave", xlabel="samples", ylabel="amplitude")
# plot(values_lfo, label=f"Sine Wave", xlabel="samples", ylabel="amplitude")
# plot(values_mod, label=f"Sine Wave", xlabel="samples", ylabel="amplitude")
#
# plt.legend(loc='lower right')
# plt.show()
# fig.savefig("sine.jpg")

import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from scipy import interpolate
from scipy.interpolate import interp1d
from scipy.io import wavfile
import time

from Modifiers.Detune import Detune, ModulatedDetune
from Modifiers.WaveAdder import WaveAdder as wa, WaveAdder
from Modifiers.Panner import StereoPanner as sp, StereoPanner, ModulatedPanner
from Modulation.ParamsModulation import LFOModulation, ModulationType
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.ModulatedOscillator import ModulatedOscillator
from Oscillators.Oscillator import Oscillator, Type
from pygame import midi
import pyaudio
#Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
#Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
#Modulated wave s(t)=A_c[1+mu*cos(2*pi*f_m*t)]cos(2*pi*f_c*t)
from Oscillators.WaveGenerator import WaveGenerator
from Synth.Synth import Synth

A_c = 5#float(input('Enter carrier amplitude: '))
f_c = 25#float(input('Enter carrier frquency: '))
A_m = 5#float(input('Enter message amplitude: '))
f_m = 1#float(input('Enter message frquency: '))
modulation_index = 6#float(input('Enter modulation index: '))

render_rate = 18000
sample_rate = 18000
buffer = 2048

print('done')

wave_generator = WaveGenerator(render_rate)

lfo_1 = LFO(Oscillator(Type.sawtooth,wave_generator,render_rate))

envelope_1 = Envelope(0.3,0.8,3.8,3.9,0.5,render_rate)

modulation_1 = LFOModulation(ModulationType.fm)

detune_1 = Detune(1/4)
detune_2 = ModulatedDetune(1/4,lfo_1,2)

wave_adder_1 = WaveAdder(1,1)

panner_1 = StereoPanner(0.3)
panner_2 = ModulatedPanner(0.2,lfo_1,4)

base_oscillator_1 = Oscillator(Type.sawtooth,wave_generator,render_rate)
base_oscillator_2 = Oscillator(Type.sine,wave_generator,render_rate)
modulated_oscillator = ModulatedOscillator(Type.sine,wave_generator,lfo_1,3,envelope_1,modulation_1,1,render_rate)

synth = Synth(modulated_oscillator,
              detune=detune_1,
              wave_adder=wave_adder_1,
              stereo_panner=panner_1,
              render_rate=render_rate,
              stereo=True)
print('done')

# midi.init()
# if midi.get_count() > 0:
#     midi_input = midi.Input(1)
# else:
#     raise Exception("no midi devices detected")

stream = pyaudio.PyAudio().open(
    rate=sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    output=True,
    frames_per_buffer=buffer
)

def interpolate(samples):
    new_arr = []
    new_arr.append(samples[0])
    for i in range(0,len(samples)-1):
        el_1 = samples[i]
        el_2 = samples[i+1]
        new_arr.append((el_1+el_2)/2)
        new_arr.append(el_2)
    new_arr.append(el_2)
    return new_arr

def get_samples(time):
    # Return samples in int16 format
    samples = []
    new_buf_size = int(buffer*(render_rate/sample_rate))
    a = int(sample_rate/render_rate)
    for _ in range(0,new_buf_size):
        n_s = synth.get_next_sample(2,440,time)
        # for _ in range(0,a):
        #     samples.append(
        #         n_s
        #     )
        samples.append(
            n_s
        )
        time += 1

    # samples = interpolate(samples)

    # x = np.linspace(0,new_buf_size-1,new_buf_size)
    # f = interp1d(x, samples, kind = 'linear')
    #
    # xnew = np.linspace(0,new_buf_size-1,new_buf_size*int(sample_rate/render_rate))
    #
    # samples = f(xnew)

    return change_samples(samples), time

@njit()
def change_samples(samples = np.array([])):
    samples = np.array(samples) * 0.3
    samples = samples.clip(-0.8, 0.8) * 32767
    samples = samples.astype(np.int16)
    samples = samples.reshape(buffer, -1)
    return samples

time = 0
while True:
    samples, time = get_samples(time)
    stream.write(samples.tobytes())

#
#
# base_oscillator_3 = Oscillator(Type.sine,render_rate)
# base_oscillator_4 = Oscillator(Type.square,render_rate)
# base_oscillator_5 = Oscillator(Type.sawtooth,render_rate)
# base_oscillator_6 = Oscillator(Type.triangle,render_rate)


arr1 = []
arr2 = []
arr3 = []
arr4 = []
sum = []
ch1 = []
ch2 = []

t1 = time.time()
for t in range(0,int(10*render_rate)):
    sm = synth.get_next_sample(10,8,t)
    # arr1.append(base_oscillator_1.get_next_sample(10,6,t))
    # arr2.append(base_oscillator_2.get_next_sample(10,8,t))

    # arr1.append(modulated_oscillator.wave_generator.waves[3][t])
    arr2.append(lfo_1.get_next_integral(3,t))
    sum.append(sm)
    # ch1.append(ster[0])
    # ch2.append(ster[1])

# for t in range(0,int(10*render_rate)):
#     arr1.append(base_oscillator_3.get_next_sample(10,5,t))
#     arr2.append(base_oscillator_4.get_next_sample(10,5,t))
#     arr3.append(base_oscillator_5.get_next_sample(10,5,t))
#     arr4.append(base_oscillator_6.get_next_sample(10,5,t))
#     # ch1.append(ster[0])
#     # ch2.append(ster[1])

# for t in range(0,int(0.5*render_rate)):
#     osc,sm,ster = synth.get_next_sample(10,880,t)
#     arr1.append(osc[0])
#     arr2.append(osc[1])
#     sum.append(sm)
#     ch1.append(ster[0])
#     ch2.append(ster[1])
#
# for t in range(0,int(0.5*render_rate)):
#     osc,sm,ster = synth.get_next_sample(10,987.78,t)
#     arr1.append(osc[0])
#     arr2.append(osc[1])
#     sum.append(sm)
#     ch1.append(ster[0])
#     ch2.append(ster[1])
#
# for t in range(0,int(0.75*render_rate)):
#     osc,sm,ster = synth.get_next_sample(10,587.32,t)
#     arr1.append(osc[0])
#     arr2.append(osc[1])
#     sum.append(sm)
#     ch1.append(ster[0])
#     ch2.append(ster[1])
#
# for t in range(0,int(0.25*render_rate)):
#     osc,sm,ster = synth.get_next_sample(10,0.1,t)
#     arr1.append(osc[0])
#     arr2.append(osc[1])
#     sum.append(sm)
#     ch1.append(ster[0])
#     ch2.append(ster[1])
#
# for t in range(0,int(0.5*render_rate)):
#     osc,sm,ster = synth.get_next_sample(10,987.78,t)
#     arr1.append(osc[0])
#     arr2.append(osc[1])
#     sum.append(sm)
#     ch1.append(ster[0])
#     ch2.append(ster[1])
#
# for t in range(0,int(0.25*render_rate)):
#     osc,sm,ster = synth.get_next_sample(10,880,t)
#     arr1.append(osc[0])
#     arr2.append(osc[1])
#     sum.append(sm)
#     ch1.append(ster[0])
#     ch2.append(ster[1])
#
# for t in range(0,int(0.25*render_rate)):
#     osc,sm,ster = synth.get_next_sample(10,784,t)
#     arr1.append(osc[0])
#     arr2.append(osc[1])
#     sum.append(sm)
#     ch1.append(ster[0])
#     ch2.append(ster[1])
#
# for t in range(0,int(0.75*render_rate)):
#     osc,sm,ster = synth.get_next_sample(10,739.98,t)
#     arr1.append(osc[0])
#     arr2.append(osc[1])
#     sum.append(sm)
#     ch1.append(ster[0])
#     ch2.append(ster[1])

print(" Total time taken is :", time.time() - t1)


plt.subplot(3,1,1)
plt.title('Summator')
plt.plot(arr1, 'g')
plt.ylabel('Amplitude')
plt.xlabel('osc 1')

plt.subplot(3,1,2)
plt.plot(arr2, 'r')
plt.ylabel('Amplitude')
plt.xlabel('osc 2')

plt.subplot(3,1,3)
plt.plot(sum, color="purple")
plt.ylabel('Amplitude')
plt.xlabel('Sum')
#
# plt.subplot(4,1,4)
# plt.plot(arr4, color="purple")
# plt.ylabel('Amplitude')
# plt.xlabel('Triangle')
#
# plt.subplot(5,1,5)
# plt.plot(ch2, color="purple")
# plt.ylabel('Amplitude')
# plt.xlabel('chanel 2')

plt.subplots_adjust(hspace=1)
plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(16, 9)

to_16 = lambda wav, amp: np.int16(wav * amp * (2**15 - 1))
def wave_to_file(wav, wav2=None, fname="temp.wav", amp=0.01):
    wav = np.array(wav)
    wav = to_16(wav, amp)
    if wav2 is not None:
        wav2 = np.array(wav2)
        wav2 = to_16(wav2, amp)
        wav = np.stack([wav, wav2]).T

    wavfile.write(fname, render_rate, wav)

wave_to_file(sum, fname="c_maj7.wav")

plt.show()

# fig.savefig('Amplitude Modulation.png', dpi=100)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
