import requests as req
import random
#all_pokemon_url = "https://pokeapi.co/api/v2/pokemon?offset=1260&limit=20"

# gibt ALLE Pokemon als Liste zurück
def GetAllPokemon(url, all_pokemon):
    # Daten der neuen url/Seite aufrufen
    data = req.get(url).json()
    # Wenn keine nächste Seite nicht mehr Rekursieren
    if type(data["next"]) is str:							
        all_pokemon = GetAllPokemon(data["next"], all_pokemon)
            
    # alle Pokemon der aktuellen Seite der Liste der gesamt Pokemon hinzufügen
    for entry in data["results"]:
        pokemon = [entry["name"], entry["url"]]
        all_pokemon.append(pokemon)
    
    return all_pokemon

# gibt count-anzahl an zufälligen Listen elementen(also sachen die als Liste abgespeichert sind)
# aus der json datenmenge zurück(z.B. Fähigkeiten und Moves)
def GetRandomPokemonListEntry(url, entry_name, singular_entry_name, count):
    data = req.get(url).json()[entry_name]
    
    # alle Einträge in Liste eintragen
    all_entries = []
    for entry in data:
        all_entries.append(entry[singular_entry_name]["name"])
        continue
    
    # Anzahl an zufälligen raussuchen
    pokemon_entries = []
    for i in range(count):
        while True:
            chosen_entry = all_entries[random.randint(0, len(all_entries) - 1)]
            if not (chosen_entry in pokemon_entries):
                pokemon_entries.append(chosen_entry)
                break
        
    return pokemon_entries
    
# gibt alles schön aus
def PrintChosenTeam(team_pokemons):
    for pokemon in team_pokemons:
        print("----------|----------")
        print(f"Name      | {pokemon[0][0]}")
        print(f"Fähigkeit | {pokemon[1][0]}")
        print(f"Moves     | {pokemon[2][0]}")
        print(f"          | {pokemon[2][1]}")
        print(f"          | {pokemon[2][2]}")
        print(f"          | {pokemon[2][3]}")
    
all_pokemon_url = "https://pokeapi.co/api/v2/pokemon"
teamsize = 6

all_pokemon = GetAllPokemon(all_pokemon_url, [])
team_pokemons = []

for i in range(teamsize):
    pokemon = []
    # Pokemon = [[Name, Url]]
    pokemon.append(all_pokemon[random.randint(1, 1281)])
    # Pokemon = [[Name, Url], [Ability]]
    pokemon.append(GetRandomPokemonListEntry(pokemon[0][1], "abilities", "ability", 1))
    # Pokemon = [[Name, Url], [Ability], [Move1, Move2, Move3, Move4]]
    pokemon.append(GetRandomPokemonListEntry(pokemon[0][1], "moves", "move", 4))
    team_pokemons.append(pokemon)
    
PrintChosenTeam(team_pokemons)