# DS 01 – Rechnernetze: Aufbau und Komponenten

> **Themenfeld E.1 – Internetprotokolle** · Doppelstunde 1 von 5

---

## Lernziele dieser Stunde

- Du kannst erklären, was ein Rechnernetz ist und wozu es dient.
- Du kennst die wichtigsten Netzwerkkomponenten und ihre Funktion.
- Du kannst verschiedene Netzwerktopologien unterscheiden.
- Du kannst ein einfaches Netzwerk in Filius aufbauen und testen.

---

## 1. Was ist ein Rechnernetz?

Ein **Rechnernetz** (engl. *computer network*) ist ein Zusammenschluss von zwei oder mehr Computern, die miteinander kommunizieren können. Rechnernetze ermöglichen:

- **Datenaustausch** – Dateien, Nachrichten, E-Mails versenden und empfangen
- **Ressourcenteilung** – gemeinsame Nutzung von Druckern, Speicher, Internet
- **Kommunikation** – Chats, Videokonferenzen, soziale Netzwerke
- **Zugriff auf Dienste** – Webseiten, Datenbanken, Cloud-Speicher

### Netzwerke nach Reichweite

| Abkürzung | Name | Reichweite | Beispiel |
|-----------|------|-----------|----------|
| **PAN** | Personal Area Network | wenige Meter | Bluetooth-Verbindung zum Kopfhörer |
| **LAN** | Local Area Network | ein Gebäude / Campus | Schulnetzwerk |
| **WLAN** | Wireless LAN | wie LAN, aber kabellos | WLAN im Klassenraum |
| **MAN** | Metropolitan Area Network | eine Stadt | Stadtnetz einer Universität |
| **WAN** | Wide Area Network | weltweit | Das Internet |

> **Das Internet** ist das größte WAN der Welt – ein Netzwerk aus Netzwerken.

---

## 2. Netzwerkkomponenten

### Endgeräte
- **Computer / Laptop / Smartphone** – Geräte, die Daten senden und empfangen
- **Server** – Computer, die Dienste für andere bereitstellen (z. B. Webserver)

### Netzwerkgeräte

| Gerät | Funktion |
|-------|----------|
| **Netzwerkkabel** | Physische Verbindung zwischen Geräten |
| **Switch** | Verbindet mehrere Geräte in einem lokalen Netzwerk (LAN). Leitet Daten gezielt an das richtige Gerät weiter. |
| **Router** | Verbindet verschiedene Netzwerke miteinander. Leitet Datenpakete zwischen Netzen weiter (Routing). |
| **Access Point** | Ermöglicht WLAN-Zugang zu einem kabelgebundenen Netzwerk |

### Merke: Switch vs. Router

```
Switch  → verbindet Geräte INNERHALB eines Netzwerks
Router  → verbindet verschiedene NETZWERKE miteinander
```

**Analogie:** Ein Switch ist wie ein Briefverteiler innerhalb eines Bürogebäudes. Ein Router ist wie die Post, die Briefe zwischen verschiedenen Städten transportiert.

---

## 3. Netzwerktopologien

Die **Topologie** beschreibt, wie die Geräte in einem Netzwerk miteinander verbunden sind.

### Stern-Topologie (heute am häufigsten)
```
       PC1
        |
PC4 -- Switch -- PC2
        |
       PC3
```
- Alle Geräte sind mit einem zentralen Switch verbunden
- **Vorteil:** Fällt ein Kabel aus, sind nur ein Gerät betroffen
- **Nachteil:** Fällt der Switch aus, ist das gesamte Netz gestört

### Bus-Topologie (veraltet)
```
PC1 --- PC2 --- PC3 --- PC4
         |
    gemeinsames Kabel
```
- Alle Geräte teilen sich ein Kabel
- **Vorteil:** Wenig Kabel nötig
- **Nachteil:** Kollisionen, ein Kabelbruch stört alles

### Ring-Topologie
```
PC1 --- PC2
 |       |
PC4 --- PC3
```
- Daten werden im Kreis weitergegeben
- **Vorteil:** Jedes Gerät hat gleiche Zugangschancen
- **Nachteil:** Ein Ausfall unterbricht den Ring

---

## 4. Filius – Erste Schritte

