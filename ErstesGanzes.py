import requests
import socket  # Import socket module

#SOCKET
s = socket.socket()  
host = ''  
port = 12345 
s.bind((host, port))  
s.listen(1)  
connection, client_address = s.accept()  

#PokeAPI 
ditto_response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
pikachu_response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

#DATEN UMWANDELN
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
        Text = f"Ditto greift an. Pikachu hat noch {pikachu_hp} HP"
        print(Text)
        connection.sendall(Text.encode()) 

        if pikachu_hp <= 0:
            Text = "Ditto gewinnt!"
            print(Text)
            connection.sendall(Text.encode())
            break

        # Pikachu greift Ditto an
        ditto_hp -= pikachu_attack
        if ditto_hp <= 0:
            ditto_hp = 0
        Text = f"Pikachu greift an. Ditto hat noch {ditto_hp} HP"
        print(Text)
        connection.sendall(Text.encode())

        if ditto_hp <= 0:
            Text = "Pikachu gewinnt!"
            print(Text)
            connection.sendall(Text.encode())
            break

connection.close()      
s.close()               
