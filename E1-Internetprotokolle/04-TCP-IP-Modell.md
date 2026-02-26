# DS 04 – Das TCP/IP-Referenzmodell

> **Themenfeld E.1 – Internetprotokolle** · Doppelstunde 4 von 5

---

## Lernziele dieser Stunde

- Du kannst die vier Schichten des TCP/IP-Referenzmodells benennen und erklären.
- Du verstehst, welche Protokolle auf welcher Schicht arbeiten.
- Du kannst das Prinzip der Datenkapselung beschreiben.
- Du kannst den Datenfluss beim Aufruf einer Webseite erklären.

---

## 1. Wozu ein Schichtenmodell?

Die Kommunikation im Internet ist komplex. Um diese Komplexität beherrschbar zu machen, wird sie in **Schichten** aufgeteilt. Jede Schicht hat eine klar definierte Aufgabe und baut auf der darunterliegenden Schicht auf.

**Analogie – Briefversand:**

| Schicht | Briefversand | Internet |
|---------|-------------|----------|
| 4 | Brief schreiben | Daten der Anwendung (z. B. Webseite) |
| 3 | Brief in Umschlag, Adresse drauf | Empfänger-Port und Absender-Port |
| 2 | Umschlag mit Briefmarke zur Post | IP-Adresse des Empfängers |
| 1 | Post transportiert den Brief | Kabel, WLAN, Lichtsignale |

---

## 2. Die vier Schichten des TCP/IP-Modells

```
┌─────────────────────────────────────┐
│  4. Anwendungsschicht               │  HTTP, HTTPS, SMTP, POP3, FTP, DNS
│     (Application Layer)             │
├─────────────────────────────────────┤
│  3. Transportschicht                │  TCP, UDP
│     (Transport Layer)               │
├─────────────────────────────────────┤
│  2. Internetschicht                 │  IP, ICMP
│     (Internet Layer)                │
├─────────────────────────────────────┤
│  1. Netzzugangsschicht              │  Ethernet, WLAN, DSL
│     (Network Access Layer)          │
└─────────────────────────────────────┘
```

### Schicht 1 – Netzzugangsschicht (Network Access)

- **Aufgabe:** Physische Übertragung von Daten über das Kabel, WLAN oder andere Medien
- **Protokolle:** Ethernet, WLAN (IEEE 802.11)
- **Adressierung:** MAC-Adresse (Hardware-Adresse der Netzwerkkarte)
- **Geräte:** Switch, Netzwerkkabel, Access Point

> Eine **MAC-Adresse** ist eine weltweit eindeutige Hardware-Adresse jeder Netzwerkkarte, z. B. `AA:BB:CC:DD:EE:FF`

### Schicht 2 – Internetschicht (Internet)

- **Aufgabe:** Weiterleitung von Datenpaketen über Netzwerkgrenzen hinweg (Routing)
- **Protokolle:** IP (Internet Protocol), ICMP (für Ping)
- **Adressierung:** IP-Adresse
- **Geräte:** Router

### Schicht 3 – Transportschicht (Transport)

- **Aufgabe:** Zuverlässige Übertragung der Daten zwischen zwei Programmen
- **Protokolle:**
  - **TCP** (Transmission Control Protocol): Zuverlässig, verbindungsorientiert. Stellt sicher, dass alle Pakete ankommen und in der richtigen Reihenfolge sind.
  - **UDP** (User Datagram Protocol): Schnell, aber unzuverlässig. Keine Garantie, dass Pakete ankommen.
- **Adressierung:** Portnummer (identifiziert den Dienst/das Programm auf einem Rechner)

| Protokoll | Eigenschaften | Einsatz |
|-----------|-------------|---------|
| **TCP** | Zuverlässig, langsamer | Webseiten, E-Mail, Dateiübertragung |
| **UDP** | Schnell, keine Garantie | Video-Streaming, Online-Spiele, DNS |

### Schicht 4 – Anwendungsschicht (Application)

- **Aufgabe:** Bereitstellung von Diensten für den Benutzer
- **Protokolle:**

