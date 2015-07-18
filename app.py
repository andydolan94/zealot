import tkinter
import main

__author__ = 'Andrew'

# Defining the window
root = tkinter.Tk()

root.title("Project Zealot")
root.tk_setPalette(background='white', foreground='black',
                   activeBackground='black', activeForeground='white')

app = main.MainController(root)
root.mainloop()
