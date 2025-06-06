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
        self.pokemon1 = self.trainerHost[0]
        self.pokemon2 = self.trainerClient[0]

        x = self.show_teams()

        attacker1 = self.pokemon1
        attacker2 = self.pokemon2

        while True:
             
            Who = self.bestimme_angreifer()
            print("\n")
            self.display_status()

            Attacke = self.attack(attacker1, attacker2, Who)
            Which = int(input("Welches Pokemon für den nächsten Angriff: "))
            self.pokemon1 = self.trainerHost[Which-1]
            attacker1 = self.pokemon1

            if Who == 1:
                Who = 2
            else:
                Who = 1 

            Attacke = self.attack(attacker1, attacker2, Who)
            Which = int(input("Welches Pokemon für den nächsten Angriff"))
            self.pokemon2 = self.trainerClient[Which-1]
            attacker2 = self.pokemon2

    def attack(self, attacker1, attacker2, line):
        if line == 1:
            move1 = self.choose_attack(attacker1)
            damage1 = self.calculate_damage(attacker1, attacker2, move1)
            self.apply_damage(attacker2, damage1)
            print(f"{attacker1.get_name()} greift mit {move1} an und verursacht {damage1} Schaden!")

            if attacker2.get_currenthp() <= 0:
                print(f"{attacker2.get_name()} wurde besiegt! {attacker1.get_name()} gewinnt!\n")

        elif line == 2:
            move2 = self.choose_attack(attacker2)
            damage2 = self.calculate_damage(attacker2, attacker1, move2)
            self.apply_damage(attacker1, damage2)
            print(f"{attacker2.get_name()} greift mit {move2} an und verursacht {damage2} Schaden!")

            if attacker1.get_currenthp() <= 0:
                print(f"{attacker1.get_name()} wurde besiegt! {attacker2.get_name()} gewinnt!\n")

    def display_status(self):
        print(f"{self.pokemon1.get_name()}: {self.pokemon1.get_currenthp()} HP")
        print(f"{self.pokemon2.get_name()}: {self.pokemon2.get_currenthp()} HP\n")

    def choose_attack(self, pokemon):
        print(f"{pokemon.get_name()}, wähle eine Attacke:")
        for i, move in enumerate(pokemon.get_attacks(), 1):
            print(f"{i}: {move}")

        while True:
            choice = input("Deine Wahl (1-4): ")
            if choice in ['1', '2', '3', '4']:
                return pokemon.get_attacks()[int(choice) - 1]
            print("Ungültig! Bitte 1-4 eingeben.")

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
            print(f"{i}. {poke}")

        print("\nTrainerClient-Team:")
        for i, poke in enumerate(self.trainerClient, 1):
            print(f"{i}. {poke}")

kampf = Kampf()
kampf.start()
