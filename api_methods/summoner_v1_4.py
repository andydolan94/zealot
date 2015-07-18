from models import summoner
import requests

__author__ = 'Andrew'


def get_summoner_by_name(api_key, input_name, region):
    """
    Creates a summoner object from the API GET method:
        /api/lol/{region}/v1.4/summoner/by-name/{summonerNames}
    :param api_key:
    :param input_name:
    :param region:
    :return new_summoner:
    """

    # The URL from where the summoner information was obtained
    url = "https://" + region.slug + ".api.pvp.net/api/lol/" + region.slug + "/v1.4/summoner/by-name/" + input_name \
          + "?api_key=" + api_key

    # Create an empty summoner
    new_summoner = summoner.Summoner()

    # The response
    response = requests.get(url)

    # If the response is healthy...
    if response.status_code == 200:

        # Set the summoner information
        new_summoner.id = response.json()[input_name]["id"]
        new_summoner.name = response.json()[input_name]["name"]
        new_summoner.profile_icon_id = response.json()[input_name]["profileIconId"]
        new_summoner.revision_date = response.json()[input_name]["revisionDate"]
        new_summoner.level = response.json()[input_name]["summonerLevel"]

    return new_summoner, response
