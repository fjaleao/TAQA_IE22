# Python program to create
# a file explorer in Tkinter
from fileinput import filename
import os
from select import select

# import all components
# from the tkinter library
from tkinter import *
from tkinter import ttk

# import filedialog module
from tkinter import filedialog
import tkinter

from sst import transcript

# Function for opening the
# file explorer window

def openfile():
    return filedialog.askopenfilename()

def browseFiles():
	filename = filedialog.askopenfilename(initialdir=os.getcwd(),
										title="Select a File",
										filetypes=(("Video files",
														"*.mp4*"),
													("Audio files",
														"*.mp3*, *.wav*")))

	# Change label contents
	label_file_explorer.configure(text=filename)    
	
def Go():

    if(combox.get()=="English"):
        lang = "en-US"
    elif(combox.get()=="Portuguese"):
        lang = "pt-PT"

    trs = None
    trs = transcript(label_file_explorer.cget("text"), lang, 1)

    while(trs==None):
        label_status.config(text="Status : Processing...")

    label_status.config(text="Status : Finished")




																								
# Create the root window
window = Tk()

# Set window title
window.title('Transcripter 5000')

# Set window size
window.geometry("800x500")

# Set window background color
window.config(background = "white")


# Create a File Explorer label
label_file_explorer = Label(window,
							text = "Select File",
							width = 100, height = 3,
							fg = "blue")


label_lang= Label(window,
							text = "Select Language",
							width = 100, height = 4,
							fg = "blue")


label_status = Label(window, text="Status:", width = 100, height = 4,
							fg = "blue")

vlist = ["English", "Portuguese"]	

combox = ttk.Combobox(window, values=vlist)

button_go = Button(window, text="Transcript", command=Go)

button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(window,
					text = "Exit",
					command = exit)




# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

label_lang.grid(column=1, row=3)
combox.grid(column=1, row=4)

button_go.grid(column = 1, row = 5)

button_exit.grid(column = 1,row = 6)

# Let the window wait for any events
window.mainloop()
