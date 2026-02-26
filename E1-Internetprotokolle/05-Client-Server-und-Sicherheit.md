# DS 05 – Client-Server-Architektur, Protokolle und Sicherheit

> **Themenfeld E.1 – Internetprotokolle** · Doppelstunde 5 von 5

---

## Lernziele dieser Stunde

- Du kannst die Client-Server-Architektur erklären und von Peer-to-Peer abgrenzen.
- Du verstehst den Ablauf von HTTP, SMTP und POP3 auf Protokollebene.
- Du kannst Sicherheitsaspekte der Netzwerkkommunikation benennen.
- Du kannst eine einfache Client-Server-Anwendung in Python schreiben.

---

## 1. Client-Server-Architektur

### Das Prinzip

Die **Client-Server-Architektur** ist das grundlegende Kommunikationsmodell im Internet:

```
  Client                     Server
  ┌──────┐    Anfrage →     ┌──────┐
  │      │ ───────────────> │      │
  │  💻  │                  │  🖥️  │
  │      │ <─────────────── │      │
  └──────┘    ← Antwort     └──────┘
```

- **Client:** Stellt Anfragen (z. B. dein Browser)
- **Server:** Beantwortet Anfragen (z. B. ein Webserver)
- **Dienst (Service):** Die Leistung, die der Server bereitstellt (z. B. Webseiten ausliefern)
- **Protokoll:** Die „Sprache", die Client und Server sprechen (z. B. HTTP)

### Beispiele

| Dienst | Client | Server | Protokoll |
|--------|--------|--------|-----------|
| Webseiten | Browser (Chrome, Firefox) | Webserver (Apache, Nginx) | HTTP / HTTPS |
| E-Mail senden | Mailprogramm (Thunderbird) | Mailserver | SMTP |
| E-Mail empfangen | Mailprogramm | Mailserver | POP3 / IMAP |
| Dateiübertragung | FTP-Client (FileZilla) | FTP-Server | FTP |
| Namensauflösung | Jeder Rechner | DNS-Server | DNS |

### Client-Server vs. Peer-to-Peer

| Eigenschaft | Client-Server | Peer-to-Peer (P2P) |
|-------------|--------------|-------------------|
| Rollen | Fest: Client fragt, Server antwortet | Alle Teilnehmer gleichberechtigt |
| Beispiel | Webseiten, E-Mail | BitTorrent, manche Chats |
| Vorteil | Zentrale Verwaltung, zuverlässig | Kein einzelner Ausfallpunkt |
| Nachteil | Server als Flaschenhals / Ausfallpunkt | Schwerer zu verwalten |

---

## 2. Protokolle im Detail

### HTTP – Webseiten abrufen

**HTTP** (Hypertext Transfer Protocol) ist das Protokoll für den Abruf von Webseiten.

#### Eine HTTP-Anfrage (Request)

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

- `GET` = Methode (Daten anfordern)
- `/index.html` = Pfad zur gewünschten Ressource
- `Host` = Server-Domainname
- `User-Agent` = Informationen über den Browser

#### Eine HTTP-Antwort (Response)

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<!DOCTYPE html>
<html>
  <head><title>Beispiel</title></head>
  <body><h1>Hallo Welt!</h1></body>
</html>
```

- `200 OK` = Statuscode (alles in Ordnung)
- Danach folgt der eigentliche HTML-Code

#### Wichtige HTTP-Statuscodes

| Code | Bedeutung |
|------|-----------|
| `200 OK` | Alles in Ordnung |
| `301 Moved Permanently` | Seite dauerhaft umgezogen |
| `403 Forbidden` | Zugriff verweigert |
| `404 Not Found` | Seite nicht gefunden |
| `500 Internal Server Error` | Serverfehler |

### SMTP – E-Mails senden

**SMTP** (Simple Mail Transfer Protocol) wird zum **Versenden** von E-Mails verwendet.

```
Client:  HELO client.example.com
Server:  250 Hello client.example.com

Client:  MAIL FROM:<anna@example.com>
Server:  250 OK

Client:  RCPT TO:<bob@example.com>
Server:  250 OK

Client:  DATA
Server:  354 Start mail input

Client:  Subject: Hallo Bob!
Client:  
Client:  Wie geht es dir?
Client:  .
Server:  250 OK

Client:  QUIT
Server:  221 Bye
```

> **Sicherheitsproblem:** Bei SMTP wird der Absender (`MAIL FROM`) nicht überprüft – man kann eine beliebige Absenderadresse angeben! Das ermöglicht **E-Mail-Spoofing**.

### POP3 – E-Mails abrufen

**POP3** (Post Office Protocol Version 3) wird zum **Abrufen** von E-Mails verwendet.

```
Client:  USER bob
Server:  +OK

