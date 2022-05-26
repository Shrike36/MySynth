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

#Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
#Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
#Modulated wave s(t)=A_c[1+mu*cos(2*pi*f_m*t)]cos(2*pi*f_c*t)
from Oscillators.BaseOscillator import BaseOscillator
from Oscillators.SawtoothOscillator import SawtoothOscillator
from Oscillators.SineOscillator import SineOscillator
from Oscillators.SquareOscillator import SquareOscillator
from Oscillators.TriangleOscillator import TriangleOscillator

A_c = 5#float(input('Enter carrier amplitude: '))
f_c = 440#float(input('Enter carrier frquency: '))
A_m = 5#float(input('Enter message amplitude: '))
f_m = 2#float(input('Enter message frquency: '))
modulation_index = 3#float(input('Enter modulation index: '))

sample_rate = 44100

modulator = SineOscillator(f_m,A_m,sample_rate)
carrier = SineOscillator(f_c,A_c,sample_rate)
carrier2 = SineOscillator(523.36,A_c*2,sample_rate)

car = []
car2 = []
mod = []
for t in range(0,10*sample_rate):
    car.append(carrier.getNextValue())
    car2.append(carrier2.getNextValue())
    mod.append(modulator.getNextValue())

carrier.setTimeToNull()
modulator.setTimeToNull()

product_am = []
product_fm = []
for t in range(0,10*sample_rate):
    carrier_next = carrier.getNextValue()
    modulator_next = modulator.getNextValue()
    product_am.append((1 + modulation_index*modulator_next/A_m)*carrier_next)
    # time = np.linspace(0,int(carrier.sample_rate/carrier_next.frequency),int(self.sample_rate/self.frequency))
    product_fm.append(np.cos(2 *np.pi*f_c*t + modulation_index*modulator_next/A_m))

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

plt.subplot(3,1,1)
plt.title('Amplitude Modulation')
plt.plot(mod,'g')
plt.ylabel('Amplitude')
plt.xlabel('Message signal')

plt.subplot(3,1,2)
plt.plot(car, 'r')
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(3,1,3)
plt.plot(product_am, color="purple")
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

wave_to_file(product_am,car2, fname="c_maj7.wav")

plt.show()

fig.savefig('Amplitude Modulation.png', dpi=100)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
