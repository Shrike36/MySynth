
class WaveAdder:

    '0 <= index <= 1'
    @staticmethod
    def get_sum(first_sample, second_sample, index=0):
        return ((1-index)*first_sample + index*second_sample)