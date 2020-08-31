import pyttsx3 # pip install pyttsx3

# 1. essas linhas de código fazem o robo falar

engine = pyttsx3.init() # 1.1 -  inicializando o motor da fala
engine.say("Hello World!") # 1.2 - dando o comando do que o robo vai falar.
engine.runAndWait() # 1.3 - processando a fala
engine.stop() # parando a fala
