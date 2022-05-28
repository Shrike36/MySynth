class LFO():
    def __init__(self, osc, index):
        self.lfo_osc = osc
        self.index = index

    def get_next_value(self,frequency,time):
        return self.index * self.lfo_osc.get_next_sample(1,frequency,time)

    def set_time_to_null(self):
        self.lfo_osc.set_time_to_null()