import requests
import socket  

class SattleBystem:
    def __init__(self, Player):
        self.Player = Player
        self.connection = None
        self.s = None  # Socket speichern, um später zu schließen

    def SocketHost(self):

        self.s = socket.socket()  
        host = ''  
        port = 12345  
        self.s.bind((host, port))  
        self.s.listen(1)  
        self.connection, client_address = self.s.accept() 
        
        Text = str(input("Test-Nachricht: "))
        self.connection.sendall(Text.encode()) 
                        
    def SocketClient(self):
            
            self.s = socket.socket()
            ip = str(input("IpAdress"))
            self.s.connect((ip, 12345))
            self.connection = self.s  # damit auch client senden kann
            while True:
                x = self.connection.recv(30)
                print(x.decode())

    def Kämpfen(self, PokemonParameter):
        # Werte aus dem Parameter extrahieren
        ditto_hp = PokemonParameter["ditto_hp"]
        ditto_attack = PokemonParameter["ditto_attack"]
        pikachu_hp = PokemonParameter["pikachu_hp"]
        pikachu_attack = PokemonParameter["pikachu_attack"]

        while ditto_hp > 0 and pikachu_hp > 0:
            # Ditto greift Pikachu an
            pikachu_hp -= ditto_attack
            if pikachu_hp <= 0:
                pikachu_hp = 0
            Text = f"Ditto greift an. Pikachu hat noch {pikachu_hp} HP"
            print(Text)
            self.connection.sendall(Text.encode()) 

            if pikachu_hp <= 0:
                Text = "Ditto gewinnt!"
                print(Text)
                self.connection.sendall(Text.encode())
                break

            # Pikachu greift Ditto an
            ditto_hp -= pikachu_attack
            if ditto_hp <= 0:
                ditto_hp = 0
            Text = f"Pikachu greift an. Ditto hat noch {ditto_hp} HP"
            print(Text)
            self.connection.sendall(Text.encode())

            if ditto_hp <= 0:
                Text = "Pikachu gewinnt!"
                print(Text)
                self.connection.sendall(Text.encode())
                break


PokemonParameter = {
    "ditto_hp": 100,
    "ditto_attack": 25,
    "pikachu_hp": 80,
    "pikachu_attack": 30
}
Client = SattleBystem("1")
#Client.SocketClient("192.168.X.X")
Socket = SattleBystem("2")
#Socket.SocketHost()

Socket.Kämpfen(PokemonParameter)

""""
# PokeAPI 
ditto_response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
pikachu_response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")


# Daten umwandeln
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

    # Beispielaufruf (Rolle 1 oder 2 setzen und Methoden entsprechend starten)
    # kampf = SattleBystem("Spieler1", "127.0.0.1")
    # kampf.Sockets(1)
    # kampf.Kämpfen({
    #     "ditto_hp": ditto_hp,
    #     "ditto_attack": ditto_attack,
    #     "pikachu_hp": pikachu_hp,
    #     "pikachu_attack": pikachu_attack
    # })

# Optional: Verbindung schließen
# kampf.connection.close()      
# kampf.s.close()
"""