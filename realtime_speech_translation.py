import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from deep_translator import GoogleTranslator
import os
import time

# Text-to-Speech: Speak translated text in target language
def speak(text, language="en"):
    try:
        print(f"🔊 Speaking in {language}...")
        tts = gTTS(text=text, lang=language, slow=False)
        filename = "temp_audio.mp3"
        tts.save(filename)
        playsound(filename)
        time.sleep(0.5)  # Small delay before cleanup
        os.remove(filename)  # Clean up temp file
        print("✅ Audio played successfully!")
    except Exception as e:
        print(f"❌ Speech error: {e}")

# Speech-to-Text: Recognize spoken language (English)
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        print("(Adjusting for ambient noise...)")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=10)
            print("🔍 Recognizing speech...")
            text = recognizer.recognize_google(audio, language="en-US")
            print(f"✅ You said: {text}")
            return text
        except sr.WaitTimeoutError:
            print("❌ No speech detected. Please try again.")
        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
    return ""

# Translate text using deep-translator (more reliable alternative)
def translate_text(text, target_language="hi"):
    try:
        # Try using googletrans first
        from googletrans import Translator
        translator = Translator()

        # Create a new translator instance for each translation
        translation = translator.translate(text, dest=target_language)

        # Handle both sync and async versions
        if hasattr(translation, 'text'):
            result = translation.text
        else:
            # If it's a coroutine, we need to handle it differently
            import asyncio
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            translation = loop.run_until_complete(translator.translate(text, dest=target_language))
            result = translation.text
            loop.close()

        print(f"🌍 Translated text ({target_language}): {result}")
        return result

    except Exception as e:
        print(f"❌ Translation error with googletrans: {e}")
        print("🔄 Trying alternative translation method...")

        try:
            # Fallback to deep-translator
            from deep_translator import GoogleTranslator

            # Language code mapping for deep-translator
            result = GoogleTranslator(source='en', target=target_language).translate(text)
            print(f"🌍 Translated text ({target_language}): {result}")
            return result
        except ImportError:
            print("❌ Please install deep-translator: pip install deep-translator")
            return ""
        except Exception as e2:
            print(f"❌ Translation failed: {e2}")
            return ""

# Display language options to the user
def display_language_options():
    print("\n" + "="*50)
    print("🌍 MULTILINGUAL SPEECH TRANSLATOR")
    print("="*50)
    print("Available translation languages:")
    print("1. Hindi (hi)")
    print("2. Tamil (ta)")
    print("3. Telugu (te)")
    print("4. Bengali (bn)")
    print("5. Marathi (mr)")
    print("6. Gujarati (gu)")
    print("7. Malayalam (ml)")
    print("8. Punjabi (pa)")
    print("9. Spanish (es)")
    print("="*50)

    choice = input("Please select the target language number (1-9): ")

    language_dict = {
        "1": "hi",  # Hindi
        "2": "ta",  # Tamil
        "3": "te",  # Telugu
        "4": "bn",  # Bengali
        "5": "mr",  # Marathi
        "6": "gu",  # Gujarati
        "7": "ml",  # Malayalam
        "8": "pa",  # Punjabi
        "9": "es"   # Spanish
    }

    selected_lang = language_dict.get(choice, "hi")
    print(f"✅ Selected language: {selected_lang}\n")
    return selected_lang

# Main function to combine all steps
def main():
    try:
        # Step 1: Select target language
        target_language = display_language_options()

        # Step 2: Capture speech input
        original_text = speech_to_text()

        if original_text:
            # Step 3: Translate the text
            translated_text = translate_text(original_text, target_language)

            if translated_text:
                # Step 4: Speak the translated text
                speak(translated_text, language=target_language)
                print("\n✅ Translation complete!")
            else:
                print("❌ Translation failed. Please try again.")
        else:
            print("❌ No speech input detected. Please try again.")

    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()