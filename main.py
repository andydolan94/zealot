import queue

import view
import model
import events

__author__ = 'Andrew'


class MainController:
    def __init__(self, master):
        """
        Initialisation of the controller as a whole; handles the thread queue, view and model
        :param master:
        :return:
        """

        # Creating an instance of master for the periodic call function
        self.master = master

        # Here, we are creating a queue for asynchronous communication between threads
        self.queue = queue.Queue()

        # Initialise the model before anything else
        self.model = model.Model()

        # Initialise the GUI
        self.view = view.View(master, self.queue, self.event_handler)

        # Initialise the periodic call running variable
        self.running = True

        # Start the periodic call in the GUI to check if the queue contains anything
        self.periodic_call()

    def event_handler(self, event):
        """
        Takes an event and assigns a task depending on what event took place
        :param event:
        :return:
        """

        if event.widget.widgetName == "submit button":
            events.submit_select_event(self.model, self.view, self.queue)
        elif event.widget.widgetName == "enter key":
            events.submit_select_event(self.model, self.view, self.queue)
        elif event.widget.widgetName == "get game":
            events.get_game_select_event(self.model, self.queue)
        else:
            events.no_event_assigned(self.queue)

    def periodic_call(self):
        """
        Check every 100 ms if there is something new in the queue
        :return:
        """

        # update_view() check
        self.view.update_view()

        # If the program is not running
        if not self.running:
            import sys
            sys.exit(0)  # Close the program w/ exit code 0

        # Call this function after 100 ms
        self.master.after(100, self.periodic_call)
