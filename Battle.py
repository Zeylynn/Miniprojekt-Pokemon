import api_handler as API
import pokemon_builder as PokeBuild
import random

class Kampf:
    def __init__(self):
        # Host fangt immer an
        self.trainerHost = []
        self.trainerClient = []

        self.api_handler = API.API_Handler()
        self.builder = PokeBuild.PokemonBuilder(self.api_handler)

        self.createPlayerTeams()
        
    def createPlayerTeams(self):
        # TODO auf nationalen Pokedex umstellen damit ich keine Mega Formen etc. habe
        for i in range(6):
            self.trainerHost.append(self.builder.build(str(random.randint(1, 1000))))
            self.trainerClient.append(self.builder.build(str(random.randint(1, 1000)))) 

    def bestimme_angreifer(self):
        # Speed Werte aus den Stats rausziehen yk
        speed1 = self.pokemon1.stats["speed"]
        speed2 = self.pokemon2.stats["speed"]
        
        if speed1 > speed2:
            return self.pokemon1, self.pokemon2
        elif speed2 > speed1:
            return self.pokemon2, self.pokemon1
        else:
            return random.choice([(self.pokemon1, self.pokemon2), (self.pokemon2, self.pokemon1)])

    def start(self):
        print(f"Kampf startet zwischen {self.pokemon1.name} und {self.pokemon2.name}!\n")
        
        while True:
            attacker1, attacker2 = self.bestimme_angreifer()
            self.display_status()

            # Erster Angrif
            move1 = self.choose_attack(attacker1)
            damage1 = self.calculate_damage(attacker1, attacker2, move1)
            self.apply_damage(attacker2, damage1)
            print(f"{attacker1.name} greift mit {move1} an und verursacht {damage1} Schaden!")

            if attacker2.stats["hp"] <= 0:
                print(f"{attacker2.name} wurde besiegt! {attacker1.name} gewinnt!\n")
                break

            # Zweiter Angriff
            move2 = self.choose_attack(attacker2)
            damage2 = self.calculate_damage(attacker2, attacker1, move2)
            self.apply_damage(attacker1, damage2)
            print(f"{attacker2.name} greift mit {move2} an und verursacht {damage2} Schaden!")

            if attacker1.stats["hp"] <= 0:
                print(f"{attacker1.name} wurde besiegt! {attacker2.name} gewinnt!\n")
                break

    def display_status(self):
        print(f"{self.pokemon1.name}: {self.pokemon1.stats['hp']} HP")
        print(f"{self.pokemon2.name}: {self.pokemon2.stats['hp']} HP\n")

    def choose_attack(self, pokemon):
        print(f"{pokemon.name}, wähle eine Attacke:")
        for i, move in enumerate(pokemon.moves, 1):
            print(f"{i}: {move}")
    
        while True:
            choice = input("Deine Wahl (1-4): ")
            if choice in ['1','2','3','4']:
                return pokemon.moves[int(choice)-1]
            print("Ungültig! Bitte 1-4 eingeben.")

    def calculate_damage(self, attacker, defender, move):
        # Verwende die Attack- und Defense-Werte aus dem Dictionary
        base_attack = attacker.stats["attack"]
        base_defense = defender.stats["defense"]
        random_factor = random.randint(10, 20)
        damage = max(1, int((base_attack / base_defense) * random_factor))
        return damage

    def apply_damage(self, defender, damage):
        defender.stats["hp"] = max(0, defender.stats["hp"] - damage)

kampf = Kampf()
kampf.start()