| Protokoll | Port | Dienst |
|-----------|------|--------|
| **HTTP** | 80 | Webseiten (unverschlüsselt) |
| **HTTPS** | 443 | Webseiten (verschlüsselt) |
| **SMTP** | 25 | E-Mail versenden |
| **POP3** | 110 | E-Mail abrufen |
| **IMAP** | 143 | E-Mail abrufen (fortgeschritten) |
| **FTP** | 21 | Dateiübertragung |
| **DNS** | 53 | Namensauflösung |

---

## 3. Datenkapselung (Encapsulation)

Wenn Daten durch die Schichten wandern, wird auf jeder Schicht ein **Header** (Kopfinformation) hinzugefügt. Diesen Vorgang nennt man **Kapselung**.

### Senden: Von oben nach unten

```
Schicht 4: Anwendung    │ HTTP-Daten                    │
                         ├──────────────────────────────┤
Schicht 3: Transport     │ TCP-Header │ HTTP-Daten      │  ← Segment
                         ├────────────┼─────────────────┤
Schicht 2: Internet      │ IP-Header  │ TCP │ HTTP      │  ← Paket
                         ├────────────┼─────┼───────────┤
Schicht 1: Netzzugang    │ ETH-Header │ IP  │ TCP │HTTP │  ← Frame
                         └────────────┴─────┴─────┴─────┘
```

### Empfangen: Von unten nach oben

Beim Empfänger wird auf jeder Schicht der entsprechende Header entfernt (→ **Entkapselung**), bis die reinen Anwendungsdaten übrig bleiben.

### Analogie: Russische Matroschka-Puppe 🪆

Jede Schicht „verpackt" die Daten der darüberliegenden Schicht, wie bei ineinander verschachtelten Puppen.

---

## 4. Beispiel: Aufruf einer Webseite

Was passiert, wenn du `http://www.example.com` im Browser eingibst?

```
1. DNS-Auflösung (Schicht 4)
   Browser → DNS-Server: "Welche IP hat www.example.com?"
   DNS-Server → Browser: "93.184.216.34"

2. TCP-Verbindungsaufbau (Schicht 3)
   PC ←→ Server: "Drei-Wege-Handshake" (SYN → SYN-ACK → ACK)
   → Verbindung steht

3. HTTP-Anfrage (Schicht 4)
   Browser → Server: "GET / HTTP/1.1  Host: www.example.com"

4. Verarbeitung auf allen Schichten (Schicht 4 → 1)
   - HTTP-Anfrage wird in TCP-Segmente verpackt
   - TCP-Segmente werden in IP-Pakete verpackt
   - IP-Pakete werden in Ethernet-Frames verpackt
   - Frames werden über das Kabel gesendet

5. Server antwortet (Schicht 1 → 4)
   - Server empfängt Frames, entpackt bis zur HTTP-Anfrage
   - Server sendet HTTP-Antwort mit der Webseite zurück

6. Browser zeigt die Webseite an
```

### Der TCP-Dreiwege-Handshake

Vor jeder TCP-Verbindung wird eine Verbindung aufgebaut:

```
Client                    Server
  │                         │
  │ ── SYN ──────────────> │   "Ich möchte eine Verbindung"
  │                         │
  │ <────────── SYN-ACK ── │   "OK, ich bin bereit"
  │                         │
  │ ── ACK ──────────────> │   "Bestätigt, los geht's!"
  │                         │
  │ ═══ Verbindung steht ══│
```

---

## 🔨 Erarbeitungsaufgabe: Datenaustausch in Filius beobachten

> Siehe auch: [Filius-Anleitung: Datenaustausch beobachten](filius-anleitungen/04-datenaustausch.md)

### Vorbereitung
Verwende das Netzwerk aus DS 03 (mit DNS-Server und Webserver) oder baue es neu:

```
PC-Client (192.168.1.1) ──┐
                          Switch ── DNS-Server (192.168.1.10)
Webserver (192.168.1.20) ─┘
```

### Aufgabe

1. **Wechsle in den Aktionsmodus**

2. **Aktiviere den Datenaustausch-Mitschnitt:**
   - Rechtsklicke auf das Kabel zwischen Client und Switch
   - Wähle „Datenaustausch anzeigen" (oder ähnlich)

3. **Rufe eine Webseite auf:**
   - Öffne den Webbrowser am Client
   - Rufe `www.meineschule.de` auf

