
class WaveAdder:
    def __init__(self,*index):
        self.indexes = index

    '0 <= index <= 1'
    def get_sum(self, samples):
        if (len(samples) > len(self.indexes)):
            samples += [0]*(len(samples)-len(self.indexes))
        res = 0
        for i in range(0,len(samples)):
            res += samples[i] * self.indexes[i]
        return res / sum(self.indexes)