import mido
import time

from file import Note


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