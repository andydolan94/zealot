import threading

__author__ = 'Andrew'


def submit_select_event(model, view, queue):
    """
    This event is triggered to retrieve the summoner info from the input
    :param model:
    :param view:
    :param queue:
    :return:
    """

    # Name and region from the view input
    name = view.summoner_name_entry.get()
    region = view.region_var.get()

    # The thread
    submit_press_event_thread = threading.Thread(target=model.retrieve_summoner_info)
    submit_press_event_thread._args = (queue, name, region)
    submit_press_event_thread.start()


def get_game_select_event(model, queue):
    """
    This event is triggered to retrieve all the other summoners in the entered summoner's game
    :return:
    """

    # The thread
    get_game_event_thread = threading.Thread(target=model.retrieve_other_summoners)
    get_game_event_thread._args = (queue,)
    get_game_event_thread.start()


def no_event_assigned(queue):
    """
    This event is triggered when an unknown input has been made
    :param queue:
    :return:
    """

    # Return error to the status bar
    put_list = ["update status bar", "Oops, something went wrong - please contact the developer about this issue",
                "red"]
    queue.put(put_list)