Client:  PASS geheim123
Server:  +OK 2 messages

Client:  LIST
Server:  +OK
Server:  1 512
Server:  2 1024

Client:  RETR 1
Server:  +OK 512 octets
Server:  [E-Mail-Inhalt]

Client:  QUIT
Server:  +OK Bye
```

> **Sicherheitsproblem:** Das Passwort wird bei einfachem POP3 **im Klartext** übertragen! Jeder, der den Netzwerkverkehr mithört, kann das Passwort lesen.

---

## 3. Sicherheitsaspekte

### Gefahren bei unverschlüsselter Kommunikation

| Gefahr | Beschreibung | Betroffene Protokolle |
|--------|-------------|----------------------|
| **Mitlesen (Sniffing)** | Daten werden auf dem Übertragungsweg abgefangen | HTTP, POP3, SMTP, FTP |
| **Spoofing** | Fälschen der Absenderadresse | SMTP |
| **Man-in-the-Middle** | Angreifer schaltet sich zwischen Client und Server | Alle unverschlüsselten |
| **Replay-Attacke** | Aufgezeichnete Daten werden erneut gesendet | Alle unverschlüsselten |

### Schutzmaßnahmen

| Maßnahme | Beschreibung |
|----------|-------------|
| **HTTPS** (statt HTTP) | Verschlüsselte Webkommunikation (TLS/SSL) |
| **SMTPS / STARTTLS** | Verschlüsseltes E-Mail-Versenden |
| **POP3S / IMAPS** | Verschlüsseltes E-Mail-Abrufen |
| **Zertifikate** | Identitätsprüfung des Servers |
| **Firewall** | Kontrolliert ein-/ausgehenden Netzwerkverkehr |

### HTTPS – Das Schloss im Browser 🔒

```
HTTP:   Daten werden im KLARTEXT übertragen
        → Jeder kann mitlesen!

HTTPS:  Daten werden VERSCHLÜSSELT übertragen (TLS/SSL)
        → Vertraulich und integritätsgeschützt!
```

Am Schloss-Symbol 🔒 in der Adressleiste des Browsers erkennt man, dass eine HTTPS-Verbindung besteht.

---

## 4. Filius: E-Mail-Kommunikation simulieren

> Siehe auch: [Filius-Anleitung: E-Mail](filius-anleitungen/05-email.md)

### Netzwerk aufbauen

```
PC-Anna (192.168.1.1) ──┐
                        Switch ── Mailserver (192.168.1.10)
PC-Bob (192.168.1.2) ──┘            DNS-Server (192.168.1.20)
```

### Schritte

1. Erstelle das Netzwerk und konfiguriere IP-Adressen
2. DNS-Server auf `192.168.1.20`:
   - `mail.schule.de` → `192.168.1.10`
3. Mailserver auf `192.168.1.10`:
   - Installiere **E-Mail-Server** (SMTP + POP3)
   - Richte Postfächer ein: `anna@schule.de` und `bob@schule.de`
4. PC-Anna:
   - Installiere **E-Mail-Programm**
   - Konfiguriere: Absender `anna@schule.de`, SMTP-Server: `mail.schule.de`, POP3-Server: `mail.schule.de`
5. PC-Bob: analog für `bob@schule.de`
6. Sende eine E-Mail von Anna an Bob und rufe sie bei Bob ab

### Beobachte den Datenaustausch!
- Aktiviere den Datenmitschnitt
- Kannst du die SMTP-Befehle und POP3-Befehle erkennen?
- Siehst du, dass das Passwort im Klartext übertragen wird?

---

## 5. Python: Einfache Client-Server-Anwendung

Jetzt nutzen wir Python (in Thonny), um selbst eine Client-Server-Kommunikation zu programmieren!

### Einfacher Echo-Server

Der Server empfängt eine Nachricht vom Client und sendet sie zurück.

**Server** (zuerst starten):

```python
# echo_server.py – in Thonny öffnen und starten
import socket

# Server erstellen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))  # Auf Port 12345 lauschen
server.listen(1)                    # Auf eine Verbindung warten

print("Server gestartet. Warte auf Client...")
verbindung, adresse = server.accept()
print(f"Client verbunden: {adresse}")

# Nachricht empfangen und zurücksenden
nachricht = verbindung.recv(1024).decode("utf-8")
print(f"Empfangen: {nachricht}")

antwort = f"Echo: {nachricht}"
verbindung.send(antwort.encode("utf-8"))
print(f"Gesendet: {antwort}")

