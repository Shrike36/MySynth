import rtmidi


class MidiInterface(object):
    def __init__(self, port):
        self.port = port
        self.midi_in = rtmidi.MidiIn()
        self.available_ports = self.midi_in.get_ports()
        self.notes_as_freq = self.calc_midi_freqs()
        self.midi_in.open_port(port)
        self.port_name = self.midi_in.get_port_name(port)
        self.currentFreq = 0
        self.velocity = 0
        self.pressed = False
        self.lastNote = 0

    @staticmethod
    def midi_to_freq(n):
        return 440 * 2 ** ((n - 69) / 12)

    def calc_midi_freqs(self):
        freqs = []
        for i in range(127):
            freqs.append(self.midi_to_freq(i))
        return freqs

    def __call__(self, event, data=None):
        message = event
        # print(message)
        note = message[0][1]
        note_vel = message[0][2]
        note_state = message[0][0]
        if note_state == 144:
            self.currentFreq = self.notes_as_freq[note]
            self.velocity = note_vel
            self.pressed = True
            # self.data.kb_state.state = True
            self.lastNote = note
        elif note_state == 128 and note == self.lastNote:
            self.pressed = False

        # print(message, self.data.kb_state.state, self.lastNote, note, self.currentFreq)
