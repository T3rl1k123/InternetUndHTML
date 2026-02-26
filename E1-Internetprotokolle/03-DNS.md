# DS 03 – Das Domain Name System (DNS)

> **Themenfeld E.1 – Internetprotokolle** · Doppelstunde 3 von 5

---

## Lernziele dieser Stunde

- Du kannst erklären, wozu DNS benötigt wird.
- Du verstehst, wie eine DNS-Auflösung funktioniert.
- Du kennst den hierarchischen Aufbau des DNS.
- Du kannst einen DNS-Server in Filius einrichten und testen.

---

## 1. Warum brauchen wir DNS?

Menschen merken sich Namen leichter als Zahlen. Stell dir vor, du müsstest dir für jede Webseite eine IP-Adresse merken:

| Was du eingibst | Was der Computer braucht |
|----------------|------------------------|
| `www.google.de` | `142.250.185.99` |
| `www.wikipedia.org` | `91.198.174.192` |
| `www.instagram.com` | `157.240.1.174` |

Das **Domain Name System (DNS)** ist das „Telefonbuch des Internets". Es übersetzt **Domainnamen** (z. B. `www.google.de`) in **IP-Adressen** (z. B. `142.250.185.99`).

---

## 2. Wie funktioniert eine DNS-Auflösung?

Wenn du `www.example.com` in deinen Browser eingibst, passiert Folgendes:

```
1. Dein PC fragt seinen DNS-Server:
   "Welche IP hat www.example.com?"

2. Der DNS-Server sucht in seiner Datenbank
   → Gefunden? → Antwort zurück an den PC
   → Nicht gefunden? → Fragt einen übergeordneten DNS-Server

3. Der PC erhält die IP-Adresse: 93.184.216.34

4. Der PC verbindet sich mit dem Webserver unter 93.184.216.34
```

### Ablauf als Diagramm

```
  Benutzer          PC              DNS-Server        Webserver
     |               |                  |                 |
     |-- www.example.com -->|           |                 |
     |               |--- DNS-Anfrage ->|                 |
     |               |<-- 93.184.216.34-|                 |
     |               |--- HTTP-Anfrage ------------------>|
     |               |<-- Webseite ------------------------|
     |<-- Webseite --|                  |                 |
```

### DNS-Cache

Um nicht jedes Mal nachfragen zu müssen, speichert dein PC aufgelöste Namen für eine gewisse Zeit im **DNS-Cache**. Das beschleunigt wiederholte Aufrufe.

> **Probiere es aus:** Öffne die Kommandozeile deines Rechners und gib ein:
> - Windows: `nslookup www.google.de`
> - macOS/Linux: `dig www.google.de` oder `nslookup www.google.de`

---

## 3. Hierarchischer Aufbau des DNS

Das DNS ist **hierarchisch** aufgebaut, wie ein Baum:

```
                    . (Root)
                   / | \
                 /   |   \
              .de  .com  .org    ← Top-Level-Domains (TLD)
              / \     |
           /     \    |
     google  example  wikipedia  ← Second-Level-Domains
        |       |
       www     www               ← Subdomains / Hostnamen
```

### Domainnamen lesen (von rechts nach links!)

```
www . example . com .
 │      │       │   │
 │      │       │   └── Root-Domain (wird meist weggelassen)
 │      │       └────── Top-Level-Domain (TLD)
 │      └────────────── Second-Level-Domain
 └───────────────────── Subdomain / Hostname
```

### Arten von Top-Level-Domains

| TLD | Typ | Beispiele |
|-----|-----|-----------|
| `.de`, `.at`, `.ch` | Länderbezogen (ccTLD) | Websites aus Deutschland, Österreich, Schweiz |
| `.com` | Generisch (gTLD) | Kommerzielle Websites |
| `.org` | Generisch (gTLD) | Organisationen |
| `.edu` | Gesponsert (sTLD) | Bildungseinrichtungen (USA) |
| `.io`, `.dev` | Neuere gTLDs | Technische Websites |

---

## 4. DNS-Server in Filius

In Filius kannst du einen eigenen DNS-Server einrichten und die Namensauflösung simulieren.

### Aufbau

```
Netzwerk: 192.168.1.0/24

  PC-Client (192.168.1.1) ──┐
                            Switch ── DNS-Server (192.168.1.10)
  Webserver (192.168.1.20) ─┘
```

---

## 🔨 Erarbeitungsaufgabe: DNS-Server in Filius einrichten

> Siehe auch: [Filius-Anleitung: DNS](filius-anleitungen/03-dns.md)

### Schritt-für-Schritt

1. **Erstelle das Netzwerk** im Entwurfsmodus:
   - 1 Switch
   - 1 PC-Client: IP `192.168.1.1`, Maske `255.255.255.0`
   - 1 DNS-Server: IP `192.168.1.10`, Maske `255.255.255.0`
   - 1 Webserver: IP `192.168.1.20`, Maske `255.255.255.0`

2. **DNS-Server beim Client eintragen:**
   - Doppelklicke auf den PC-Client
   - Trage als DNS-Server `192.168.1.10` ein

