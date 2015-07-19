from tkinter import *

__author__ = 'Andrew'


def view_game(participants):
    master = Tk()
    master.title("Current Game")
    master.tk_setPalette(background='white', foreground='black', activeBackground='black',
                         activeForeground='white')

    frame_base = Frame(master)
    frame_base.pack()

    labels = []
    grid_counter = [0, 0]

    for participant in participants:

        if participant.team_id == 100:
            labels.append(Label(frame_base, text=participant.name, fg='blue'))
            labels[-1].grid(row=grid_counter[0], column=0)
            grid_counter[0] += 1
        elif participant.team_id == 200:
            labels.append(Label(frame_base, text=participant.name, fg='red'))
            labels[-1].grid(row=grid_counter[1], column=1)
            grid_counter[1] += 1

    # Loop it!
    master.mainloop()
