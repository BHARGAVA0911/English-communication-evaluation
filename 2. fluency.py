import librosa
import nltk
from nltk import word_tokenize
nltk.download('punkt_tab')

def analyze_fluency(audio_path, text):
    # Load audio and calculate duration
    audio, sr = librosa.load(audio_path, sr=16000)
    duration = librosa.get_duration(y=audio, sr=sr)

    # Tokenize words and calculate words per minute (WPM)
    words = len(word_tokenize(text))
    wpm = words / (duration / 60) if duration > 0 else 0

    # Determine fluency band based on WPM
    if wpm >= 140:
        fluency_band = 5
    elif 120 <= wpm < 140:
        fluency_band = 4
    elif 100 <= wpm < 120:
        fluency_band = 3
    elif 80 <= wpm < 100:
        fluency_band = 2
    elif wpm < 80:
        fluency_band = 1
    return fluency_band
