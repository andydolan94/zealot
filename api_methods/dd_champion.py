from models import champion
import requests

__author__ = 'Andrew'


def get_champions_by_participants(_participants, version, language):

    # URL
    url = "http://ddragon.leagueoflegends.com/cdn/" + str(version) + "/data/" + language + "/champion.json"

    # The response
    response = requests.get(url)

    # If the response is healthy...
    if response.status_code == 200:

        # For each ID in the ID list...
        for participant in _participants:

            # Create a champion
            participant.current_champion = champion.Champion()

            # Assign the key
            participant.current_champion.key = participant.champion_id

            for key, value in response.json()['data'].items():
                if int(value['key']) == participant.current_champion.key:

                    # Assign all the other attributes
                    participant.current_champion.version = value['version']
                    participant.current_champion.id = value['id']
                    participant.current_champion.name = value['name']
                    participant.current_champion.title = value['title']
                    participant.current_champion.blurb = value['blurb']
                    participant.current_champion.info = value['info']
                    participant.current_champion.image = value['image']
                    participant.current_champion.tags = value['tags']
                    participant.current_champion.partype = value['partype']
                    participant.current_champion.stats = value['stats']
