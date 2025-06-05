import pokemon_obj as Pokemon
import random

class PokemonBuilder:
    def __init__(self, handler):
        self.api_handler = handler  # Damit man den Handler durch einen Fake-Handler ersetzen soll

    def build(self, name):
        data = self.api_handler.get_pokemon_data(name)

        name = data["name"]         # falls man mit zahlen statt namen builded
        # Daten aus Dictionary "filtern"
        sprite = data["sprites"]["front_default"]

        types = []
        for type in data["types"]:
            types.append(type["type"]["name"])

        stats = {}
        for stat in data["stats"]:
            stat_name = stat["stat"]["name"]
            stat_value = stat["base_stat"]
            stats[stat_name] = stat_value

        selected_moves = self.get_random_attacks(data, 4)

        # Objekt erstellen
        pokemon = Pokemon.Pokemon()
        pokemon.set_data(name, sprite, types, stats, selected_moves)
        return pokemon

    def get_random_attacks(self, data, count):
        all_moves = []
        for move in data["moves"]:
            all_moves.append(move["move"]["name"])

        # Durch Sample kann es keine Dopplungen in Attacken geben
        # TODO so machen dass es auch unter 4 Moves sein können
        return random.sample(all_moves, count)