verbindung.close()
server.close()
print("Server beendet.")
```

**Client** (nach dem Server starten):

```python
# echo_client.py – in einem zweiten Thonny-Fenster öffnen und starten
import socket

# Verbindung zum Server herstellen
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))
print("Mit Server verbunden!")

# Nachricht senden
nachricht = input("Nachricht eingeben: ")
client.send(nachricht.encode("utf-8"))
print(f"Gesendet: {nachricht}")

# Antwort empfangen
antwort = client.recv(1024).decode("utf-8")
print(f"Antwort vom Server: {antwort}")

client.close()
```

> **So testest du es:**
> 1. Starte `echo_server.py` in Thonny
> 2. Öffne ein zweites Thonny-Fenster und starte `echo_client.py`
> 3. Gib eine Nachricht ein – der Server sendet sie zurück!

### Einfacher Chat-Server (Erweiterung)

```python
# chat_server.py – Mehrere Nachrichten austauschen
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen(1)

print("Chat-Server gestartet. Warte auf Verbindung...")
verbindung, adresse = server.accept()
print(f"Client verbunden: {adresse}")
print("Chat gestartet! (Zum Beenden 'quit' eingeben)")

while True:
    # Nachricht vom Client empfangen
    nachricht = verbindung.recv(1024).decode("utf-8")
    if nachricht.lower() == "quit":
        print("Client hat den Chat beendet.")
        break
    print(f"Client: {nachricht}")
    
    # Antwort eingeben und senden
    antwort = input("Server: ")
    verbindung.send(antwort.encode("utf-8"))
    if antwort.lower() == "quit":
        break

verbindung.close()
server.close()
```

```python
# chat_client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))
print("Verbunden! Chat gestartet. (Zum Beenden 'quit' eingeben)")

while True:
    nachricht = input("Du: ")
    client.send(nachricht.encode("utf-8"))
    if nachricht.lower() == "quit":
        break
    
    antwort = client.recv(1024).decode("utf-8")
    if antwort.lower() == "quit":
        print("Server hat den Chat beendet.")
        break
    print(f"Server: {antwort}")

client.close()
```

Die Python-Dateien findest du auch im Ordner [`python/`](python/).

---

## 🔨 Erarbeitungsaufgabe

Wähle **eine** der folgenden Aufgaben:

### Option A: SMTP und POP3 in Filius untersuchen
1. Baue das E-Mail-Netzwerk in Filius auf (siehe Abschnitt 4)
2. Sende eine E-Mail von Anna an Bob
3. Aktiviere den Datenmitschnitt und analysiere den Verkehr
4. Dokumentiere die SMTP-Befehle, die du beobachtest
5. Rufe die Mail bei Bob ab und dokumentiere die POP3-Befehle
6. Bewerte: Welche Sicherheitsprobleme erkennst du?

### Option B: Python Client-Server
1. Gib den Echo-Server und Echo-Client in Thonny ein
2. Teste die Kommunikation
3. Erweitere den Server so, dass er die empfangene Nachricht in GROSSBUCHSTABEN zurücksendet
4. Erweitere zu einem Chat (mehrere Nachrichten hin und her)

---

## 📝 Übungsaufgaben

### Aufgabe 1: Begriffe erklären
Erkläre in eigenen Worten:
1. Was ist ein Client? Was ist ein Server?
2. Was ist ein Dienst?
3. Was ist ein Protokoll?
4. Was ist der Unterschied zwischen HTTP und HTTPS?

<details>
<summary>Lösung anzeigen</summary>

1. Ein **Client** ist ein Programm/Rechner, der Anfragen an einen Server stellt (z. B. ein Browser). Ein **Server** ist ein Programm/Rechner, der Anfragen von Clients beantwortet und Dienste bereitstellt (z. B. ein Webserver).

2. Ein **Dienst** ist eine Leistung, die ein Server für Clients erbringt, z. B. das Ausliefern von Webseiten oder das Speichern von E-Mails.

3. Ein **Protokoll** ist ein Satz von Regeln, die festlegen, wie Client und Server miteinander kommunizieren. Es definiert das Format der Nachrichten und den Ablauf der Kommunikation.

4. **HTTP** überträgt Daten unverschlüsselt im Klartext – jeder, der den Verkehr mithört, kann die Daten lesen. **HTTPS** verschlüsselt die Daten mit TLS/SSL, sodass nur Client und Server sie lesen können.
</details>

### Aufgabe 2: HTTP-Anfrage analysieren
Gegeben ist folgende HTTP-Anfrage:

```
GET /bilder/logo.png HTTP/1.1
Host: www.schule-musterstadt.de
User-Agent: Mozilla/5.0
Accept: image/png
```

1. Welche HTTP-Methode wird verwendet?
2. Welche Ressource wird angefordert?
3. An welchen Server geht die Anfrage?
4. Was würde der Server antworten, wenn die Datei nicht existiert?

<details>
<summary>Lösung anzeigen</summary>

1. `GET`
2. `/bilder/logo.png`
3. `www.schule-musterstadt.de`
4. `HTTP/1.1 404 Not Found`
</details>

### Aufgabe 3: Sicherheit bewerten
Du schreibst eine E-Mail mit deinen Zugangsdaten für ein Schulprojekt an einen Mitschüler. Beschreibe:
1. Welche Protokolle werden beim Versand und Empfang der E-Mail verwendet?
2. An welchen Stellen könnte ein Angreifer die Zugangsdaten abfangen?
3. Welche Maßnahmen könnten das verhindern?

<details>
<summary>Lösung anzeigen</summary>

1. Versand: SMTP, Empfang: POP3 oder IMAP
2. Mögliche Angriffspunkte:
   - Zwischen deinem PC und dem Mailserver (SMTP-Verbindung)
   - Auf dem Mailserver selbst (E-Mails werden gespeichert)
   - Zwischen dem Mailserver und dem PC des Empfängers (POP3-Verbindung)
   - Im Log-File des Servers
3. Maßnahmen:
   - Verschlüsselte Protokolle verwenden (SMTPS, POP3S)
   - E-Mail-Inhalt selbst verschlüsseln (z. B. PGP)
   - Sensible Daten nicht per E-Mail versenden
   - Passwort nicht per E-Mail, sondern persönlich übermitteln
</details>

### Aufgabe 4: Python-Erweiterung (⭐ Herausforderung)
Erweitere den Python-Echo-Server so, dass er einfache HTTP-Anfragen beantworten kann:

```python
# Tipp: Der Server soll auf eine GET-Anfrage antworten:
# HTTP/1.1 200 OK
# Content-Type: text/html
#
# <html><body><h1>Hallo vom Python-Server!</h1></body></html>
```

Du kannst den Server dann im Browser testen: Öffne `http://127.0.0.1:12345`

