from gtts import gTTS
from playsound import playsound

def textToAudio(str):
    audio=gTTS(str)
    audio.save('mini.mp3')
    
textToAudio("33987")
playsound('mini.mp3')