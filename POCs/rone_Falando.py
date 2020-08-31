import pyttsx3 # pip install pyttsx3

# essas linhas de código fazem o robo falar

engine = pyttsx3.init()
engine.say("Hello World!")
engine.runAndWait()
engine.stop()
