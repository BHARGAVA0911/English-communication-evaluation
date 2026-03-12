import whisper
from pydub import AudioSegment
from IPython.display import Audio

# Convert MP3 to WAV
def convert_mp3_to_wav(mp3_path, wav_path="converted_audio_1.wav"):
    audio = AudioSegment.from_mp3(mp3_path)
    audio = audio.set_frame_rate(16000).set_channels(1)  # Resample to 16kHz mono
    audio.export(wav_path, format="wav")
    return wav_path

# Load Whisper model and transcribe
def transcribe_with_whisper(mp3_path):
    model = whisper.load_model("base")
    wav_path = convert_mp3_to_wav(mp3_path)
    result = model.transcribe(wav_path)
    return result["text"]

audio_file = "/content/X6mHBDi0.mp3"
wav_path = convert_mp3_to_wav(audio_file)
transcript = transcribe_with_whisper(audio_file)
print(f"Transcript: {transcript}\n")
display_audio = Audio(wav_path)
display(display_audio)
