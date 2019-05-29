from tkinter import *

root = None
session_settings = None
ent_ww = None
ent_minimal_volume = None
ent_resX = None
ent_resY = None


def btn_close_opr():
    session_settings.set_height_res(ent_resY.get())
    session_settings.set_width_res(ent_resX.get())
    session_settings.set_wake_word(ent_ww.get())
    session_settings.set_min_volume(ent_minimal_volume.get())
    root.destroy()


def run(settings):
    global root
    global session_settings
    global ent_ww
    global ent_minimal_volume
    global ent_resX
    global ent_resY
    session_settings = settings
    root = Tk()
    root.title("A(GH)lexa - settings")
    root.minsize(width=300, height=200)
    root.resizable(width=True, height=True)
    root.grid_propagate(True)
    root.grid(baseWidth=300, baseHeight=200, widthInc=True, heightInc=True)

    lbl_ww = Label(root, text="Wake word:")
    lbl_ww.grid(sticky=E)
    ent_ww = Entry(root)
    ent_ww.insert(END, session_settings.get_wake_word())
    ent_ww.grid(row=0, column=1, sticky=W)

    lbl_minimal_volume = Label(root, text="Minimal volume:")
    lbl_minimal_volume.grid(row=1, column=0, sticky=E)
    ent_minimal_volume = Entry(root)
    ent_minimal_volume.insert(END, session_settings.get_min_volume())
    ent_minimal_volume.grid(row=1, column=1, sticky=W)

    lbl_resY = Label(root, text="Height resolution:")
    lbl_resY.grid(row=2, column=0, sticky=E)
    ent_resY = Entry(root)
    ent_resY.insert(END, session_settings.get_width_res())
    ent_resY.grid(row=2, column=1, sticky=W)

    lbl_resX = Label(root, text="Width resolution:")
    lbl_resX.grid(row=3, column=0, sticky=E)
    ent_resX = Entry(root)
    ent_resX.insert(END, session_settings.get_height_res())
    ent_resX.grid(row=3, column=1, sticky=W)

    btn_save_and_close = Button(root, text="Save and close", command=btn_close_opr)
    btn_save_and_close.grid(row=4, column=0, columnspan=2)

    root.mainloop()
