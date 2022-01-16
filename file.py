import mido

pitches = {
    "Cb": 11,
    "C": 12,
    "C#": 13,
    "Db": 13,
    "D": 14,
    "D#": 15,
    "Eb": 15,
    "E": 16,
    "E#": 17,
    "Fb": 16,
    "F": 17,
    "F#": 18,
    "Gb": 18,
    "G": 19,
    "G#": 20,
    "Ab": 20,
    "A": 21,
    "A#": 22,
    "Bb": 22,
    "B": 23,
    "B#": 24
}

durations = {
    "1": 1,
    "1/2": .5,
    "3/4": .75,
    "1/4": .25,
    "1/8": .125,
    "1/16": .0625
}

class Note:
    def __init__(self, pitch="C", duration="1/4", octave=3):
        self.pitch = pitch
        self.duration = duration
        self.octave = octave
        assert (self.getMidiNote() >= 0), "Note out of range, (0-127)"
        assert (self.getMidiNote() <= 127), "Note out of range, (0-127)"
        assert (pitches.__contains__(self.pitch)), f"{self.pitch} is not a valid note"
        assert (self.pitch != "Cb" and self.octave != -1), "C is the lowest in octave -1"

    def getMidiNote(self):
        midi = pitches[self.pitch] + (12*self.octave)
        return midi

    def getDuration(self):
        return durations[self.duration]

    def add(self, mess):
        return mido.Message(mess, note=self.getMidiNote())
