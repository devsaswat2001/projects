import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as kt
import pyjokes

engine = pyttsx3.init()


def talk(text):
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()


class NotSupported(Exception):
    def __init__(self, message="command not supported yet"):
        self.message = message

    def __str__(self):
        f"""{self.message}"""


class VoiceInput:
    def __init__(self):
        self.listener = sr.Recognizer

        try:
            with sr.Recognizer as source:
                print("Listening")
                talk("Listening")
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()

                if "hey" or "shelly" in command:
                    Output.greet(command)
                elif "who is" in command:
                    Output.wiki_search(command)
                elif "what is" in command:
                    Output.wiki_search(command)
                elif "why" or "how" or "where" or "find" in command:
                    Output.google_search(command)
                elif "play" in command:
                    Output.play_songs(command)
                elif "joke" or "jokes" in command:
                    Output.tell_a_joke(command)

        except NotSupported:
            talk(NotSupported)


class Output:

    def __init__(self, command):
        self.command = command

    def greet(self):
        talk("Hi saswat how may I help you?")

    def wiki_search(self):
        keyword = self.command.replace("who is", "")
        talk("Just a moment")
        info_got = wikipedia.summary(keyword, 4)
        talk(info_got)

    def google_search(self):
        talk(kt.search(self.command))

    def play_songs(self):
        song = self.command.replace("play", "")
        talk("playing" + song)
        kt.playonyt(song)

    def tell_a_joke(self):
        talk("Here is a joke")
        talk(pyjokes.get_jokes())
