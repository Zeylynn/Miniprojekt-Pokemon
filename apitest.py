import requests

# Daten von der PokeAPI holen
ditto_response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
pikachu_response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

if ditto_response.status_code == 200 and pikachu_response.status_code == 200:
    ditto_data = ditto_response.json()
    pikachu_data = pikachu_response.json()

    ditto_hp = ditto_data["stats"][0]["base_stat"]
    ditto_attack = ditto_data["stats"][1]["base_stat"]

    pikachu_hp = pikachu_data["stats"][0]["base_stat"]
    pikachu_attack = pikachu_data["stats"][1]["base_stat"]

    print(f"Ditto: {ditto_hp}HP, {ditto_attack}-Damage")
    print(f"Pikachu: {pikachu_hp}HP, {pikachu_attack}-Damage")
    print("\n")


    # Kampf-Runden
    while ditto_hp > 0 and pikachu_hp > 0:
        # Ditto greift Pikachu an
        pikachu_hp -= ditto_attack
        if pikachu_hp <= 0:
            pikachu_hp = 0
        print(f"Ditto greift an. Pikachu hat noch {pikachu_hp} HP")

        if pikachu_hp <= 0:
            print("Ditto gewinnt!")
            break

        # Pikachu greift Ditto an
        ditto_hp -= pikachu_attack
        if ditto_hp <= 0:
            ditto_hp = 0
        print(f"Pikachu greift an. Ditto hat noch {ditto_hp} HP")

        if ditto_hp <= 0:
            print("Pikachu gewinnt!")
            break