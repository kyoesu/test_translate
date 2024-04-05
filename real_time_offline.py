import speech_recognition as sr
import pyttsx3
from transformers import MarianMTModel, MarianTokenizer




def main():
    voice_engine = pyttsx3.init()
    # Загрузка модели и токенизатора
    model_name = 'Helsinki-NLP/opus-mt-ru-en'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    r = sr.Recognizer()
    while True:
        new_text=translate_offline(recognition_text(voice_engine,r),tokenizer, model)
        talk(new_text,voice_engine)


def talk(words, voice_engine):
    print(words)
    voice_engine.say(words)
    voice_engine.runAndWait()

def recognition_text(voice_engine,r) :
    

    with sr.Microphone() as source:
        print("Скажите что-то")
        r.pause_threshold = 1 
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        recognized_text = r.recognize_google(audio, language="ru-RU")
        print("Распознано: " + recognized_text)

    except sr.UnknownValueError:
        talk("Повторите еще раз",voice_engine)
        recognized_text = recognition_text(voice_engine,r)

    return recognized_text

def translate_offline(text,tokenizer, model):
    # Токенизация текста
    inputs = tokenizer.encode(text, return_tensors='pt')
    # Перевод текста
    translated = model.generate(inputs)
    # Декодирование переведенного текста
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text










if __name__ == '__main__':
    main()
    