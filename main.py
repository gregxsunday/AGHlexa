import os
import settings
import pickle
import Actions
import threading
import GUI

class GUI_thread(threading.Thread):
    def run(self):
        GUI.run(session_settings)


path = "saved_settings.settings"
session_settings = None


def execute_command(command):
    global session_settings
    com_with_args = command.split(" ")
    if com_with_args[0] == "incv":
        if session_settings is not None:
            session_settings.set_min_volume(session_settings.get_min_volume() + 1)
    elif com_with_args[0] == "decv":
        if session_settings is not None:
            session_settings.set_min_volume(session_settings.get_min_volume() - 1)
    elif com_with_args[0] == "setww":
        if session_settings is not None and len(com_with_args) > 1:
            session_settings.set_wake_word(com_with_args[1])
    else:
        print("Minimal volume is: " + session_settings.get_min_volume().__str__())
        print("\nWake word is: " + session_settings.get_wake_word()+"\n")


def main():
    global session_settings
    if os.path.isfile(path):
        unpickling = open(path, "rb")
        session_settings = pickle.load(unpickling)
        unpickling.close()
    else:
        session_settings = settings.Setter()

    #gthread = GUI_thread()
    #gthread.run()

    GUI.run(session_settings)

    #while True:
    #    command = input()
    #   if command.split(" ")[0].lower() == "exit":
    #        break
    #    execute_command(command)


if __name__ == "__main__":
    main()
