from datetime import datetime
from pygame import mixer

interruption='sounds/interruption.ogg' 

mixer.init()
mixer.music.load(interruption)
mixer.music.play(-1)
#while 1:
        #1
