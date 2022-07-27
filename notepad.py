# Program Created by TJ Kapil
# this module provides classes and factory functions for creating file/directory selection windows.
from tkinter.filedialog import *
# 1. Tinker (UI)
import tkinter as tk
from tkinter import *

# Implement the open, save, and exitm clear buttons
# Define the save button
def saveFile():  # Save the file
    new_file = asksaveasfile(mode = 'w', filetypes = [('text files', '.txt')]) # asksaveasfile returns a file object
    if new_file is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return # Don't do anything if no file is selected.
    text = str(entry.get(1.0, END)) # get the text from the entry
    new_file.write(text) # write the text to the file
    new_file.close() # close the file

def openFile(): # Open the file
    file = askopenfile(mode = "r", filetypes = [('text files', '*.txt')]) # askopenfile returns a file object
    if file is not None: # if no file is selected, file is `None`
        content = file.read() # read the contents of the file
        entry.insert(INSERT, content) # insert the content of the file into the entry

def clearFile(): # Clear the file
    entry.delete(1.0, END) # delete the text from the entry beginning at 1.0 and ending at END

# Define our UI (User Interface)
canvas = tk.Tk()
# Define geometry size of canvas
canvas.geometry("400x500")
# Set the title of the canvas
canvas.title("TJ's Note App")
# Define color of canvas --> "white"
canvas.configure(bg='white')
# Create a frame and add buttons to that frame store in top variable
top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor = 'n') # anchor = nw to pack in top left corner
# Create buttons store in variable b1 and b25
b1 = Button(canvas, text = "Open", bg= "white", command = openFile) # command = function to call
# Pack the created button
b1.pack(in_ = top, side=LEFT)
# Create buttons store in variable b1 and b2, and b3
b2 = Button(canvas, text = "Save", bg= "white", command=saveFile) # command = function to call
# Pack the created button
b2.pack(in_ = top, side=LEFT)
# Create buttons store in variable b1 and b2
b3 = Button(canvas, text = "Clear", bg= "white", command=clearFile) # command = function to call
# Pack the created button
b3.pack(in_ = top, side=LEFT)
# Create buttons store in variable b1 and b2
b4 = Button(canvas, text = "Exit", bg= "white", command=exit) # exit function is defined in the main program
# Pack the created button
b4.pack(in_ = top, side=LEFT)

# Create an Entry
entry = Text(canvas, wrap=WORD, bg= "#F9DDA4", font = ("poppins", 15)) # wrap = WORD to wrap text next line
# Pack the entry
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH) # expand = TRUE to expand to fill space both x and y coordinates.


# Loop to start the canvas // TEST
canvas.mainloop()
