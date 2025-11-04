from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound

def main():
    # Ask user for input text
    text = input("Enter text to translate: ")

    # Choose target language (hi = Hindi)
    target_lang = "hi"

    # Translate text automatically from any language
    translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
    print(f"Translated ({target_lang}): {translated}")

    # Convert translated text to speech
    tts = gTTS(translated, lang=target_lang)
    mp3_file = "output.mp3"
    tts.save(mp3_file)

    # Play the generated voice
    playsound(mp3_file)

if __name__ == "__main__":
    main()