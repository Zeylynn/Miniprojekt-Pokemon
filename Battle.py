import api_handler as API
import pokemon_builder as PokeBuild
import random

class Kampf:
    def __init__(self):
        self.trainerHost = []
        self.trainerClient = []

        self.api_handler = API.API_Handler()
        self.builder = PokeBuild.PokemonBuilder(self.api_handler)

        self.createPlayerTeams()

    def createPlayerTeams(self):
        for i in range(6):
            self.trainerHost.append(self.builder.build(str(random.randint(1, 1000))))
            self.trainerClient.append(self.builder.build(str(random.randint(1, 1000))))

    def bestimme_angreifer(self):
        speed1 = self.pokemon1.get_stats()["Speed"]
        speed2 = self.pokemon2.get_stats()["Speed"]

        if speed1 > speed2:
            return 1
        elif speed2 > speed1:
            return 2
        else:
            return random.choice([1, 2])

    def start(self):
        self.pokemon1 = self.get_next_alive(self.trainerHost)
        self.pokemon2 = self.get_next_alive(self.trainerClient)

        self.show_teams()

        while True:
            if not self.team_alive(self.trainerHost):
                print("TrainerClient gewinnt!")
                break
            if not self.team_alive(self.trainerClient):
                print("TrainerHost gewinnt!")
                break

            who = self.bestimme_angreifer()
            print("\n")
            self.display_status()

            if who == 1:
                self.attack(self.pokemon1, self.pokemon2, self.trainerHost, is_host=True)
                if self.pokemon2.get_currenthp() <= 0:
                    self.pokemon2 = self.get_next_alive(self.trainerClient)
            else:
                self.attack(self.pokemon2, self.pokemon1, self.trainerClient, is_host=False)
                if self.pokemon1.get_currenthp() <= 0:
                    self.pokemon1 = self.get_next_alive(self.trainerHost)

    def attack(self, attacker, defender, team, is_host):
        pokemon, move = self.choose_action(attacker, team)

        if pokemon != attacker:
            if is_host:
                self.pokemon1 = pokemon
            else:
                self.pokemon2 = pokemon
            print(f"{attacker.get_name()} wurde ausgewechselt zu {pokemon.get_name()}.\n")
            return

        if move:
            damage = self.calculate_damage(attacker, defender, move)
            self.apply_damage(defender, damage)
            print(f"{attacker.get_name()} greift mit {move} an und verursacht {damage} Schaden!")

            if defender.get_currenthp() <= 0:
                print(f"{defender.get_name()} wurde besiegt!\n")

    def choose_action(self, pokemon, team):
        print(f"{pokemon.get_name()}, wähle:")
        for i, move in enumerate(pokemon.get_attacks(), 1):
            print(f"{i}: Attacke - {move}")

        for i, teammate in enumerate(team, 5):
            if teammate.get_currenthp() > 0:
                print(f"{i}: Wechsel zu {teammate.get_name()}")

        while True:
            choice = input("Wahl (1-4 Attacke, 5-9 Wechsel): ")
            if choice in ['1', '2', '3', '4']:
                return pokemon, pokemon.get_attacks()[int(choice) - 1]
            if choice in ['5', '6', '7', '8', '9']:
                idx = int(choice) - 5
                if 0 <= idx < len(team) and team[idx].get_currenthp() > 0:
                    return team[idx], None
                else:
                    print("Dieses Pokémon ist K.O. oder existiert nicht.")
            else:
                print("Ungültige Eingabe!")

    def get_next_alive(self, team):
        for poke in team:
            if poke.get_currenthp() > 0:
                return poke
        return None

    def team_alive(self, team):
        return any(p.get_currenthp() > 0 for p in team)

    def display_status(self):
        print(f"{self.pokemon1.get_name()}: {self.pokemon1.get_currenthp()} HP")
        print(f"{self.pokemon2.get_name()}: {self.pokemon2.get_currenthp()} HP\n")

    def calculate_damage(self, attacker, defender, move):
        base_attack = attacker.get_stats()["Attack"]
        base_defense = defender.get_stats()["Defense"]
        random_factor = random.randint(10, 20)
        damage = max(1, int((base_attack / base_defense) * random_factor))
        return damage

    def apply_damage(self, defender, damage):
        new_hp = defender.get_currenthp() - damage
        defender.set_currenthp(max(0, new_hp))

    def show_teams(self):
        print("TrainerHost-Team:")
        for i, poke in enumerate(self.trainerHost, 1):
            print(f"{i}. {poke.get_name()} - {poke.get_currenthp()} HP")

        print("\nTrainerClient-Team:")
        for i, poke in enumerate(self.trainerClient, 1):
            print(f"{i}. {poke.get_name()} - {poke.get_currenthp()} HP")


kampf = Kampf()
kampf.start()