import os
import requests

__author__ = 'Andrew'


class SummonerIcon:
    """
    For creating a summoner icon object containing all the information about a summoner icon
    """

    def __init__(self, version, profile_icon_id):
        """
        Constructor for SummonerIcon object
        :param version:
        :param profile_icon_id:
        :return:
        """
        # The version
        self.version = version

        # The profile icon ID
        self.profile_icon_id = profile_icon_id

        # The URL from where the summoner icon was obtained
        self.url = "http://ddragon.leagueoflegends.com/cdn/" + str(self.version) + "/img/profileicon/" \
                   + str(self.profile_icon_id) + ".png"

        # The response
        self.response = requests.get(self.url)

        # The file itself that will be stored locally
        self.file = os.path.join(os.path.dirname(__file__), '../images/summoner_icon.png')


class Versions:
    """
    For creating a Versions object containing all the latest versions for Data Dragon's realms and all of the
    versions for League of Legends dating back all the way back to "lolpatch_3.7".
    """

    def __init__(self, region):
        """
        Constructor for Versions object
        :param region:
        :return:
        """

        # The region
        self.region = region

        # The URL that contains all the realms and their current versions
        self.realms_endpoint_url = "https://ddragon.leagueoflegends.com/realms/" + self.region.slug + ".json"

        # The response from the realms endpoint url
        self.realms_endpoint_response = requests.get(self.realms_endpoint_url)

        # The URL that contains all the versions for League of Legends
        self.versions_endpoint_url = "https://ddragon.leagueoflegends.com/api/versions.json"

        # Getting the profile icon version
        self.profile_icon_version = self.get_json_object_value("profileicon")

        # Getting the champion version
        self.champion_version = self.get_json_object_value("champion")

    def get_json_object_value(self, key):
        """
        Takes a key which decides what value is required and returns the value of that key in the json object
        :param key:
        :return:
        """

        # Getting the raw json data
        data = self.realms_endpoint_response.json()

        # Extraction of the json object
        # E.g. json object: { n:{ key:value, key:value } }
        json_object = data["n"]

        return json_object[key]
