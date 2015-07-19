__author__ = 'Andrew'


class Summoner:
    """
    For creating a summoner object containing all the information about a summoner
    """

    def __init__(self):
        """
        Constructor for Summoner objects
        :return:
        """
        # Mutual attributes (summoner_v1.4 & current_game_v1.0)
        self.id = None
        self.name = None
        self.profile_icon_id = None

        # summoner_v1.4 attributes
        self.revision_date = None
        self.level = None


class InGameSummoner(Summoner):
    def __init__(self):
        Summoner.__init__(self)

        # current_game_v1.0 attributes
        self.champion_id = None
        self.bot = None
        self.team_id = None
        self.spell_1_id = None
        self.spell_2_id = None
        self.runes = None
        self.masteries = None
