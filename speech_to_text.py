import speech_recognition as sr


def transcribe_speech():
    """Captures speech from the microphone and returns the transcription."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        transcription = recognizer.recognize_google(audio)
        print(f"Transcription: {transcription}")
        return transcription
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None