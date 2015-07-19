from views import current_game_view
from tkinter import *

import threading
import queue

__author__ = 'Andrew'


class View:
    def __init__(self, _master, _queue, _action):
        """
        All of the view elements are initialised here. This will change as more elements are added to avoid this
        function from being bloated.
        :param _master:
        :param _queue:
        :param _action:
        :return:
        """

        # Passing in the master, queue and the action

        self.master = _master
        self.queue = _queue
        self.action = _action

        # -------------------------------------------------------------------

        """
        Creating the core frames
            + BASE
            + STATUS BAR
        """
        # Create frames
        self.frame_base = Frame(self.master)
        self.frame_status_bar = Frame(self.master, height=20, bg="light grey")

        # Pack frames
        self.frame_base.pack()
        self.frame_status_bar.pack(side=BOTTOM, fill=X)

        # -------------------------------------------------------------------

        """
        Creating elements in the frames
            - BASE
                + Summoner Name Label
                + Summoner Name Entry       (Entry - typed input)
                + Summoner Region Label
                + Summoner Region Entry     (OptionMenu - user can only input existing regions)
                + Summoner Level Label
                + Summoner Level Entry      (Label - acts as a results element)
                + Submit Button
                + Get Game Button           (Only visible once a summoner has been retrieved)
                + Summoner Icon
            - STATUS BAR
                + Status Bar Message
        """
        # Create View Labels
        self.summoner_name_label = Label(self.frame_base, text="Summoner Name:")
        self.summoner_region_label = Label(self.frame_base, text="Region:")
        self.summoner_level_label = Label(self.frame_base, text="Level:")

        # Create Entry for summoner name
        self.summoner_name_entry = Entry(self.frame_base)
        self.summoner_name_entry.bind("<Return>", self.action)
        self.summoner_name_entry.widgetName = "enter key"

        # Create Drop Down Box for region
        self.region_var = StringVar(self.frame_base)
        self.region_var.set("oce")  # Sets OCE as the default region
        self.summoner_region_entry = OptionMenu(self.frame_base, self.region_var, "oce", "na")

        # Create Entry for level
        self.summoner_level_entry = Label(self.frame_base, text="")

        # Create Submit Button (and give action)
        self.submit_button = Button(self.frame_base, text="Submit")
        self.submit_button.bind("<Button-1>", self.action)
        self.submit_button.widgetName = "submit button"

        # Create Get Game button
        self.get_game_button = Button(self.frame_base, text="Get Current Game")
        self.get_game_button.bind("<Button-1>", self.action)
        self.get_game_button.widgetName = "get game"

        # Create the area for the Summoner Icon
        photo = PhotoImage(file="images/no_summoner_icon.png")
        self.summoner_icon = Label(self.frame_base, image=photo)

        # Create Status Bar message
        self.status_bar_message = Label(self.frame_status_bar, text="Ready", bg="light grey", fg="green")

        # -------------------------------------------------------------------

        """
        Base Grid Layout and Status Bar Packing
        """
        # Labels (left column)
        self.summoner_name_label.grid(row=0, column=1, sticky=E)
        self.summoner_region_label.grid(row=1, column=1, sticky=E)
        self.summoner_level_label.grid(row=2, column=1, sticky=E)

        # Entries (right column)
        self.summoner_name_entry.grid(row=0, column=2)
        self.summoner_region_entry.grid(row=1, column=2)
        self.summoner_level_entry.grid(row=2, column=2)

        # Buttons (last row)
        self.submit_button.grid(row=3, column=1, columnspan=2)

        # Summoner Icon (Left of info)
        self.summoner_icon.grid(row=0, column=0, rowspan=4)
        self.summoner_icon.image = photo

        # Status Bar Message
        self.status_bar_message.pack(side=LEFT)

        # -------------------------------------------------------------------

    def update_view(self):
        """
        Handle all the messages currently in the queue (if any).
        :return:
        """
        while self.queue.qsize():
            try:
                queue_item = self.queue.get(0)
                if queue_item[0] == "update status bar":
                    self.status_bar_message.destroy()
                    self.status_bar_message = Label(self.frame_status_bar, text=queue_item[1], bg="light grey",
                                                    fg=queue_item[2])
                    self.status_bar_message.pack(side=LEFT)
                elif queue_item[0] == "update summoner data":
                    # Summoner Level
                    self.summoner_level_entry.destroy()
                    self.summoner_level_entry = Label(self.frame_base, text=queue_item[1])
                    self.summoner_level_entry.grid(row=2, column=2)

                    # Summoner Icon
                    self.summoner_icon.destroy()
                    photo = PhotoImage(file="images/summoner_icon.png")
                    self.summoner_icon = Label(self.frame_base, image=photo)
                    self.summoner_icon.grid(column=0, row=0, rowspan=4)
                    self.summoner_icon.image = photo

                    # Submit button shift <--
                    self.submit_button.destroy()
                    self.submit_button = Button(self.frame_base, text="Submit")
                    self.submit_button.bind("<Button-1>", self.action)
                    self.submit_button.widgetName = "submit button"
                    self.submit_button.grid(row=3, column=1)

                    # Place the "Get Game" button into the grid
                    self.get_game_button.grid(row=3, column=2)

                elif queue_item[0] == "update current game":
                    # Create a new window via thread
                    current_game_win_thread = threading.Thread(target=current_game_view.view_game)
                    current_game_win_thread._args = ([queue_item[1]])
                    current_game_win_thread.start()

            except queue.Empty:
                pass
