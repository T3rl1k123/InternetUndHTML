# Einfacher Webserver in Python
# Liefert eine HTML-Seite an den Browser aus.
# Starte dieses Programm und öffne http://127.0.0.1:12345 im Browser.

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen(5)

print("=== Python-Webserver ===")
print("Gestartet auf http://127.0.0.1:12345")
print("Öffne diese Adresse im Browser!")
print("Zum Beenden: Strg+C\n")

try:
    while True:
        # Auf eingehende Verbindung warten
        verbindung, adresse = server.accept()
        
        # HTTP-Anfrage empfangen
        anfrage = verbindung.recv(1024).decode("utf-8")
        
        # Erste Zeile der Anfrage anzeigen
        erste_zeile = anfrage.split("\n")[0] if anfrage else "(leer)"
        print(f"Anfrage von {adresse}: {erste_zeile}")
        
        # HTML-Seite erstellen
        html = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Python Webserver</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; }
        h1 { color: #2c3e50; }
        p { color: #555; }
        .info { background: #ecf0f1; padding: 15px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Hallo vom Python-Webserver!</h1>
    <p>Diese Seite wird von einem selbst geschriebenen Server ausgeliefert.</p>
    <div class="info">
        <p><strong>So funktioniert es:</strong></p>
        <ol>
            <li>Dein Browser sendet eine HTTP-GET-Anfrage</li>
            <li>Der Python-Server empfängt die Anfrage</li>
            <li>Der Server erstellt eine HTTP-Antwort mit HTML</li>
            <li>Der Browser zeigt das HTML an</li>
        </ol>
    </div>
</body>
</html>"""
        
        # HTTP-Antwort zusammenbauen
        antwort = "HTTP/1.1 200 OK\r\n"
        antwort += "Content-Type: text/html; charset=utf-8\r\n"
        antwort += f"Content-Length: {len(html.encode('utf-8'))}\r\n"
        antwort += "Connection: close\r\n"
        antwort += "\r\n"
        antwort += html
        
        # Antwort senden
        verbindung.send(antwort.encode("utf-8"))
        verbindung.close()

except KeyboardInterrupt:
    print("\nServer beendet.")
    server.close()
