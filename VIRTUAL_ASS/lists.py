lists = {}
def make_a_list():
    global r
    talk("what should I call it?")

    # done = False

    # while not done:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            voice = r.listen(source)
            listname = r.recognize_google(voice)
            listname = listname.lower()

            lists[f"{listname}"] = []
            talk("what should I add?")
            r.adjust_for_ambient_noise(source, duration=0.2)
            voice = r.listen(source)
            item = r.recognize_google(voice)
            item = item.lower()
            lists[f"{listname}"].append(item)
            done = True

    except sr.UnknownValueError:
        r = sr.Recognizer()
        talk("I did not get that, could you please repeat? ")


def show_list():
    global r
    if len(lists.keys) == 0:
        talk("no lists found")

    elif len(lists.keys()) > 1:
        talk("which list to show ?")

        # done = False
        # while not done:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                voice = r.listen(source)
                listname = r.recognize_google(voice)
                listname = listname.lower()
                if listname in lists.keys():
                    done = True
                    talk(lists[f"{listname}"])
                else:
                    talk(f"{listname} not found")
                    talk("Do you want to create one? ")
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    voice = r.lisen(source)
                    command = r.recognize_google(voice)
                    command = command.lower()
                    if "yes" in command:
                        done = True
                        make_a_list()

        except sr.UnknownValueError:
            r = sr.Recognizer()
            talk("Did not get that, please repeat!")
    else:
        talk(lists.values())


def delete_item():
    global r
    if len(lists.keys) == 0:
        talk("no lists found to delete item")

    elif len(lists.keys()) > 1:
        talk("which list to modify ?")

        done = False
        while not done:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    voice = r.listen(source)
                    listname = r.recognize_google(voice)
                    listname = listname.lower()
                    if listname in lists.keys():
                        talk("what to delete?")
                        r.adjust_for_ambient_noise(source, duration=0.2)
                        voice = r.listen(source)
                        item_to_delete = r.recognize_google(voice)
                        item_to_delete = item_to_delete.lower()
                        if item_to_delete in lists[f"{listname}"]:
                            done = True
                            talk("deleting")
                            lists[listname].remove(item_to_delete)
                        else:
                            done = True
                            talk("no such item found!")
            except sr.UnknownValueError:
                r = sr.Recognizer()
                talk("Did not get that, please repeat!")
    else:
        r.adjust_for_ambient_noise(source, duration=0.2)
        voice = r.listen(source)
        item_to_delete = r.recognize_google(voice)
        item_to_delete = item_to_delete.lower()
        if item_to_delete in lists[f"{listname}"]:
            talk("deleting")
            lists[listname].remove(item_to_delete)
        else:
            talk("no such item found!")


def delete_list():
    global r
    if len(lists.keys) == 0:
        talk("no lists to delete")
    elif len(lists.keys) > 1:
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


def add_item():
    global r
    if len(lists.keys) == 0:
        talk("no lists made to add")
        talk("do you want to create a list?")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                voice = r.listen(source)
                command = r.recognize_google(voice)
                command = command.lower()
                if "yes" in command:
                    make_a_list()
        except sr.UnknownValueError:
            r = sr.Recognizer()
            talk("please repeat! ")

    else:
        talk("which list to modify?")
        done = False
        while not done:
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    voice = r.listen(source)
                    listname = r.recognize_google(voice)
                    listname = listname.lower()

                    if listname in lists.keys():
                        talk("what to add ?")
                        r.adjust_for_ambient_noise(source, duration=0.2)
                        voice = r.listen(source)
                        item_to_add = r.recognize_google(voice)
                        item_to_add = item_to_add.lower()
                        done = True
                        talk(f"adding {item_to_add} in {listname}")
                        lists[f"{listname}"].appen(item_to_add)

                    else:
                        done = True
                        talk("list not found")
            except sr.UnknownValueError:
                r = sr.Recognizer()
                talk("did not get that, please repeat! ")
