

class Modulation:
    @staticmethod
    def am_lfo_modulation(osc_val,mod_val,mod_index):
        return (1+mod_val)*osc_val/(int(mod_index)+1)

    @staticmethod
    def am_envelope_modulation(osc_val,mod_val):
        return mod_val*osc_val