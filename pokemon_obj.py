class Pokemon:
    def __init__(self):
        self.__name = None
        self.__sprite = None
        self.__type = None          # TODO Soll ich doppeltypen unterstützen? => Glaub nicht sonst Liste statt string
        self.__attacks = []

        self.__currenthp = None

        # STATS
        self.__hp = None            #1
        self.__attack = None        #2
        self.__sp_attack = None     #3
        self.__defense = None       #4
        self.__sp_defense = None    #5
        self.__speed = None         #6
        
    def get_name(self):
        return self.__name

    def get_currenthp(self):
        return self.__currenthp
    
    def set_currenthp(self, amount):
        self.__currenthp = amount

    def get_sprite(self):
        return self.__sprite

    def get_type(self):
        return self.__type

    def get_stats(self):
        return {
            "HP": self.__hp,
            "Attack": self.__attack,
            "Defense": self.__defense,
            "Sp. Attack": self.__sp_attack,
            "Sp. Defense": self.__sp_defense,
            "Speed": self.__speed
        }

    def get_attacks(self):
        return self.__attacks

    # zum setzen(daten sind ja privat)
    def set_data(self, name, sprite, types, stats, attacks):
        self.__name = name
        self.__sprite = sprite
        self.__type = types
        self.__hp = stats["hp"]
        self.__attack = stats["attack"]
        self.__defense = stats["defense"]
        self.__sp_attack = stats["special-attack"]
        self.__sp_defense = stats["special-defense"]
        self.__speed = stats["speed"]
        self.__attacks = attacks
        self.__currenthp = self.__hp

        
    def __str__(self):
        stats = self.get_stats()
        return (
            f"{self.get_name()} | Typen: {', '.join(self.get_type())}\n"
            f"  HP: {stats['HP']}, Atk: {stats['Attack']}, Def: {stats['Defense']}, "
            f"SpAtk: {stats['Sp. Attack']}, SpDef: {stats['Sp. Defense']}, Speed: {stats['Speed']}\n"
            f"  Attacken: {', '.join(self.get_attacks())}"
        )
    __repr__ = __str__