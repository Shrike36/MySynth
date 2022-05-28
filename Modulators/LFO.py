class LFO():
    def __init__(self, osc):
        self.lfo_osc = osc

    def get_next_value(self,frequency,time):
        return self.lfo_osc.get_next_sample(1,frequency,time)