from utilities import verify
from utilities import clean

from api_methods import summoner_v1_4
from api_methods import current_game_v1_0
from models import data_dragon
from models import summoner
from data import region_data

__author__ = 'Andrew'


class Model:
    """
    NOTE: ALL FUNCTIONS INSIDE THIS MODEL ARE CALLED VIA THREADS
    Handles everything in terms of api_methods, mainly calling functions within the api_methods
    """

    def __init__(self):
        """
        Constructor for Model object
        :return:
        """

        # Riot developer API key
        self.api_key = "348d54f6-1599-431e-9fea-373ec5c65325"

        # Default summoner name the model uses
        self.name = ""

        # Default summoner for the user
        self.summoner = summoner.Summoner()

        # Default participants involved in current game
        self.participants = None

        # Default region the model uses (Explicitly Oceania)
        self.region = region_data.get_region_by_slug('oce')

        # Versions (version numbers for various requests and information)
        self.versions = None

    def retrieve_summoner_info(self, queue, name, region):
        """
        This function tells the api_methods to collect information from the internet and return them to here. After
        that, basic data manipulation occurs and then it is sent to the queue for the app to manage
        :param name:
        :param region:
        :return:
        """

        # Set the name to the one specified by the user
        self.name = clean.clean(name)

        # Set the region to the one specified by the user
        self.region = region_data.get_region_by_slug(region)

        # Check if the name is valid
        [name_is_valid, reason] = verify.is_name_valid(self.name)

        # If the username is not valid...
        if not name_is_valid:

            # Update the status bar
            put_list = ["update status bar", reason, "red"]
            queue.put(put_list)
            return  # Exit the function

        # Update status bar
        put_list = ["update status bar", "Getting info...", "dark orange"]
        queue.put(put_list)

        # Obtain a summoner
        self.summoner, response = summoner_v1_4.get_summoner_by_name(self.api_key, self.name, self.region)

        # Update the version from the selected region
        self.versions = data_dragon.Versions(self.region)

        # If response is healthy...
        if response.status_code == 200:

            # Obtain the image
            summoner_icon = data_dragon.SummonerIcon(self.versions.profile_icon_version, self.summoner.profile_icon_id)

            # Save the image locally
            with open(summoner_icon.file, 'wb') as f:
                for chunk in summoner_icon.response.iter_content(512):
                    f.write(chunk)

            # Send the updated information to the GUI
            put_list = ["update summoner data", str(self.summoner.level)]
            queue.put(put_list)

            # Update the status bar
            put_list = ["update status bar", "Obtained summoner: " + self.summoner.name, "green"]
            queue.put(put_list)

        # Otherwise...
        else:

            # Display reason in the status bar
            put_list = ["update status bar", response.reason, "red"]
            queue.put(put_list)

    def retrieve_other_summoners(self, queue):
        """
        This function collects all the summoners that are currently in the same game as the player and displays
        information about those summoners
        :param queue:
        :return:
        """

        # Update status bar
        put_list = ["update status bar", "Searching for game...", "dark orange"]
        queue.put(put_list)

        # Obtain the participants and the response
        self.participants, response = current_game_v1_0.get_participants(self.api_key, self.summoner.id, self.region)

        # If response is healthy...
        if response.status_code == 200:

            # Print each participants user name
            for participant in self.participants:
                print(participant.name + str(participant.runes))

            # Alert the user
            put_list = ["update status bar", "Game found!", "green"]
            queue.put(put_list)

        # If the player is currently not in game...
        elif response.status_code == 404:

            # Alert the user
            put_list = ["update status bar", "Summoner is currently not in a game", "red"]
            queue.put(put_list)

        # Otherwise...
        else:

            # Display reason in the status Bar
            put_list = ["update status bar", response.reason, "red"]
            queue.put(put_list)
