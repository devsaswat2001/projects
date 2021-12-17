import pywhatkit as kt
import speech_recognition as sr

recognizer = sr.Recognizer()

class Whatsapp:
    def __init__(self):
        self.group = None
        self.contact = None

    def command_input(self,command):
        if "to" in command:
            self.contact = command.replace("send a message to","")
            Whatsapp.contact(self.contact)
        else:
            talk("to whom?")
            command = recongnizer.listen()
            if "group" in command:
                self.group = command.replace("to group","")
                Whatsapp.group(self.group)
            else:
                if command in contact_list[name]:
                    Whatsapp.contact(command)
                else:
                    talk(command+" not found in your contacts. Do you want to save it?")
                    command = recognizer.listen()
                    if "yes" in command:
                        talk("number to be saved, sir")
                        number = recognizer.listen()
                        contact_list.csv(add(name,number))
                        talk("saving")
                        talk("sending message")
                        Whatsapp.contact(number)

    def contact(self):
        phone_no = self.contact_list[number of the selected one]
        talk("what to write,sir?")
        command = recognizer.listen()
        messgae = recognizer.recongnize_google(command)
        message = message.lower()
        kt.sendwhatmsg_instantly(f"+91{phone_no}", message)
        talk("sending")

    def group(self):
        talk("what to write,sir?")
        command = recognizer.listen()
        messgae = recognizer.recongnize_google(command)
        message = message.lower()
        kt.sendwhatmsg_group(self.group, message)
        talk("sending")
