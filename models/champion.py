__author__ = 'Andrew'


class Champion:
    """
    "Morgana":  {"version":"5.2.1",

                "id":"Morgana",

                "key":"25",

                "name":"Morgana",

                "title":"Fallen Angel",

                "blurb":
                    "There is a world far away populated by graceful and beautiful winged beings gifted with
                immortality, where an ancient conflict still rages. Like so many conflicts, this war split families. One
                side proclaimed themselves as beings of perfect order and ...",

                "info":
                    {"attack":1,"defense":6,"magic":8,"difficulty":1},

                "image":
                    {"full":"Morgana.png","sprite":"champion2.png","group":"champion","x":96,"y":0,"w":48,"h":48},

                "tags":
                    ["Mage","Support"],

                "partype":"Mana",

                "stats":
                    {"hp":547.48,"hpperlevel":86.0,"mp":340.8,"mpperlevel":60.0,"movespeed":335.0,"armor":25.384,
                    "armorperlevel":3.8,"spellblock":30.0,"spellblockperlevel":0.0,"attackrange":450.0,"hpregen":5.705,
                    "hpregenperlevel":0.6,"mpregen":6.0,"mpregenperlevel":0.8,"crit":0.0,"critperlevel":0.0,
                    "attackdamage":55.46,"attackdamageperlevel":3.5,"attackspeedoffset":0.0,"attackspeedperlevel":1.53}}
    """

    def __init__(self):
        self.version = None
        self.id = None
        self.key = None
        self.name = None
        self.title = None
        self.blurb = None
        self.info = None
        self.image = None
        self.tags = None
        self.partype = None
        self.stats = None
