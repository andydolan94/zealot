from tkinter import *

__author__ = 'Andrew'


def view_game(participants):
    """
    Creates a new window to display the current participants involved in the corresponding match
    :param participants:
    :return:
    """
    master = Tk()
    master.title("Current Game")
    master.tk_setPalette(background='white', foreground='black', activeBackground='black',
                         activeForeground='white')

    # Creating the base frame
    frame_base = Frame(master)
    frame_base.pack()

    # Label list of names displayed on window
    name_labels = []
    champ_labels = []
    grid_counter = [0, 0]

    # For each participant...
    for participant in participants:

        # Display the participant + champion on the left side IF they are on blue team
        if participant.team_id == 100:

            # Name
            name_labels.append(Label(frame_base, text=participant.name, fg='blue'))
            name_labels[-1].grid(row=grid_counter[0], column=0)

            # Champion
            champ_labels.append(Label(frame_base, text=participant.current_champion.name))
            champ_labels[-1].grid(row=grid_counter[0], column=1)

            # Increment counter
            grid_counter[0] += 1

        # Display the participant on the right side IF they are on red team
        elif participant.team_id == 200:

            # Name
            name_labels.append(Label(frame_base, text=participant.name, fg='red'))
            name_labels[-1].grid(row=grid_counter[1], column=3)

            # Champion
            champ_labels.append(Label(frame_base, text=participant.current_champion.name))
            champ_labels[-1].grid(row=grid_counter[1], column=2)

            # Increment counter
            grid_counter[1] += 1

    # Loop it!
    master.mainloop()
