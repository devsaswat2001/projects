import pyttsx3
import speech_recognition as sr
from neuralintents import GenericAssistant
import sys

r = sr.Recognizer()

engine = pyttsx3.init()


def talk(text):
    engine.setProperty('rate', 165)
    engine.say(text)
    engine.runAndWait()


def hello():
    talk("Hello. what can I do for you?")


"""
################## THIS IS THE LIST PART ##############
"""

lists = {}


def make_a_list():
    global r

    done = False

    while not done:
        try:
            with sr.Microphone() as source:
                talk("what should I call it?")
                r.adjust_for_ambient_noise(source, duration=0.2)
                voice = r.listen(source)
                listname = r.recognize_google(voice)
                listname = listname.lower()
                if listname in lists:
                    talk("what should I add?")
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    voice = r.listen(source)
                    item = r.recognize_google(voice)
                    item = item.lower()
                    lists[f"{listname}"].append(item)
                    done = True
                    print(lists)

                lists[f"{listname}"] = []
                talk("what should I add?")
                r.adjust_for_ambient_noise(source, duration=0.2)
                voice = r.listen(source)
                item = r.recognize_google(voice)
                item = item.lower()
                lists[f"{listname}"].append(item)
                done = True
                print(lists)
        except sr.UnknownValueError:
            r = sr.Recognizer()
            talk("I did not get that, could you please repeat? ")


def show_list():
    global r
    if len(lists.keys()) == 0:
        talk("no lists found")

    elif len(lists.keys()) > 1:
        talk("which list to show ?")

        done = False
        while not done:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    voice = r.listen(source)
                    listname = r.recognize_google(voice)
                    listname = listname.lower()
                    if listname in lists.keys():
                        done = True
                        talk(lists[f"{listname}"])
                        print(lists)
                    else:
                        talk(f"{listname} not found")
                        talk("Do you want to create one? ")
                        r.adjust_for_ambient_noise(source, duration=0.2)
                        voice = r.listen(source)
                        command = r.recognize_google(voice)
                        command = command.lower()
                        if "yes" in command:
                            done = True
                            make_a_list()

            except sr.UnknownValueError:
                r = sr.Recognizer()
                talk("Did not get that, please repeat!")
    else:
        lst = list(lists.values())
        talk(lst)
        print(lst)


def delete_item():
    global r
    if len(lists.keys()) == 0:
        talk("no lists found to delete item")

    elif len(lists.keys()) > 1:

        done = False
        while not done:
            try:
                with sr.Microphone() as source:
                    talk("which list to modify ?")
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    voice = r.listen(source)
                    listname = r.recognize_google(voice)
                    listname = listname.lower()
                    print(f"input: {listname}")
                    if listname in lists.keys():
                        talk("what to delete?")
                        r.adjust_for_ambient_noise(source, duration=0.2)
                        voice = r.listen(source)
                        item_to_delete = r.recognize_google(voice)
                        item_to_delete = item_to_delete.lower()
                        print(f"input: {item_to_delete}")
                        if item_to_delete in lists[f"{listname}"]:
                            done = True
                            talk("deleting")
                            lists[listname].remove(item_to_delete)
                            print(lists[listname])
                        else:
                            done = True
                            talk("no such item found!")
                            print("no such item found!")
            except sr.UnknownValueError:
                r = sr.Recognizer()
                talk("Did not get that, please repeat!")
    else:
        try:
            with sr.Microphone() as source:
                talk("what to delete?")
                r.adjust_for_ambient_noise(source, duration=0.2)
                voice = r.listen(source)
                item_to_delete = r.recognize_google(voice)
                item_to_delete = item_to_delete.lower()
                print(f"input: {item_to_delete}")
                lst = list(lists.keys())
                if item_to_delete in lists[lst[0]]:
                    talk("deleting")
                    lists[lst[0]].remove(item_to_delete)
                else:
                    talk("no such item found!")
        except sr.UnknownValueError:
            r = sr.Recognizer()
            talk("please repeat")


def delete_list():
    global r
    if len(lists.keys()) == 0:
        talk("no lists to delete")
    elif len(lists.keys()) > 1:
        talk("which list to delete?")
        done = False
        while not done:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    voice = r.listen(source)
                    listname = r.recognize_google(voice)
                    listname = listname.lower()
                    if listname in lists.keys():
                        talk(f"deleting {listname}")
                        del lists[f"{listname}"]
                    else:
                        talk("list not found")
            except sr.UnknownValueError:
                r = sr.Recognizer()
                talk("Did not understand that, please repeat!")
    else:
        lists.clear()
        talk(" there was only one list. list deleted")


def add_item():
    global r
    if len(lists.keys()) == 0:
        try:
            with sr.Microphone() as source:
                talk("no lists made to add")
                talk("do you want to create a list?")
                r.adjust_for_ambient_noise(source, duration=0.2)
                voice = r.listen(source)
                command = r.recognize_google(voice)
                command = command.lower()
                if "yes" in command:
                    make_a_list()
                    print("making a list")
        except sr.UnknownValueError:
            r = sr.Recognizer()
            talk("please repeat! ")

    else:

        done = False
        while not done:
            try:
                with sr.Microphone() as source:
                    talk("which list to modify?")
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    voice = r.listen(source)
                    listname = r.recognize_google(voice)
                    listname = listname.lower()
                    print(f"input: {listname}")
                    if listname in lists.keys():
                        talk("what to add ?")
                        r.adjust_for_ambient_noise(source, duration=0.2)
                        voice = r.listen(source)
                        item_to_add = r.recognize_google(voice)
                        item_to_add = item_to_add.lower()
                        done = True
                        talk(f"adding {item_to_add} in {listname}")
                        print(f"adding {item_to_add} in {listname}")
                        lists[f"{listname}"].appen(item_to_add)

                    else:
                        done = True
                        talk("list not found")
                        print("list not found")

            except sr.UnknownValueError:
                r = sr.Recognizer()
                talk("did not get that, please repeat! ")
                print("did not get that, please repeat! ")


mappings = {
    "greeting": hello,
    "make_a_list": make_a_list,
    "show_list": show_list,
    "delete_item": delete_item,
    "delete_list": delete_list,
    "add_item": add_item
}
assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()
print("listening")
talk("please give commands")

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()

        assistant.request(command)
    except sr.UnknownValueError:
        r = sr.Recognizer()
