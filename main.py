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
import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time

#Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
#Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
#Modulated wave s(t)=A_c[1+mu*cos(2*pi*f_m*t)]cos(2*pi*f_c*t)
from Modulation.Modulation import Modulation
from Modulators.Envelope import Envelope
from Modulators.LFO import LFO
from Oscillators.BaseOscillator import BaseOscillator
from Oscillators.SawtoothOscillator import SawtoothOscillator
from Oscillators.SineOscillator import SineOscillator
from Oscillators.SquareOscillator import SquareOscillator
from Oscillators.TriangleOscillator import TriangleOscillator

A_c = 5#float(input('Enter carrier amplitude: '))
f_c = 440#float(input('Enter carrier frquency: '))
A_m = 5#float(input('Enter message amplitude: '))
f_m = 2#float(input('Enter message frquency: '))
modulation_index = 140#float(input('Enter modulation index: '))

sample_rate = 22000

print('done')
lfo = LFO(SquareOscillator(f_m, A_m, sample_rate),modulation_index)
oscillator = SineOscillator(f_c, A_c, sample_rate)
carrier2 = SineOscillator(523.36,A_c,sample_rate)
envelope = Envelope(0.3,0.2,0.8,0.9,1,sample_rate)
print('done')

osc = []
car2 = []
lfo_1 = []
env = []
arr = []
for t in range(0,10*sample_rate):
    osc.append(oscillator.get_next_value(t))
    car2.append(carrier2.get_next_value(t))
    lfo_1.append(lfo.get_next_value(t))
    env.append(envelope.get_next_value(t))
    arr.append(np.cos(2*np.pi*f_c*t/(sample_rate)))

print('done')

oscillator.set_time_to_null()
lfo.set_time_to_null()
envelope.set_time_to_null()

oscillator2=SineOscillator(523.36,A_c,sample_rate)
lfo2=LFO(SquareOscillator(f_m, A_m, sample_rate),1)
envelope2 = Envelope(0.3,0.2,0.8,0.9,1,sample_rate)


product_am = []
product_am2 = []
product_fm = []

t1 = time.time()
for t in range(0,10*sample_rate):
    oscillator_next = oscillator.get_next_value(t)
    lfo_next = lfo.get_next_value(t)
    env_next = envelope.get_next_value(t)

    oscillator2_next = oscillator2.get_next_value(t)
    lfo2_next = lfo2.get_next_value(t)
    env2_next = envelope2.get_next_value(t)

    # product_am.append((1 + modulation_index*modulator_next/A_m)*carrier_next)

    product_am.append(Modulation.am_lfo_modulation(oscillator_next, lfo_next, lfo.index))
    product_am[t] = Modulation.am_envelope_modulation(product_am[t],env_next)

    product_am2.append(Modulation.am_lfo_modulation(oscillator2_next, lfo2_next, lfo2.index))
    product_am2[t] = Modulation.am_envelope_modulation(product_am2[t],env2_next)

    # time = np.linspace(0,int(carrier.sample_rate/carrier_next.frequency),int(self.sample_rate/self.frequency))
    # product_fm.append(np.cos(2*np.pi*f_c*t + modulation_index*lfo_next/A_m))
    product_fm.append(Modulation.pm_lfo_modulation(oscillator,lfo_next,lfo.index,t,sample_rate))
print(" Total time taken is :", time.time() - t1)
print('done')

# carrier = A_c*np.cos(2*np.pi*f_c*t)
# for i in range(0,len(carrier)):
#     if carrier[i] < 0:
#         carrier[i] = -1
#     else:
#         carrier[i] = 1
# modulator = A_m*np.cos(2*np.pi*f_m*t)
# for i in range(0,len(modulator)):
#     if modulator[i] < 0:
#         modulator[i] = -1
#     else:
#         modulator[i] = 1
product = A_c*(1+modulation_index*np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_c*t)
# product_fm = np.cos(2 *np.pi*f_c*t + modulation_index*modulator/A_m)
# for i in range(0,len(product_fm)):
#     if product_fm[i] < 0:
#         product_fm[i] = -1
#     else:
#         product_fm[i] = 1
# product_am = (1 + modulation_index*modulator/A_m)*carrier

plt.subplot(4,1,1)
plt.title('Amplitude Modulation')
plt.plot(lfo_1, 'g')
plt.ylabel('Amplitude')
plt.xlabel('LFO signal')

plt.subplot(4,1,2)
plt.plot(osc, 'r')
plt.ylabel('Amplitude')
plt.xlabel('Oscillator signal')

plt.subplot(4,1,3)
plt.plot(env, color="purple")
plt.ylabel('Amplitude')
plt.xlabel('Envelope')

plt.subplot(4,1,4)
plt.plot(product_fm, color="purple")
plt.ylabel('Amplitude')
plt.xlabel('AM signal')

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

    wavfile.write(fname, sample_rate, wav)

# wave_to_file(product_am,product_am2, fname="c_maj7.wav")

plt.show()

fig.savefig('Amplitude Modulation.png', dpi=100)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
