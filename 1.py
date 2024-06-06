import speech_recognition as sr
from pydub import AudioSegment
import os

# Конвертация MP3 в WAV
mp3_path = "C:\WorkSpace\\test\\MyApp_yhebka\\2.mp3"
wav_path = r"C:\WorkSpace\test\MyApp_yhebka\v2.wav"

# Загрузка и конвертация файла
audio = AudioSegment.from_mp3(mp3_path)
audio.export(wav_path, format="wav")

# Использование сконвертированного файла
audio = sr.AudioFile(wav_path)

# Инициализация распознавателя речи
recognizer = sr.Recognizer()

try:
    with audio as source:
        audio_data = recognizer.record(source, duration=600)  # Слушаем первые 10 минут
        text = recognizer.recognize_google(audio_data, language="ru-RU")
    # Запись транскрипции в файл
    with open(r"C:\WorkSpace\test\MyApp_yhebka\transcription.txt", "w", encoding='utf-8') as file:
        file.write(text)
except Exception as e:
    print(f"Произошла ошибка: {e}")
