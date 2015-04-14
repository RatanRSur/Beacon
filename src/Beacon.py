from datetime import datetime
from pygame import mixer

interruption='~/stuff/Sentry/sounds/interruption.mp3'

mixer.init()
mixer.music.load(interruption)
mixer.music.play()
