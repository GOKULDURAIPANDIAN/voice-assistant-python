import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initialize recognizer & text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Choose voice (0 = male, 1 = female on most systems)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for a voice command"""
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')
            return command
    except:
        return ""

def run_assistant():
    """Process the voice command"""
    command = take_command()
    print(f"👉 Command: {command}")

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        try:
            info = wikipedia.summary(person, 1)
            talk(info)
        except:
            talk("Sorry, I couldn't find information on that.")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'open youtube' in command:
        talk("Opening YouTube")
        pywhatkit.playonyt("YouTube")

    elif command != "":
        talk('Sorry, I did not get that. Please repeat.')

# Run continuously
while True:
    run_assistant()
