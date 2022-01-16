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
    "B#": 24,
}

durations = [
    "1",
    "1/2",
    "3/4",
    "1/4",
    "1/8",
    "1/16"
]

def getTicks(note):
    if note.duration == "1":
        return 32
    if note.duration == "3/4":
        return 24
    if note.duration == "1/2":
        return 16
    if note.duration == "1/4":
        return 8
    if note.duration == "1/8":
        return 4
    if note.duration == "1/16":
        return 2


time_signatures = {
    "4/4": getTicks
}

class Rest:
    def __init__(self, duration="1/4"):
        self.duration = duration
        assert (durations.__contains__(self.duration)), f"{self.duration} is not a valid duration"

    def getDuration(self):
        return durations[self.duration]

    def getMidiMessage(self, msg):
        return None

class Note(Rest):
    def __init__(self, pitch="C", duration="1/4", octave=3):
        super(Note,self).__init__(duration)
        self.pitch = pitch
        self.octave = octave
        assert (self.getMidiNote() >= 0), "Note out of range, (0-127)"
        assert (self.getMidiNote() <= 127), "Note out of range, (0-127)"
        assert (pitches.__contains__(self.pitch)), f"{self.pitch} is not a valid pitch"

    def getMidiNote(self):
        midi = pitches[self.pitch] + (12 * self.octave)
        return midi

    def getMidiMessage(self, msg):
        return mido.Message(msg,note=self.getMidiNote())

class Song:
    def __init__(self, tempo=100, time_signature="4/4"):
        self.tempo = tempo
        self.time_signature = time_signature
        self.ticks = []

    def do_tick(self,tick):
        port.send(tick)

    def play(self):
        for tick in self.ticks:
            if tick is not None:
                self.do_tick(tick)
            time.sleep(self.tick_time())

    def tick_time(self):
        ts = int(self.time_signature.split("/")[1])
        return (((60*1000) / self.tempo) / (32 / ts)) / 1000

    def append(self, msg):
        self.ticks.append(msg)

    def appendNote(self,note):
        t = time_signatures[self.time_signature](note)
        for i in range(0, t-1):
            if i == 0:
                self.append(note.getMidiMessage('note_on'))
            else:
                self.append(None)
        self.append(note.getMidiMessage('note_off'))

port=mido.open_output()

song = Song(tempo=100)

song.appendNote(Note("C", octave=4, duration="1/4"))
song.appendNote(Note("D#", octave=4, duration="1/4"))
song.appendNote(Note("C", octave=4, duration="1/8"))
song.appendNote(Note("C", octave=4, duration="1/8"))
song.appendNote(Rest(duration="3/4"))
song.appendNote(Note("C", octave=4, duration="1/4"))

song.play()
