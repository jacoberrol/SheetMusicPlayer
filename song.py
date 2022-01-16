import mido
import time

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
        assert (pitches.__contains__(self.pitch)), f"{self.pitch} is not a valid pitch"
        assert (durations.__contains__(self.duration)), f"{self.duration} is not a valid duration"

    def getMidiNote(self):
        midi = pitches[self.pitch] + (12*self.octave)
        return midi

    def getDuration(self):
        return durations[self.duration]

    def add(self, mess):
        return mido.Message(mess, note=self.getMidiNote())

class Song:
    def __init__(self, tempo=100, time_signature="4/4"):
        self.tempo = tempo
        self.time_signature = time_signature
        self.ticks = []

    def do_tick(self,tick):
        port.send(tick)
        time.sleep(self.tick_time())

    def play(self):
        for tick in self.ticks:
            self.do_tick(tick)

    def tick_time(self):
        ts = int(self.time_signature.split("/")[1])
        return (((60*1000) / self.tempo) / (16 / ts)) / 1000

    def append(self, msg):
        self.ticks.append(msg)

port=mido.open_output()

song = Song()
song.append(Note("C", octave=4).add('note_on'))
song.append(Note("D#", octave=4).add('note_on'))
song.append(Note("C", octave=4).add('note_off'))
song.append(Note("D#", octave=4).add('note_off'))
song.play()