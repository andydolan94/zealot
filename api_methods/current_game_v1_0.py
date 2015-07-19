from models import summoner
import requests

__author__ = 'Andrew'


def get_participants(api_key, summoner_id, region):
    # The URL from where the summoner information was obtained
    url = "https://" + region.slug + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" \
          + region.platform_id + "/" + str(summoner_id) + "?api_key=" + api_key

    # Create a participants list
    participants = []

    # The response
    response = requests.get(url)

    # If the response is healthy...
    if response.status_code == 200:

        # For each participant
        for participant in response.json()["participants"]:

            # Create a new summoner
            new_summoner = summoner.InGameSummoner()

            # Set the summoner information
            new_summoner.id = participant["summonerId"]
            new_summoner.name = participant["summonerName"]
            new_summoner.profile_icon_id = participant["profileIconId"]
            new_summoner.champion_id = participant["championId"]
            new_summoner.bot = participant["bot"]
            new_summoner.team_id = participant["teamId"]
            new_summoner.spell_1_id = participant["spell1Id"]
            new_summoner.spell_2_id = participant["spell2Id"]
            new_summoner.runes = participant["runes"]
            new_summoner.masteries = participant["masteries"]

            # Append the new summoner to the participants list
            participants.append(new_summoner)

    # Return a tuple of the list of participants and the response
    return participants, response
