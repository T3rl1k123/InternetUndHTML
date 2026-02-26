# Echo-Server
# Empfängt eine Nachricht vom Client und sendet sie zurück.
# Zuerst dieses Programm starten, dann den Client.

import socket

# Server-Socket erstellen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server an Adresse und Port binden
# 127.0.0.1 = localhost (der eigene Rechner)
# 12345 = Portnummer (frei wählbar über 1024)
server.bind(("127.0.0.1", 12345))

# Auf eingehende Verbindungen warten (max. 1 gleichzeitig)
server.listen(1)
print("Echo-Server gestartet auf 127.0.0.1:12345")
print("Warte auf Client-Verbindung...")

# Verbindung annehmen
verbindung, adresse = server.accept()
print(f"Client verbunden von: {adresse}")

# Nachricht empfangen (max. 1024 Bytes)
nachricht = verbindung.recv(1024).decode("utf-8")
print(f"Empfangen: {nachricht}")

# Echo-Antwort zurücksenden
antwort = f"Echo: {nachricht}"
verbindung.send(antwort.encode("utf-8"))
print(f"Gesendet: {antwort}")

# Verbindung und Server schließen
verbindung.close()
server.close()
print("Server beendet.")
