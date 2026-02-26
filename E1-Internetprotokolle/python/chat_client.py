# Chat-Client
# Verbindet sich mit dem Chat-Server für einen Text-Chat.
# Zuerst den Chat-Server starten, dann dieses Programm!

import socket

# Verbindung zum Server herstellen
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

print("=== Chat-Client ===")
print("Verbunden mit Server!")
print("Zum Beenden 'quit' eingeben.\n")

while True:
    # Eigene Nachricht eingeben und senden
    nachricht = input("Du:     ")
    client.send(nachricht.encode("utf-8"))
    
    if nachricht.lower() == "quit":
        print("Chat beendet.")
        break
    
    # Antwort vom Server empfangen
    antwort = client.recv(1024).decode("utf-8")
    
    if antwort.lower() == "quit":
        print("Server hat den Chat beendet.")
        break
    
    print(f"Server: {antwort}")

client.close()
