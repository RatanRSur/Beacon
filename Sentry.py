from datetime import datetime
from pygame import mixer
from collections import deque

interruption='sounds/interruption.ogg' 

class Ambience:
    def __init__(self):
        self.noiseArray = deque()
        self.noisiness = 0
        self.isNight = False
    #def sample(self):
        #self.noiseArray.

class Speaker:
    def __init__(self):
        mixer.init()
        self.track = interruption
        mixer.music.load(self.track)
        self.volume = 0
        mixer.music.play(-1)
        self.playing = true
    def updateVolume(self, ambienceObj):
        self.volume = ambienceObj.noisiness

ambience = Ambience()
speaker = Speaker()


#while 1:
    #1
