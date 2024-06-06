import speech_recognition as sr

# Загрузка аудио файла
audio_path = r"C:\WorkSpace\test\MyApp_yhebka\videoplayback.weba"
audio = sr.AudioFile(audio_path)

# Инициализация распознавателя речи
recognizer = sr.Recognizer()

# Использование распознавателя для транскрипции аудио
try:
    with audio as source:
        audio_data = recognizer.record(source, duration=600)  # Слушаем первые 10 минут
        text = recognizer.recognize_google(audio_data, language="ru-RU")
except Exception as e:
    print(f"Произошла ошибка при распознавании аудио: {e}")

# Создание текстового файла и запись распознанного текста
try:
    with open(r"C:\WorkSpace\test\MyApp_yhebka\transcription.txt", "w", encoding='utf-8') as file:
        file.write(text)
except Exception as e:
    print(f"Произошла ошибка при записи файла: {e}")
