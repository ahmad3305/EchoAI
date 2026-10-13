import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You:", text)

        return text

    except sr.WaitTimeoutError:
        print("No speech detected.")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Speech recognition service is unavailable.")
    except OSError:
        print("Microphone not found or unavailable.")

    return ""


def speak(text):
    print("Echo:", text)
    engine.say(text)
    engine.runAndWait()