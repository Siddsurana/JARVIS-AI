import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"jarvis:{text}")
    engine.say(text)
    engine.runAndWait()


speak("Hello, I am your Python speaking BOT created by Siddharth")