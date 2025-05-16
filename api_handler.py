import requests

class API_Handler:
    def __init__(self):
        self.__base_url = "https://pokeapi.co/api/v2/pokemon/"
        # in data werden die Daten von Pokemon die schon einmal aufgerufen werden gespeichert damit ich die API nicht überanfrage
        self.__data = {}

    def get_pokemon_data(self, name):
        name = name.lower()
        if name in self.__data:
            return self.__data[name]

        url = f"{self.__base_url}{name}"
        pokemon = requests.get(url).json()

        self.__data[name] = pokemon
        return pokemon