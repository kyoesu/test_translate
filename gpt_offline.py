from transformers import MarianMTModel, MarianTokenizer

# Загрузка модели и токенизатора
model_name = 'Helsinki-NLP/opus-mt-ru-en'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_offline(text):
    # Токенизация текста
    inputs = tokenizer.encode(text, return_tensors='pt')
    # Перевод текста
    translated = model.generate(inputs)
    # Декодирование переведенного текста
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Пример использования
translated_text = translate_offline("Привет, как дела?")
print(translated_text)  # Output: Hello, how are you?