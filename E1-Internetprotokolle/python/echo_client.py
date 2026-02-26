# Echo-Client
# Verbindet sich mit dem Echo-Server und sendet eine Nachricht.
# Zuerst den Server starten, dann dieses Programm!

import socket

# Verbindung zum Server herstellen
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))
print("Mit Server verbunden!")

# Nachricht vom Benutzer eingeben
nachricht = input("Nachricht eingeben: ")

# Nachricht an den Server senden
client.send(nachricht.encode("utf-8"))
print(f"Gesendet: {nachricht}")

# Antwort vom Server empfangen
antwort = client.recv(1024).decode("utf-8")
print(f"Antwort vom Server: {antwort}")

# Verbindung schließen
client.close()
