# Chat-Server
# Erlaubt einen einfachen Text-Chat zwischen Server und Client.
# Zuerst dieses Programm starten, dann den Chat-Client!

import socket

# Server erstellen und starten
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen(1)

print("=== Chat-Server ===")
print("Gestartet auf 127.0.0.1:12345")
print("Warte auf Verbindung...")

verbindung, adresse = server.accept()
print(f"Client verbunden: {adresse}")
print("Chat gestartet! Zum Beenden 'quit' eingeben.\n")

while True:
    # Nachricht vom Client empfangen
    nachricht = verbindung.recv(1024).decode("utf-8")
    
    # Prüfen, ob der Client beenden möchte
    if nachricht.lower() == "quit":
        print("Client hat den Chat beendet.")
        break
    
    print(f"Client: {nachricht}")
    
    # Eigene Antwort eingeben und senden
    antwort = input("Du:     ")
    verbindung.send(antwort.encode("utf-8"))
    
    if antwort.lower() == "quit":
        print("Chat beendet.")
        break

verbindung.close()
server.close()
