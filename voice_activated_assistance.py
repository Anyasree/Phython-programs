import speech_recognition as sr
import pyttsx3
from datetime import datetime
import platform

def speak(text: str):
    """Speak text using TTS with enhanced debugging."""
    print("SPEAK:", text)
    try:
        # Get available engines
        print(f"System: {platform.system()}")

        engine = pyttsx3.init()

        # Debug: Print available voices
        voices = engine.getProperty('voices')
        print(f"Available voices: {len(voices)}")

        # Set properties
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)  # Max volume

        # Try setting a specific voice (helps on some systems)
        if voices:
            engine.setProperty('voice', voices[0].id)
            print(f"Using voice: {voices[0].name}")

        print("About to speak...")
        engine.say(text)
        print("Running engine...")
        engine.runAndWait()
        print("Speech completed")

    except Exception as e:
        print(f"Error speaking: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

def get_audio(timeout=5, phrase_time_limit=6):
    """Capture voice input and return recognized text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        # Only listen once - removed duplicate listen() call
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

    try:
        command = r.recognize_google(audio)
        print(f"✅ You said: {command}")
        return command.lower()
    except sr.WaitTimeoutError:
        print("⌛ No speech detected.")
    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
    return ""

def respond_to_command(command):
    """Process recognized voice command."""
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "time" in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        hour = now.hour
        minute = now.minute

        # Check if it's class time (21:10)
        if hour == 21 and minute == 14:
            speak("It is time for a class with Anya")
        # Check if class is coming up soon (21:05 - 21:09)
        elif hour == 21 and 5 <= minute < 10:
            speak(f"The time is {current_time}. Your class with Anya starts in {10 - minute} minutes")
        else:
            speak(f"The time is {current_time}")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True

def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break

if __name__ == "__main__":
    main()