<details>
<summary>Lösung anzeigen</summary>

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen(1)
print("Webserver gestartet auf http://127.0.0.1:12345")

while True:
    verbindung, adresse = server.accept()
    anfrage = verbindung.recv(1024).decode("utf-8")
    print(f"Anfrage von {adresse}:")
    print(anfrage[:200])  # Erste 200 Zeichen anzeigen
    
    html = "<html><body><h1>Hallo vom Python-Server!</h1>"
    html += "<p>Diese Seite wird von einem selbst geschriebenen Server ausgeliefert.</p>"
    html += "</body></html>"
    
    antwort = "HTTP/1.1 200 OK\r\n"
    antwort += "Content-Type: text/html; charset=utf-8\r\n"
    antwort += f"Content-Length: {len(html.encode('utf-8'))}\r\n"
    antwort += "\r\n"
    antwort += html
    
    verbindung.send(antwort.encode("utf-8"))
    verbindung.close()
```
</details>

---

## 📋 Zusammenfassung E.1 – Internetprotokolle

| Thema | Kernbegriffe |
|-------|-------------|
| **Rechnernetze** | LAN, WAN, Switch, Router, Topologie |
| **IP-Adressen** | IPv4, Subnetzmaske, Netzwerk-/Hostanteil, Gateway |
| **DNS** | Domainname, DNS-Server, DNS-Auflösung, Hierarchie |
| **TCP/IP-Modell** | 4 Schichten, Protokolle, Datenkapselung, Ports |
| **Client-Server** | Client, Server, Dienst, Protokoll, HTTP, SMTP, POP3 |
| **Sicherheit** | HTTPS, Verschlüsselung, Spoofing, Sniffing, Man-in-the-Middle |

---

## 🔗 Weiterführende Links

- [inf-schule.de – Client-Server](https://www.inf-schule.de/rechnernetze/filius/erkundung_cs)
- [Wikipedia – HTTP](https://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- [Wikipedia – SMTP](https://de.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
- [RFC 2616 – HTTP/1.1 (englisch)](https://www.rfc-editor.org/rfc/rfc2616)

---

[← Zurück: DS 04](04-TCP-IP-Modell.md) · [Weiter → E.2: HTML-Grundgerüst](../E2-HTML-Dokumente/01-HTML-Grundgeruest.md)
