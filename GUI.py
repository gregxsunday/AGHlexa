from tkinter import *
import threading
import settings_GUI
import Actions

root = None
session_settings = None
information = None


class Listener(threading.Thread):  # listen in background
    def run(self):
        pass


def btn_close_opr():
    root.destroy()


def btn_settings_opr():
    settings_GUI.run(session_settings)


def btn_listen_opr():
    input_procedure = "Play sth"  # change to google API input
    instruction_with_args = Actions.get_instruction_with_args(input_procedure)
    if instruction_with_args[0] == "WrongInstruction":
        information.labelText = "Wrong instruction"
        return
    return  # Place for program modules execution


def run(settings):
    global root
    global session_settings
    global information
    session_settings = settings
    root = Tk()
    root.title("A(GH)lexa")
    root.minsize(width=session_settings.get_width_res(), height=session_settings.get_height_res())
    root.resizable(width=True, height=True)
    root.grid_propagate(True)
    root.grid(baseWidth=session_settings.get_width_res(), baseHeight=session_settings.get_height_res(), widthInc=True, heightInc=True)

    information = Label(root, text="Welcome, say something")
    information.grid(columnspan=2, sticky=S)
    btn_close = Button(root, text="Close", command=btn_close_opr)
    btn_close.grid(row=1, column=0)
    btn_settings = Button(root, text="Settings", command=btn_settings_opr)
    btn_settings.grid(row=1, column=1)

    btn_listen = Button(root, text="Listen", command=btn_listen_opr)
    btn_listen.grid(row=2, column=0, columnspan=2)

    root.mainloop()