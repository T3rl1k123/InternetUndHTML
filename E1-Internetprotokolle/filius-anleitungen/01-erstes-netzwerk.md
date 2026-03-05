# Filius-Anleitung: Erstes Netzwerk aufbauen

> Zu [DS 01 – Rechnernetze](../01-Rechnernetze.md)

---

## Ziel

Ein einfaches Netzwerk mit 3 PCs und einem Switch in Filius aufbauen und die Kommunikation testen.

## Schritt 1: Filius starten

1. Starte Filius
2. Du befindest dich im **Entwurfsmodus** (Schraubenschlüssel-Symbol oben links ist aktiv)

## Schritt 2: Switch platzieren

1. Klicke in der Werkzeugleiste auf das **Switch-Symbol** (sieht aus wie ein kleiner Kasten mit Verbindungen)
2. Klicke auf die **Mitte der Arbeitsfläche**, um den Switch dort zu platzieren
3. Optional: Benenne den Switch per Doppelklick als „Switch1"

## Schritt 3: PCs platzieren

1. Klicke auf das **Rechner-Symbol** in der Werkzeugleiste
2. Klicke links oben auf die Arbeitsfläche → PC1 wird platziert
3. Wiederhole das für PC2 (rechts oben) und PC3 (unten)

## Schritt 4: Kabel verlegen

1. Klicke auf das **Kabel-Symbol** in der Werkzeugleiste
2. Klicke auf **PC1** und dann auf den **Switch** → Verbindung wird erstellt
3. Wiederhole für PC2 → Switch und PC3 → Switch

## Schritt 5: IP-Adressen konfigurieren

Für jeden PC:

1. **Doppelklicke** auf den PC
2. Im Konfigurationsfenster:
   - **Name:** PC1 (bzw. PC2, PC3)
   - **IP-Adresse:** siehe Tabelle unten
   - **Subnetzmaske:** `255.255.255.0`

| PC | IP-Adresse | Subnetzmaske |
|----|-----------|-------------|
| PC1 | `192.168.1.1` | `255.255.255.0` |
| PC2 | `192.168.1.2` | `255.255.255.0` |
| PC3 | `192.168.1.3` | `255.255.255.0` |

## Schritt 6: Netzwerk testen

1. Klicke auf den **grünen Pfeil** (▶️) oben links, um in den **Aktionsmodus** zu wechseln
2. **Doppelklicke** auf PC1
3. Klicke auf **Software installieren** → installiere **Befehlszeile**
4. Starte die **Befehlszeile**
5. Gib ein: `ping 192.168.1.2`
6. Du solltest Antworten sehen wie:
   ```
   Antwort von 192.168.1.2 empfangen
   ```
7. Teste auch: `ping 192.168.1.3`

## Schritt 7: ARP-Datenverkehr analysieren

> **Was ist ARP?**  
> Das *Address Resolution Protocol* (ARP) übersetzt IP-Adressen in MAC-Adressen. Bevor PC1 ein Paket an PC2 schicken kann, muss er wissen, welche **MAC-Adresse** hinter der IP-Adresse `192.168.1.2` steckt. IP- und MAC-Adresse unterscheiden sich in Funktion und Gültigkeitsbereich – mehr dazu in [DS 02, Abschnitt 2](../02-IP-Adressen-und-Routing.md).

### Vorbereitung

1. Bleibe im **Aktionsmodus** (▶️)
2. **Rechtsklicke** auf PC1 und wähle **„Datenaustausch anzeigen"**
3. Das Datenaustausch-Fenster öffnet sich – es protokolliert alle gesendeten und empfangenen Pakete

### Auftrag: Ping beobachten

4. Öffne erneut die **Befehlszeile** auf PC1 (oder wechsle in das bereits offene Fenster)
5. Sende einen **neuen Ping** (damit ARP sichtbar wird – falls noch kein Paket gelaufen ist):
   ```
   ping 192.168.1.2
   ```
6. Beobachte das Datenaustausch-Fenster: Vor dem ersten ICMP-Ping-Paket erscheint eine **ARP-Anfrage**

### Analyse-Aufgaben (schriftlich beantworten)

1. **Welche Adressen** stehen in der ARP-Anfrage?  
   *(Hinweis: Die Ziel-IP ist eine Broadcast-Adresse – welche könnte das sein?)*

2. **Welche MAC-Adresse** zeigt PC1 als Absenderadresse?  
   Vergleiche sie mit der Konfigurationsanzeige von PC1 (Doppelklick im Entwurfsmodus).

3. **MAC vs. IP – worin besteht der Unterschied?**  
   Erkläre in eigenen Worten, was der Unterschied zwischen einer MAC-Adresse und einer IP-Adresse ist.  
   *(Tipp: Schaue in [DS 02 – Abschnitt 2](../02-IP-Adressen-und-Routing.md) nach.)*

4. **Warum ARP zuerst?**  
   Warum schickt PC1 zunächst eine ARP-Anfrage, bevor es den eigentlichen Ping sendet?

5. **Bonus:** Führe den Ping **ein zweites Mal** aus. Erscheint dabei erneut eine ARP-Anfrage?  
   Erkläre, warum (nicht). *(Stichwort: ARP-Cache)*

## Fertig! ✅

Dein erstes Netzwerk funktioniert. Alle drei PCs können miteinander kommunizieren.

---

[Zurück zur Übersicht](../01-Rechnernetze.md)