3. **Wechsle in den Aktionsmodus**

4. **DNS-Server konfigurieren:**
   - Doppelklicke auf den DNS-Server (192.168.1.10)
   - Installiere die Software **DNS-Server**
   - Starte den DNS-Server
   - Füge einen Eintrag hinzu:
     - Domainname: `www.meineschule.de`
     - IP-Adresse: `192.168.1.20`

5. **Webserver einrichten:**
   - Doppelklicke auf den Webserver (192.168.1.20)
   - Installiere die Software **Webserver**
   - Starte den Webserver

6. **Testen:**
   - Doppelklicke auf den PC-Client
   - Installiere den **Webbrowser**
   - Öffne den Webbrowser
   - Gib in die Adresszeile ein: `www.meineschule.de`
   - Die Startseite des Webservers sollte angezeigt werden! ✅

### Was passiert im Hintergrund?

1. Der Browser fragt den DNS-Server: „Welche IP hat `www.meineschule.de`?"
2. Der DNS-Server antwortet: `192.168.1.20`
3. Der Browser verbindet sich mit `192.168.1.20` und ruft die Webseite ab

---

## 📝 Übungsaufgaben

### Aufgabe 1: DNS-Begriffe
Erkläre in eigenen Worten:
1. Was ist ein DNS-Server?
2. Was bedeutet „DNS-Auflösung"?
3. Was ist ein DNS-Cache und wozu dient er?

<details>
<summary>Lösung anzeigen</summary>

1. Ein DNS-Server ist ein Server, der Domainnamen (wie www.google.de) in IP-Adressen (wie 142.250.185.99) übersetzen kann. Er ist das „Telefonbuch" des Internets.

2. DNS-Auflösung ist der Vorgang, bei dem ein Domainname in die zugehörige IP-Adresse umgewandelt wird.

3. Der DNS-Cache ist ein Zwischenspeicher auf dem eigenen Rechner, der kürzlich aufgelöste Domainnamen und ihre IP-Adressen speichert. Er beschleunigt wiederholte Zugriffe, weil der DNS-Server nicht erneut gefragt werden muss.
</details>

### Aufgabe 2: Domains zerlegen
Zerlege die folgenden Domains in ihre Bestandteile (Hostname, Second-Level-Domain, TLD):

1. `www.hessisches-kultusministerium.de`
2. `mail.google.com`
3. `de.wikipedia.org`
4. `shop.amazon.de`

<details>
<summary>Lösung anzeigen</summary>

| Domain | Hostname/Subdomain | Second-Level-Domain | TLD |
|--------|-------------------|-------------------|-----|
| `www.hessisches-kultusministerium.de` | www | hessisches-kultusministerium | .de |
| `mail.google.com` | mail | google | .com |
| `de.wikipedia.org` | de | wikipedia | .org |
| `shop.amazon.de` | shop | amazon | .de |
</details>

### Aufgabe 3: Mehrere Domains in Filius
Erweitere dein Filius-Netzwerk:
1. Füge einen zweiten Webserver hinzu (IP: `192.168.1.30`)
2. Registriere zwei Domains im DNS-Server:
   - `www.schule.de` → `192.168.1.20`
   - `www.bibliothek.de` → `192.168.1.30`
3. Teste, ob der Browser beide Adressen auflösen kann

### Aufgabe 4: DNS über Netzwerkgrenzen (⭐ Herausforderung)
Kombiniere die Aufgaben aus DS 02 und DS 03:
1. Baue zwei Netzwerke mit einem Router (wie in DS 02)
2. Platziere den DNS-Server in Netzwerk A
3. Platziere einen Webserver in Netzwerk B
4. Konfiguriere alles, sodass ein Client in Netzwerk A über den Domainnamen auf den Webserver in Netzwerk B zugreifen kann

> **Tipp:** Vergiss nicht, den Gateway und den DNS-Server bei allen Clients einzutragen!

### Aufgabe 5: Python – DNS-Abfrage
Schreibe ein kleines Python-Programm, das zu einem Domainnamen die IP-Adresse ermittelt:

```python
import socket

domain = input("Domain eingeben: ")
# Tipp: socket.gethostbyname() löst einen Domainnamen auf
```

<details>
<summary>Lösung anzeigen</summary>

```python
import socket

domain = input("Domain eingeben (z.B. www.google.de): ")
try:
    ip = socket.gethostbyname(domain)
    print(f"Die IP-Adresse von {domain} ist: {ip}")
except socket.gaierror:
    print(f"Fehler: {domain} konnte nicht aufgelöst werden.")
```
</details>

---

## 🔗 Weiterführende Links

- [inf-schule.de – DNS](https://www.inf-schule.de/rechnernetze/filius/erkundung_dns)
- [Wikipedia – Domain Name System](https://de.wikipedia.org/wiki/Domain_Name_System)
- [How DNS works (Comic, englisch)](https://howdns.works/)

---

[← Zurück: DS 02](02-IP-Adressen-und-Routing.md) · [Weiter → DS 04: TCP/IP-Modell](04-TCP-IP-Modell.md)
