import pyttsx3
import time

def speak(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("volume", 0.9)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        del engine
        time.sleep(0.2)  # small delay helps release the voice engine
    except Exception as e:
        print("⚠️ Error:", e)

print("\n🤖 Text-to-Speech Ready!")
print("💬 Type something and press Enter (or type 'exit' to quit)\n")

while True:
    text = input("🎤 You: ").strip()

    if text.lower() == "exit":
        print("👋 Goodbye!")
        speak("Goodbye!")
        break
    elif text:
        print(f"🗣️ Speaking: {text}")
        speak(text)
    else:
        print("💡 Type something or 'quit' to exit.")
quit