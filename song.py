import mido
import time

class Rest:

    durations = [
        "1",
        "15/16",
        "7/8",
        "13/16",
        "3/4",
        "11/16",
        "5/8",
        "9/16",
        "1/2",
        "7/16",
        "3/8",
        "5/16",
        "1/4",
        "3/16",
        "1/8",
        "1/16",
        "1/3",
        "1/6",
        "1/12",
        "1/24"
    ]

    def __init__(self, duration="1/4"):
        self.duration = duration
        assert (Rest.durations.__contains__(self.duration)), f"{self.duration} is not a valid duration"

    def getMidiMessage(self, msg):
        return None

class Note(Rest):

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

    def __init__(self, pitch="C", duration="1/4", octave=3):
        super(Note,self).__init__(duration)
        self.pitch = pitch
        self.octave = octave
        assert (self.getMidiNote() >= 0), "Note out of range, (0-127)"
        assert (self.getMidiNote() <= 127), "Note out of range, (0-127)"
        assert (Note.pitches.__contains__(self.pitch)), f"{self.pitch} is not a valid pitch"

    def getMidiNote(self):
        midi = Note.pitches[self.pitch] + (12 * self.octave)
        return midi

    def getMidiMessage(self, msg):
        return mido.Message(msg,note=self.getMidiNote())

class Song:

    def __getTicks__(note):
        if note.duration == "1":
            return (32 * 3)
        if note.duration == "15/16":
            return (30 * 3)
        if note.duration == "7/8":
            return (28 * 3)
        if note.duration == "13/16":
            return (26 * 3)
        if note.duration == "3/4":
            return (24 * 3)
        if note.duration == "11/16":
            return (22 * 3)
        if note.duration == "5/8":
            return (20 * 3)
        if note.duration == "9/16":
            return (18 * 3)
        if note.duration == "1/2":
            return (16 * 3)
        if note.duration == "7/16":
            return (14 * 3)
        if note.duration == "3/8":
            return (12 * 3)
        if note.duration == "5/16":
            return (10 * 3)
        if note.duration == "1/4":
            return (8 * 3)
        if note.duration == "3/16":
            return (6 * 3)
        if note.duration == "1/8":
            return (4 * 3)
        if note.duration == "1/16":
            return (2 * 3)
        if note.duration == "1/3":
            return 32
        if note.duration == "1/6":
            return 16
        if note.duration == "1/12":
            return 8
        if note.duration == "1/24":
            return 4


    time_signatures = {
        "4/4": __getTicks__
    }

    def __init__(self, tempo=100, time_signature="4/4", voices: int = 16):
        assert(Song.time_signatures.__contains__(time_signature)), f"{time_signature} is not a valid time signature"
        self.port=mido.open_output()
        self.tempo = tempo
        self.time_signature = time_signature
        self.ticks = []
        for i in range(0,voices):
            self.ticks.append([])

    def do_tick(self,tick):
        self.port.send(tick)

    def play(self):
        tick_pos = 0
        while True:
            #print(f"While >> Tick_Pos: {tick_pos}")
            played = 0
            for tick in self.ticks:
                #print(f"For >> Len: {len(tick)}")
                if len(tick) > tick_pos:
                    if tick[tick_pos] is not None:
                        #print(f"If >> Pitch {tick[tick_pos]}")
                        self.do_tick(tick[tick_pos])
                    #else:
                        #print(f"If >> None")
                    played += 1
            tick_pos += 1
            if played == 0: break
            time.sleep(self.tick_time())

    # this function returns the amount of time in one tick of the song
    # in order to support fractional note durations down to 1/16 notes
    # and triplet 1/4, 1/8, and 1/16 notes we assign 96 ticks to a
    # whole note
    def tick_time(self):
        # get the denominator of the time signature (note that gets the beat)
        ts = int(self.time_signature.split("/")[1])
        beat = f"1/{ts}"
        tpb = Song.time_signatures[self.time_signature](Rest(beat))
        # calculate ms/beat (tempo is in bpm) (60K ms/min) / (X beats/min)
        mspb = (60*1000) / self.tempo
        # produces a decimal value seconds/tick
        spt = mspb / (tpb) / 1000
        return spt

    def append(self, msg, voice: int = 0):
        self.ticks[voice].append(msg)

    def appendNote(self,note, voice: int = 0):
        t = Song.time_signatures[self.time_signature](note)
        for i in range(0, t-1):
            if i == 0:
                self.append(note.getMidiMessage('note_on'), voice=voice)
            else:
                self.append(None, voice=voice)
        self.append(note.getMidiMessage('note_off'), voice=voice)

def test():

    song = Song(tempo=100)

    song.appendNote(Note("C", octave=4, duration="1/4"))
    song.appendNote(Note("D#", octave=4, duration="1/4"))
    song.appendNote(Note("C", octave=4, duration="1/8"))
    song.appendNote(Note("C", octave=4, duration="1/8"))
    song.appendNote(Rest(duration="1/8"))
    song.appendNote(Note("C", octave=4, duration="1/16"))
    song.appendNote(Note("C", octave=4, duration="1/16"))
    song.appendNote(Note("C", octave=4, duration="1/4"))
    song.appendNote(Note("D#", octave=4, duration="1/4"))
    song.appendNote(Note("C", octave=4, duration="1/8"))
    song.appendNote(Note("C", octave=4, duration="1/8"))

    song.appendNote(Note("E", octave=4, duration="1/4"), 1)
    song.appendNote(Note("G", octave=4, duration="1/4"), 1)
    song.appendNote(Note("E", octave=4, duration="1/8"), 1)
    song.appendNote(Note("E", octave=4, duration="1/8"), 1)
    song.appendNote(Rest(duration="1/8"), 1)
    song.appendNote(Note("E", octave=4, duration="1/16"), 1)
    song.appendNote(Note("E", octave=4, duration="1/16"), 1)
    song.appendNote(Note("E", octave=4, duration="1/4"), 1)
    song.appendNote(Note("G", octave=4, duration="1/4"), 1)
    song.appendNote(Note("E", octave=4, duration="1/8"), 1)
    song.appendNote(Note("E", octave=4, duration="1/8"), 1)

    song.play()

# test()
