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
from scipy.io import wavfile
import time
from Modifiers.WaveAdder import WaveAdder as wa
from Modifiers.Panner import StereoPanner as sp
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.Oscillator import Oscillator, Type

#Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
#Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
#Modulated wave s(t)=A_c[1+mu*cos(2*pi*f_m*t)]cos(2*pi*f_c*t)
from Synth.Synth import Synth

A_c = 5#float(input('Enter carrier amplitude: '))
f_c = 25#float(input('Enter carrier frquency: '))
A_m = 5#float(input('Enter message amplitude: '))
f_m = 1#float(input('Enter message frquency: '))
modulation_index = 6#float(input('Enter modulation index: '))

render_rate = 20000

print('done')
synth = Synth(render_rate,True)
print('done')

arr1 = []
arr2 = []
sum = []

t1 = time.time()
for t in range(0,10*render_rate):
    osc1, osc2, wave = synth.get_next_sample(10,440,t)
    arr1.append(osc1)
    arr2.append(osc2)
    sum.append(wave)

print(" Total time taken is :", time.time() - t1)


plt.subplot(4,1,1)
plt.title('Amplitude Modulation')
plt.plot(arr1, 'g')
plt.ylabel('Amplitude')
plt.xlabel('Osc1 signal')

plt.subplot(4,1,2)
plt.plot(arr2, 'r')
plt.ylabel('Amplitude')
plt.xlabel('LFO1 signal')

plt.subplot(4,1,3)
plt.plot(sum, color="purple")
plt.ylabel('Amplitude')
plt.xlabel('am')
#
# plt.subplot(4,1,4)
# plt.plot(stereo_r, color="purple")
# plt.ylabel('Amplitude')
# plt.xlabel('am')

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

fig.savefig('Amplitude Modulation.png', dpi=100)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
