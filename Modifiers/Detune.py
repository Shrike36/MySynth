from Modulators.LFO import LFO


class Detune:

    '0 <= value <= 1'
    def __init__(self, value : float):
        self.is_working = True
        self.value = value
        self.ratio = [0]
        self.counter = 0

    def set_ratio(self, count_of_oscs : int):
        minus = []
        plus = []
        max = int(count_of_oscs/2)+1
        for i in range(1,max):
            minus.append(-1/i)
            plus.append(1/(max-i))
        if not (count_of_oscs % 2 == 0):
            minus.append(0)
        self.ratio = minus + plus

    def get_next_value(self,time):
        if(self.counter >= len(self.ratio)):
            self.counter = 0
        index = self.counter
        self.counter += 1
        return self.value * self.ratio[index]

class ModulatedDetune(Detune):

    '0 <= value <= 1'
    def __init__(self, value : float, lfo : LFO, lfo_rate : float):
        super().__init__(value)
        self.lfo = lfo
        self.lfo_rate = lfo_rate

    def get_next_value(self,time):
        return super().get_next_value(time)*self.lfo.get_next_value(self.lfo_rate, time)