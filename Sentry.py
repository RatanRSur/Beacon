#from datetime import datetime
from pygame import mixer
from collections import deque
import RPi.GPIO as GPIO
from time import sleep
#import spidev

interruption='sounds/interruption.ogg' 

CLK=11
MISO=9
MOSI=10
CS=22

GPIO.setmode(GPIO.BCM)
GPIO.setup(MISO, GPIO.IN)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(MOSI, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)

class Ambience:
    def __init__(self):
        self.noiseArray = deque()
        self.noiseArray.append(1)
        self.noisiness = 0
        self.noiseSum=0
        self.maxLen=100
        #self.isNight = False
    def sample(self): 
        #thanks adafruit!
        # https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/script
        channel = 0
        GPIO.output(CS, 1)
        GPIO.output(CLK,0)
        GPIO.output(CS,0) #low CS activates chip
        request =  0x18
        request <<= 3
        for i in range(5):
            if (request & 0x80):
                GPIO.output(MOSI, 1)
            else:
                GPIO.output(MOSI, 0)
            request <<= 1
            GPIO.output(CLK, 1)
            GPIO.output(CLK, 0)

        adcout= 0
        for i in range(12):
            GPIO.output(CLK, 1)
            GPIO.output(CLK, 0)
            adcout <<= 1
            if(GPIO.input(MISO)):
                adcout |= 0x1

        GPIO.output(CS, 1)
        adcout >>=1
        adjusted = adcout
        #adjusted = abs(adcout-60)
        #self.noiseSum += adjusted
        if len(self.noiseArray) == self.maxLen:
            #self.noiseSum -= self.noiseArray[0]
            self.noiseArray.popleft()
        self.noiseArray.append(adjusted)
        self.noisiness = max(self.noiseArray)
        #self.noisiness = self.noiseSum / self.maxLen
        #print self.noisiness
        print self.noisiness
        #print len(self.noiseArray)
        #print adjusted
        return adjusted


class Speaker:
    def __init__(self):
        mixer.init()
        self.track = interruption
        mixer.music.load(self.track)
        self.volume = 0
        mixer.music.play(-1)
        self.playing = True
    def updateVolume(self, ambienceObj):
        self.volume = ambienceObj.noisiness

ambience = Ambience()
speaker = Speaker()

while 1:
    ambience.sample()
    sleep(0.05)
