import socket
import json
from battle_core import BattleCore

class HostGame:
    def __init__(self, host="0.0.0.0", port=12345):
        # Initialisiert Host mit Standardwerten und BattleCore Instanz
        self.host = host
        self.port = port
        self.sock = None  # Haupt-Socket
        self.conn = None  # Client-Verbindung
        self.addr = None  # Client-Adresse
        self.team = []  # Team-Namen
        self.battle = BattleCore()  # Kampflogik

    def start_server(self):
        # Erstellt Socket, bindet an Port und wartet auf Client
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print("Warte auf Client...")
        self.conn, self.addr = self.sock.accept()
        print(f"Client verbunden: {self.addr}")

        # Liest erste Nachricht vom Client (Handshake)
        data = self.conn.recv(1024).decode()
        print("Client sagt:", data)

    def send(self, data):
        # Sendet Daten als JSON an Client
        self.conn.send(json.dumps(data).encode())

    def receive(self):
        # Empfängt JSON-Daten vom Client
        return json.loads(self.conn.recv(4096).decode())

    def run_battle(self):
        # Initialisiert Teams und aktive Pokémon
        self.battle.create_teams()
        self.battle.set_active_pokemon("host", 0)
        self.battle.set_active_pokemon("client", 0)

        # Sendet Team-Namen an Client
        self.send(self.battle.get_team_names())

        # Hauptkampfschleife
        while True:
            # Zeigt aktuellen Status an
            print("Status:", self.battle.get_current_status())

            # Holt aktives Pokémon
            host_poke = self.battle.get_active("host")

            # Empfängt Team vom Client für Anzeige
            # Zeigt Attacken und fragt Eingabe ab
            print("\nWähle deine Attacke:")
            for i, move in enumerate(host_poke.get_attacks()):
                print(f"{i+1}: {move}")
            move_host = int(input("Wähle Attacke (1-4): ")) - 1

            # Empfängt Client-Attacke
            move_client = self.receive()["move"]

            # Verarbeitet Zug und sendet Ergebnis
            result = self.battle.resolve_turn(move_host, move_client)
            self.send(result)

            # Zeigt Kampflog an
            print("\n".join(result["log"]))

            # Beendet Schleife wenn Kampf vorbei
            if self._battle_over(result["status"]):
                print("Kampf beendet.")
                break

        # Schließt Verbindungen
        self.conn.close()
        self.sock.close()

    def _battle_over(self, status):
        # Prüft ob ein Pokémon besiegt wurde
        return status["host"]["hp"] <= 0 or status["client"]["hp"] <= 0

if __name__ == "__main__":
    # Startet das Spiel wenn direkt ausgeführt
    game = HostGame()
    game.start_server()
    game.run_battle()