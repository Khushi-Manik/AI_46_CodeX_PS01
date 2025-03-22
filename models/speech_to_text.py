import os
import speech_recognition as sr
import pydub
import imageio_ffmpeg

# Ensure FFmpeg is set properly
os.environ["IMAGEIO_FFMPEG_EXE"] = imageio_ffmpeg.get_ffmpeg_exe()

def convert_audio_to_wav(input_path):
    """Convert any audio format to WAV using FFmpeg"""
    output_path = input_path.rsplit(".", 1)[0] + ".wav"
    audio = pydub.AudioSegment.from_file(input_path)
    audio.export(output_path, format="wav")
    return output_path

def transcribe_audio(file_path):
    """Convert speech to text from an audio file"""
    recognizer = sr.Recognizer()
    
    # Convert to WAV if not already in WAV format
    if not file_path.lower().endswith(".wav"):
        file_path = convert_audio_to_wav(file_path)

    with sr.AudioFile(file_path) as source:
        print("\n🔄 Processing audio...")
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data)
        print("\n✅ Transcription:\n", text)
        return text
    except sr.UnknownValueError:
        print("\n❌ Could not understand audio")
        return None
    except sr.RequestError:
        print("\n⚠️ Could not request results from Google Speech Recognition")
        return None

def record_audio():
    """Record audio using microphone and transcribe"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Recording... Speak now!")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    # Save the recording as a WAV file
    output_path = "recorded_audio.wav"
    with open(output_path, "wb") as f:
        f.write(audio_data.get_wav_data())

    return transcribe_audio(output_path)

def main():
    """Main function to choose between recording or file transcription"""
    print("\nChoose an option:")
    print("1️⃣ Record audio and convert to text")
    print("2️⃣ Transcribe an existing audio file")
    
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        record_audio()
    elif choice == "2":
        file_path = input("\nEnter the path of the audio file: ").strip()
        if not os.path.exists(file_path):
            print("\n❌ File not found!")
        else:
            transcribe_audio(file_path)
    else:
        print("\n❌ Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
