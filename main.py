import speech_recognition as sr
from translate import Translator
import pyttsx3

voice_engine = pyttsx3.init()
translator = Translator(from_lang="ru", to_lang="en")

def talk(_text):
    print(_text)
    voice_engine.say(_text)
    voice_engine.runAndWait()

def translate(_text):
    traslated_text = translator.translate(_text)
    talk(traslated_text)

def command() :
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-то")
        r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        recognized_text = r.recognize_google(audio, language="ru-RU")
        print("Распознано: " + recognized_text)

    except sr.UnknownValueError:
        talk("Повторите еще раз")
        recognized_text = command()

    return recognized_text

while True:
    translate(command())