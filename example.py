from machine import Pin
from time import sleep

pin = Pin("LED", Pin.OUT)
D = 0.1
DAA = 0.4
PAUSE = 0.6

def encode(msg):
    morse = {
        'a': [D, DAA], 'b': [DAA, D, D, D], 'c': [DAA, D, DAA, D], 'd': [DAA, D, D],
        'e': [D], 'f': [D, D, DAA, D], 'g': [DAA, DAA, D], 'h': [D, D, D, D], 'i': [D, D],
        'j': [D, DAA, DAA, DAA], 'k': [DAA, D, DAA], 'l': [D, DAA, D, D], 'm': [DAA, DAA],
        'n': [DAA, D], 'o': [DAA, DAA, DAA], 'p': [D, DAA, DAA, D], 'q': [DAA, DAA, D, DAA],
        'r': [D, DAA, D], 's': [D, D, D], 't': [DAA], 'u': [D, D, DAA], 'v': [D, D, D, DAA],
        'w': [D, DAA, DAA], 'x': [DAA, D, D, DAA], 'y': [DAA, D, DAA, DAA], 'z': [DAA, DAA, D, D],
         '1': [D, DAA, DAA, DAA, DAA], '2': [D, D, DAA, DAA, DAA], '3': [D, D, D, DAA, DAA], 
         '4': [D, D, D, D, DAA], '5': [D, D, D, D, D], '6': [DAA, D, D, D, D], 
         '7': [DAA, DAA, D, D, D], '8': [DAA, DAA, DAA, D, D],  '9': [DAA, DAA, DAA, DAA, D], 
         '0': [DAA, DAA, DAA, DAA, DAA],
    }
    return [morse[c.lower()] for c in msg]

def pin_morsecode(pin, morsecode):
    pin.off()
    for letter in morsecode:
        for duration in letter:
            pin.toggle()
            sleep(duration)
            pin.toggle()
            sleep(PAUSE-duration)
        sleep(PAUSE)


pin_morsecode(pin, encode('sos'))
