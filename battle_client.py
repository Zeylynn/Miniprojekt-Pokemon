import socket
import json

class ClientGame:
    def __init__(self, host="192.168.1.196", port=12345):
        # Initialisiert Client mit Socket-Einstellungen
        self.host = host
        self.port = port
        self.sock = None
        self.team = []  # Pokemon-Team des Clients

    def connect_to_host(self):
        # Verbindet mit dem Host-Server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        print("Verbunden mit dem Server!")
        self.sock.send(json.dumps({"msg": "ready"}).encode())  # Bestätigung senden

    def send(self, data):
        # Sendet Daten als JSON an Host
        self.sock.send(json.dumps(data).encode())

    def receive(self):
        # Empfängt Daten vom Host als JSON
        return json.loads(self.sock.recv(4096).decode())

    def play(self):
        # Hauptkampfschleife des Clients
        self.team = self.receive()["client"]  # Team-Namen empfangen
        print("Dein Team:")
        for name in self.team:
            print(f"- {name}")

        while True:
            # Client wählt Attacke
            print("\nWähle deine Attacke:")
            for i in range(4):
                print(f"{i+1}: Attacke {i+1}")
            move_index = int(input("Wähle Attacke (1-4): ")) - 1
            self.send({"move": move_index})

            # Ergebnis des Zuges vom Host empfangen und anzeigen
            result = self.receive()
            print("\n".join(result["log"]))

            if self._battle_over(result["status"]):
                print("Kampf beendet.")
                break

        self.sock.close()

    def _battle_over(self, status):
        # Überprüft, ob der Kampf vorbei ist (HP <= 0)
        return status["host"]["hp"] <= 0 or status["client"]["hp"] <= 0

if __name__ == "__main__":
    client = ClientGame()
    client.connect_to_host()  # Verbindung herstellen
    client.play()            # Kampf starten