import api_handler as API
import pokemon_builder as pkmb

api_handler = API.API_Handler()
builder = pkmb.PokemonBuilder()
pikachu = builder.build("reuniclus")

print(pikachu.get_attacks())
print(pikachu.get_sprite())
print(pikachu.get_stats())
print(pikachu.get_type())