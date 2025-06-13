import api_handler as API
import pokemon_builder as PokeBuild
import random

class BattleCore:
    def __init__(self):
        # Initialisiert den Pokémon-Builder mit einem API-Handler
        self.builder = PokeBuild.PokemonBuilder(API.API_Handler())
        # Speichert die Pokémon-Teams für Host und Client
        self.trainer_teams = {
            "host": [],
            "client": []
        }
        # Speichert die aktuell aktiven Pokémon
        self.active_pokemon = {
            "host": None,
            "client": None
        }

    def create_teams(self):
        # Erstellt zufällige Teams mit je 6 Pokemon für Host und Client
        for _ in range(6):
            self.trainer_teams["host"].append(self.builder.build(str(random.randint(1, 100))))
            self.trainer_teams["client"].append(self.builder.build(str(random.randint(1, 100))))

    def set_active_pokemon(self, side, index):
        # Setzt das aktive Pokemon für eine Seite (Host/Client)
        self.active_pokemon[side] = self.trainer_teams[side][index]

    def get_team_names(self):
        # Gibt die Namen aller Pokemon im Team zurück (für die Anzeige)
        host_names = [poke.get_name() for poke in self.trainer_teams["host"]]
        client_names = [poke.get_name() for poke in self.trainer_teams["client"]]
        return {"host": host_names, "client": client_names}

    def get_current_status(self):
        # Gibt den aktuellen Kampfstatus (Namen und HP der aktiven Pokemon) zurück
        return {
            "host": {
                "name": self.active_pokemon["host"].get_name(),
                "hp": self.active_pokemon["host"].get_currenthp()
            },
            "client": {
                "name": self.active_pokemon["client"].get_name(),
                "hp": self.active_pokemon["client"].get_currenthp()
            }
        }

    def get_active(self, side):
        # Gibt das aktive Pokemon einer Seite zurück
        return self.active_pokemon[side]

    def determine_turn_order(self):
        # Bestimmt die Reihenfolge der Züge basierend auf der Geschwindigkeit 
        h = self.active_pokemon["host"]
        c = self.active_pokemon["client"]
        s_host = h.get_stats()["Speed"]
        s_client = c.get_stats()["Speed"]
        if s_host > s_client:
            return ["host", "client"]
        elif s_client > s_host:
            return ["client", "host"]
        else:
            return random.sample(["host", "client"], 2)  # Zufällige Reihenfolge bei Gleichstand

    def resolve_turn(self, host_move_idx, client_move_idx):
        # Verarbeitet einen Kampfzug:
        # 1. Bestimmt die Zugreihenfolge
        # 2. Wendet Schaden an
        # 3. Gibt Ergebnis zurück (Log + Status)
        move_indices = {"host": host_move_idx, "client": client_move_idx}
        turn_order = self.determine_turn_order()
        log = []

        for side in turn_order:
            attacker = self.active_pokemon[side]
            defender_side = "client" if side == "host" else "host"
            defender = self.active_pokemon[defender_side]

            if attacker.get_currenthp() <= 0:
                continue  # Überspringt besiegtes Pokémon

            move_idx = move_indices[side]
            moves = attacker.get_attacks()
            move = moves[move_idx] if move_idx < len(moves) else moves[0]  # Fallback auf erste Attacke

            damage = self.calculate_damage(attacker, defender, move)
            self.apply_damage(defender, damage)

            log.append(f"{attacker.get_name()} greift mit {move} an und verursacht {damage} Schaden!")
            if defender.get_currenthp() <= 0:
                log.append(f"{defender.get_name()} wurde besiegt!")
                self.auto_switch(defender_side)  # Automatischer Wechsel

        return {"log": log, "status": self.get_current_status()}

    def calculate_damage(self, attacker, defender, move, rng=None):
        # Berechnet den Schaden basierend auf Attacke/Verteidigung und Zufallsfaktor
        atk = attacker.get_stats()["Attack"]
        deff = defender.get_stats()["Defense"]
        rng = rng if rng is not None else random.randint(10, 20)
        return max(1, int((atk / max(1, deff)) * rng))

    def apply_damage(self, defender, damage):
        # Reduziert die HP des Verteidigers
        defender.set_currenthp(max(0, defender.get_currenthp() - damage))

    def auto_switch(self, side):
        # Wechselt automatisch zum nächsten lebenden Pokémon
        for idx, p in enumerate(self.trainer_teams[side]):
            if p.get_currenthp() > 0:
                self.set_active_pokemon(side, idx)
                return
        self.active_pokemon[side] = None  # Kein Pokémon mehr übrig

    def is_battle_over(self):
        # Überprüft, ob der Kampf vorbei ist
        return self.active_pokemon["host"] is None or self.active_pokemon["client"] is None

    def switch_pokemon(self, side, index):
        # Manueller Pokémon-Wechsel (wird aktuell nicht genutzt)
        selected = self.trainer_teams[side][index]
        if selected.get_currenthp() > 0:
            self.active_pokemon[side] = selected
            return True
        return False