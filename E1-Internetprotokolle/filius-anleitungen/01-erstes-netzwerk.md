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

## Fertig! ✅

Dein erstes Netzwerk funktioniert. Alle drei PCs können miteinander kommunizieren.

---

[Zurück zur Übersicht](../01-Rechnernetze.md)