[Filius](https://www.lernsoftware-filius.de/) ist eine Simulationssoftware für Rechnernetze. Damit könnt ihr Netzwerke aufbauen, konfigurieren und Kommunikation simulieren.

### Installation
1. Lade Filius herunter: [https://www.lernsoftware-filius.de/Herunterladen](https://www.lernsoftware-filius.de/Herunterladen)
2. Installiere und starte das Programm
3. Du siehst zwei Modi:
   - 🔧 **Entwurfsmodus** – Netzwerk aufbauen und konfigurieren
   - ▶️ **Aktionsmodus** – Netzwerk testen und Kommunikation simulieren

### Die Filius-Oberfläche

Im **Entwurfsmodus** findest du links die Werkzeugleiste mit:
- **Rechner** (PC/Laptop)
- **Switch** (Verteiler)
- **Router** (Netzwerkverbinder)
- **Kabel** (Verbindung)

---

## 🔨 Erarbeitungsaufgabe: Dein erstes Netzwerk in Filius

### Schritt-für-Schritt-Anleitung

> Siehe auch: [Filius-Anleitung: Erstes Netzwerk](filius-anleitungen/01-erstes-netzwerk.md)

**Ziel:** Baue ein einfaches Netzwerk mit 3 PCs und einem Switch auf.

1. **Öffne Filius** und wechsle in den **Entwurfsmodus** (Schraubenschlüssel-Symbol)

2. **Platziere einen Switch** in der Mitte der Arbeitsfläche
   - Klicke auf das Switch-Symbol in der Werkzeugleiste
   - Klicke auf die Arbeitsfläche, um den Switch zu platzieren

3. **Platziere 3 Rechner** (PCs) um den Switch herum

4. **Verbinde die PCs mit dem Switch**
   - Klicke auf das Kabel-Symbol
   - Klicke auf PC1, dann auf den Switch
   - Wiederhole für PC2 und PC3

5. **Konfiguriere die IP-Adressen** (Doppelklick auf jeden PC):
   - PC1: IP-Adresse `192.168.1.1`
   - PC2: IP-Adresse `192.168.1.2`
   - PC3: IP-Adresse `192.168.1.3`

   > **Hinweis:** Filius fragt auch nach einer „Subnetzmaske". Trage dort überall `255.255.255.0` ein. Was die Subnetzmaske genau bedeutet, lernst du in [DS 02](02-IP-Adressen-und-Routing.md).

6. **Wechsle in den Aktionsmodus** (grüner Pfeil)

7. **Teste die Verbindung:**
   - Doppelklicke auf PC1
   - Starte die **Befehlszeile** (Terminal)
   - Gib ein: `ping 192.168.1.2`
   - Wenn du Antworten bekommst, funktioniert die Verbindung! ✅

### Ergebnis
```
       PC1 (192.168.1.1)
           |
PC3 -- Switch -- PC2 (192.168.1.2)
(192.168.1.3)
```

---

## 📝 Übungsaufgaben

### Aufgabe 1: Begriffe zuordnen
Ordne die Begriffe der richtigen Beschreibung zu:

| Begriff | Beschreibung |
|---------|-------------|
| LAN | a) Verbindet verschiedene Netzwerke |
| Router | b) Lokales Netzwerk in einem Gebäude |
| Switch | c) Verbindet Geräte innerhalb eines Netzwerks |
| WAN | d) Netzwerk über große Entfernungen |

<details>
<summary>Lösung anzeigen</summary>

- LAN → b) Lokales Netzwerk in einem Gebäude
- Router → a) Verbindet verschiedene Netzwerke
- Switch → c) Verbindet Geräte innerhalb eines Netzwerks
- WAN → d) Netzwerk über große Entfernungen
</details>

### Aufgabe 2: Netzwerk erweitern
Erweitere dein Filius-Netzwerk:
1. Füge 2 weitere PCs hinzu (PC4 und PC5)
2. Vergib passende IP-Adressen (im gleichen Netzwerk `192.168.1.x`)
3. Teste mit `ping`, ob alle PCs sich gegenseitig erreichen können

### Aufgabe 3: Nachdenken
1. Was passiert, wenn du einem PC die IP-Adresse `192.168.2.1` gibst (statt `192.168.1.x`)?  
   Probiere es in Filius aus und erkläre das Ergebnis.
2. Was passiert, wenn du zwei PCs die gleiche IP-Adresse gibst? Probiere es aus.

<details>
<summary>Lösung anzeigen</summary>

1. Der PC mit `192.168.2.1` kann die anderen PCs NICHT erreichen, weil er sich in einem anderen Netzwerk befindet. Die ersten drei Zahlen der IP-Adresse müssen übereinstimmen, damit die PCs sich im selben Netzwerk befinden. Warum genau das so ist, lernst du in DS 02 (Subnetzmaske).

2. Bei doppelten IP-Adressen kommt es zu Konflikten – die Kommunikation funktioniert nicht zuverlässig, weil das Netzwerk nicht weiß, welcher PC gemeint ist. IP-Adressen müssen innerhalb eines Netzwerks eindeutig sein.
</details>

### Aufgabe 4: Topologien zeichnen
Zeichne (auf Papier oder digital) die folgenden Netzwerke:
1. Ein Stern-Netzwerk mit 6 PCs
2. Ein Bus-Netzwerk mit 4 PCs
3. Ein Ring-Netzwerk mit 5 PCs

Welche Topologie würdest du für ein Schulnetzwerk wählen? Begründe deine Entscheidung.

---

## 🔗 Weiterführende Links

- [inf-schule.de – Rechnernetze](https://www.inf-schule.de/rechnernetze)
- [Filius – Hilfe und Dokumentation](https://www.lernsoftware-filius.de/Hilfe)
- [Video: Wie funktioniert ein Netzwerk?](https://www.youtube.com/results?search_query=Wie+funktioniert+ein+Netzwerk+einfach+erkl%C3%A4rt)

---

[Weiter → DS 02: IP-Adressen und Routing](02-IP-Adressen-und-Routing.md)
