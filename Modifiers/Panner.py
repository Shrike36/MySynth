
class StereoPanner:

    '0 <= index <= 1'
    @staticmethod
    def get_stereo_sample(sample, index=0):
        # stereo_sample = [(1+index)*sample,(1-index)*sample]
        # left_sample = (1+index)*sample
        # right_sample = (1-index)*sample
        # stereo_sample.append(left_sample)
        # stereo_sample.append(right_sample)
        return [(1-index)*sample, index*sample]