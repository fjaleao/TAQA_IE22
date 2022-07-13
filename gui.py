# Python program to create
# a file explorer in Tkinter
from asyncore import write
from curses import window
import os
from platform import win32_edition
import pandas

# import all components
# from the tkinter library
from tkinter import *
from tkinter import ttk

# import filedialog module
from tkinter import filedialog
import tkinter
from tkinter import messagebox
from analysis import analysis
from keywords import keywords

from transcript import transcript

# Function for opening the
# file explorer window


def openfile():
    return filedialog.askopenfilename()


def browseFiles():
    filename = filedialog.askopenfilename(initialdir=os.getcwd()+"/IO",
                                          title="Select a File",
                                          filetypes=(("Audio files",
                                                      "*.mp3*, *.wav*"),
                                                     ("Video files",
                                                      "*.mp4*")))

    # Change label contents
    label_file_explorer.configure(text=filename)

    button_analysis.grid_remove()


def Go():

    if(combox.get() == "English"):
        lang = "en-US"
    elif(combox.get() == "Portuguese"):
        lang = "pt-PT"
    elif(combox.get() == "Madeirense"):
        lang = "pt-PT"

    label_status.config(text="Status : Processing...")

    window.update_idletasks()

    trs = transcript(label_file_explorer.cget("text"), lang, 1)

    label_status.config(text="Status : Finished")

    wcount = keywords(trs).to_string()

    print(wcount)

    with open("words.txt", "w") as f:
        f.write(wcount)

    messagebox.showinfo(
        "Title", "The word statistics have been written to file words.txt")

    button_analysis.grid(column=1, row=7)

    label_trs.config(text=trs)


def showAnalysis():
        
    txt = label_trs.cget("text")
    lista = analysis(txt)
    results = Tk()

    #window.state(newstate='iconic')

    results.geometry("250x500")

    results.title("Results")
    L1 = Label(results, text="Text")
    L2 = Label(results, text="Rank")
    L3 = Label(results, text="Count")

    print("AQUI")

    for i in range(0,len(lista)):
        print("ENTROU")
        Lt = Label(results, text=lista(i).texto)
        Lr = Label(results, text=lista(i).rank)
        Lc = Label(results, text=lista(i).count)
        print(Lc)


    L1.grid(column=0,row=0)
    L2.grid(column=1,row=0)
    L3.grid(column=2,row=0)
    
    btn_back = Button(results, text = "Back") 



# Create the root window
window = Tk()

# Set window title
window.title('Great Title')

window.minsize(800, 500)
window.maxsize(800, 500)


window.state('normal')

# Set window size
window.geometry("700x500")

# Set window background color
window.config(background="white")


# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Select File",
                            width=100, height=3,
                            fg="red",
                            justify='center')


label_lang = Label(window,
                   text="Select Language",
                   width=100, height=4,
                   fg="red",
                   justify='center')

label_trs = Label(window)

label_status = Label(window, text="Status:",
                    width=100,
                    height=4,
                    fg="red",
                    justify='center')

vlist = ["English", "Portuguese", "Madeirense"]

combox = ttk.Combobox(window, values=vlist)

button_go = Button(window, text="Transcript", command=Go)

button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)

button_analysis = Button(
    window, text="Analyse and Show Results", command=showAnalysis)

button_exit = Button(window,
                     text="Exit",
                     command=exit)


# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns

label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

label_lang.grid(column=1, row=3)
combox.grid(column=1, row=4)

button_go.grid(column=1, row=5)

label_status.grid(column=1, row=6)

button_exit.grid(column=1, row=9)

# Let the window wait for any events
window.mainloop()
