#text to speech
from gtts import gTTS

abc=open('speech.txt')

text=abc.read()

language ="en"

obj=gTTS(text=text,lang=language,slow=False)

obj.save("speaks.mp3")



