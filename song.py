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



def getTicks(note):
    if note.duration == "1":
        return 16
    if note.duration == "3/4":
        return 12
    if note.duration == "1/2":
        return 8
    if note.duration == "1/4":
        return 4
    if note.duration == "1/8":
        return 2
    if note.duration == "1/16":
        return 1


time_signatures = {
    "4/4": getTicks
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

    def appendNote(self,note):
        t = time_signatures[self.time_signature](note)
        for i in range(0, t-1):
            self.append(mido.Message('note_on',note=note.getMidiNote()))
        self.append(mido.Message('note_off',note=note.getMidiNote()))

port=mido.open_output()

song = Song(tempo=200)

song.appendNote(Note("C", octave=4))
song.appendNote(Note("D#", octave=4))
song.appendNote(Note("C", octave=4))
song.appendNote(Note("D#", octave=4))
song.play()
