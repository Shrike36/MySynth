from Modulation.ParamsModulation import ModulationType
from Oscillators.Oscillator import Type


class SynthParams:
    def __init__(self):

        self.detune_index = 0
        self.detune_is_working = True

        self.osc_1_type = Type.sine.value
        self.osc_1_is_working = True
        self.mod_1_is_working = True
        self.mod_1_type = ModulationType.am.value
        self.mod_1_index = 1
        self.lfo_1_type = Type.sine.value
        self.lfo_1_frequency = 1

        self.osc_2_type = Type.sine.value
        self.osc_2_is_working = True
        self.mod_2_is_working = True
        self.mod_2_type = ModulationType.am.value
        self.mod_2_index = 1
        self.lfo_2_type = Type.sine.value
        self.lfo_2_frequency = 1

        self.osc_1_adder_index = 1
        self.osc_2_adder_index = 1

        self.panner_index = 0.8
        self.panner_is_working = True
        self.panner_modulation_is_working = True
        self.lfo_panner_type = Type.sine.value
        self.lfo_panner_frequency = 1


