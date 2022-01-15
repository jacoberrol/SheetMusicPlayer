import mido
import time


class Song:
    def __init__(self, tempo):

    def do_tick( tick ):
        port.send(tick)
        time.sleep(tick_time)

    def play():
        tick = 0
        tick_time = 1
        while True:
            if tick >= len(song):
                break
            do_tick( song[tick] )
            tick += 1

port=mido.open_output('IAC Driver Bus 1')

song = []
song.append(mido.Message('note_on',note=60))
song.append(mido.Message('note_on',note=63))
song.append(mido.Message('note_off',note=60))
song.append(mido.Message('note_off',note=63))
