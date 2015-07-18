__author__ = 'Andrew'


def get_summoners(api_key, summoner_id, region):

    # The URL from where the summoner information was obtained
    url = "https://" + region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/" + platform_id + "/" + summoner_id + "?api_key=" + api_key