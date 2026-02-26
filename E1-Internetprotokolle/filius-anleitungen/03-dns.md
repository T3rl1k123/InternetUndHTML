# Filius-Anleitung: DNS-Server einrichten

> Zu [DS 03 – DNS](../03-DNS.md)

---

## Ziel

Einen DNS-Server und Webserver in Filius einrichten, sodass Webseiten über einen Domainnamen erreichbar sind.

## Netzplan

```
Netzwerk: 192.168.1.0/24

  PC-Client (192.168.1.1) ──────┐
                                Switch
  DNS-Server (192.168.1.10) ────┤
  Webserver (192.168.1.20) ─────┘
```

## Schritt 1: Netzwerk aufbauen (Entwurfsmodus)

1. Platziere 1 Switch, 1 PC, 2 weitere Rechner (DNS-Server und Webserver)
2. Verbinde alle mit dem Switch

### IP-Konfiguration

| Gerät | Name | IP-Adresse | Subnetzmaske | DNS-Server |
|-------|------|-----------|-------------|------------|
| PC | PC-Client | `192.168.1.1` | `255.255.255.0` | `192.168.1.10` |
| Rechner | DNS-Server | `192.168.1.10` | `255.255.255.0` | – |
| Rechner | Webserver | `192.168.1.20` | `255.255.255.0` | – |

> **Wichtig:** Beim PC-Client muss der DNS-Server (`192.168.1.10`) eingetragen werden!

## Schritt 2: In den Aktionsmodus wechseln (▶️)

## Schritt 3: Webserver einrichten

1. **Doppelklicke** auf den Webserver (192.168.1.20)
2. Klicke auf **Software installieren**
3. Installiere den **Webserver**
4. Starte den Webserver (grüner Startbutton)
5. Der Webserver hat automatisch eine Startseite (`index.html`)

> **Optional:** Du kannst die Startseite bearbeiten und eigenen HTML-Code eingeben.

## Schritt 4: DNS-Server einrichten

1. **Doppelklicke** auf den DNS-Server (192.168.1.10)
2. Klicke auf **Software installieren**
3. Installiere den **DNS-Server**
4. Starte den DNS-Server
5. Klicke auf den DNS-Server, um ihn zu konfigurieren
6. **Füge einen Eintrag (A-Record) hinzu:**
   - **Domainname:** `www.meineschule.de`
   - **IP-Adresse:** `192.168.1.20`
   - Klicke auf „Hinzufügen"

## Schritt 5: Testen

1. **Doppelklicke** auf den PC-Client
2. Installiere den **Webbrowser**
3. Starte den Webbrowser
4. Gib in die Adresszeile ein: `www.meineschule.de`
5. Die Startseite des Webservers sollte erscheinen ✅

### Alternativ mit der Befehlszeile testen:
1. Installiere die **Befehlszeile** auf dem PC-Client
2. `ping www.meineschule.de` → Zeigt die aufgelöste IP-Adresse

## Schritt 6: Weitere Domains hinzufügen (optional)

Du kannst im DNS-Server beliebig viele Einträge hinzufügen:

| Domainname | IP-Adresse |
|-----------|-----------|
| `www.meineschule.de` | `192.168.1.20` |
| `www.bibliothek.de` | `192.168.1.30` |
| `mail.schule.de` | `192.168.1.40` |

Dafür müssen natürlich auch die entsprechenden Server existieren!

---

[Zurück zur Übersicht](../03-DNS.md)