4. **Analysiere den Mitschnitt:**
   - Welche Protokolle siehst du? (DNS, TCP, HTTP?)
   - Kannst du den TCP-Dreiwege-Handshake erkennen?
   - Welche IP-Adressen und Ports werden verwendet?

5. **Dokumentiere** deine Beobachtungen:
   - Erstelle eine Tabelle mit den beobachteten Paketen
   - Ordne jedes Paket einer Schicht des TCP/IP-Modells zu

---

## 📝 Übungsaufgaben

### Aufgabe 1: Schichten zuordnen
Ordne die Begriffe der richtigen Schicht zu:

| Begriff | Schicht |
|---------|---------|
| HTTP | ? |
| IP-Adresse | ? |
| Ethernet | ? |
| TCP | ? |
| MAC-Adresse | ? |
| Portnummer | ? |
| Router | ? |
| Switch | ? |

<details>
<summary>Lösung anzeigen</summary>

| Begriff | Schicht |
|---------|---------|
| HTTP | 4 – Anwendungsschicht |
| IP-Adresse | 2 – Internetschicht |
| Ethernet | 1 – Netzzugangsschicht |
| TCP | 3 – Transportschicht |
| MAC-Adresse | 1 – Netzzugangsschicht |
| Portnummer | 3 – Transportschicht |
| Router | 2 – Internetschicht |
| Switch | 1 – Netzzugangsschicht |
</details>

### Aufgabe 2: TCP vs. UDP
Erkläre, warum für die folgenden Anwendungen jeweils TCP oder UDP sinnvoller ist:

1. Eine E-Mail versenden
2. Ein Live-Videostream
3. Eine Datei herunterladen
4. Ein Online-Spiel (z. B. Fortnite)
5. Einen Domainnamen auflösen

<details>
<summary>Lösung anzeigen</summary>

1. **E-Mail → TCP** – Der komplette Text muss fehlerfrei ankommen
2. **Live-Video → UDP** – Geschwindigkeit ist wichtiger als Fehlerfreiheit. Ein verlorenes Bild fällt kaum auf.
3. **Datei herunterladen → TCP** – Alle Bytes müssen korrekt und vollständig ankommen
4. **Online-Spiel → UDP** – Geringe Latenz ist entscheidend. Veraltete Positionsdaten sind nutzlos.
5. **DNS → UDP** – Kurze, schnelle Anfrage/Antwort. Bei Verlust wird einfach neu gefragt.
</details>

### Aufgabe 3: Datenkapselung zeichnen
Zeichne den Kapsulungsprozess für folgendes Szenario:
- Ein Browser sendet eine HTTP-GET-Anfrage an einen Webserver
- Beschrifte für jede Schicht, welcher Header hinzugefügt wird
- Notiere relevante Informationen in jedem Header (z. B. Quell-IP, Ziel-IP, Quell-Port, Ziel-Port)

### Aufgabe 4: Portnummern
Ein Server hat die IP-Adresse `10.0.0.5`. Auf ihm laufen:
- Ein Webserver (Port 80)
- Ein E-Mail-Server für SMTP (Port 25) und POP3 (Port 110)

Gib für folgende Aktionen die vollständige Adresse an (IP:Port):
1. Eine Webseite abrufen
2. Eine E-Mail senden
3. E-Mails abholen

<details>
<summary>Lösung anzeigen</summary>

1. Webseite abrufen: `10.0.0.5:80`
2. E-Mail senden: `10.0.0.5:25`
3. E-Mails abholen: `10.0.0.5:110`
</details>

---

## 🔗 Weiterführende Links

- [inf-schule.de – Schichtenmodell](https://www.inf-schule.de/rechnernetze/protokolle)
- [Wikipedia – Internetprotokollfamilie](https://de.wikipedia.org/wiki/Internetprotokollfamilie)
- [Video: TCP/IP einfach erklärt](https://www.youtube.com/results?search_query=TCP+IP+Modell+einfach+erkl%C3%A4rt)

---

[← Zurück: DS 03](03-DNS.md) · [Weiter → DS 05: Client-Server und Sicherheit](05-Client-Server-und-Sicherheit.md)
