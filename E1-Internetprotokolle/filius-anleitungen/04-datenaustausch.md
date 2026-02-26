# Filius-Anleitung: Datenaustausch beobachten

> Zu [DS 04 – TCP/IP-Referenzmodell](../04-TCP-IP-Modell.md)

---

## Ziel

Den Datenaustausch zwischen Client und Webserver in Filius beobachten und die Protokolle der verschiedenen TCP/IP-Schichten identifizieren.

## Voraussetzung

Du brauchst das Netzwerk aus DS 03 mit DNS-Server und Webserver, oder baust es neu auf.

## Schritt 1: Datenaustausch aktivieren

1. Wechsle in den **Aktionsmodus** (▶️)
2. **Rechtsklicke** auf den PC-Client
3. Wähle **„Datenaustausch anzeigen"** (oder klicke auf das Tabellen-Symbol)
4. Es öffnet sich ein Fenster, das den Datenaustausch dieses PCs mitprotokolliert

> **Tipp:** Du kannst den Datenaustausch an jedem Gerät beobachten!

## Schritt 2: Webseite aufrufen

1. Öffne den **Webbrowser** am PC-Client
2. Rufe `www.meineschule.de` auf
3. Beobachte das Datenaustausch-Fenster

## Schritt 3: Protokolle analysieren

Im Datenaustausch-Fenster siehst du einzelne Pakete mit Details wie:
- **Quell-IP** und **Ziel-IP**
- **Quell-Port** und **Ziel-Port**
- **Protokoll** (DNS, TCP, HTTP, …)
- **Inhalt** des Pakets

### Erwarteter Ablauf

| Nr. | Von → Nach | Protokoll | Beschreibung |
|-----|-----------|-----------|-------------|
| 1 | Client → DNS | DNS (UDP) | DNS-Anfrage: „IP von www.meineschule.de?" |
| 2 | DNS → Client | DNS (UDP) | DNS-Antwort: „192.168.1.20" |
| 3 | Client → Webserver | TCP | SYN (Verbindungsaufbau – Schritt 1) |
| 4 | Webserver → Client | TCP | SYN-ACK (Schritt 2) |
| 5 | Client → Webserver | TCP | ACK (Schritt 3 – Verbindung steht!) |
| 6 | Client → Webserver | HTTP | GET /index.html HTTP/1.1 |
| 7 | Webserver → Client | HTTP | HTTP/1.1 200 OK + HTML-Inhalt |
| 8-10 | … | TCP | Verbindungsabbau (FIN, ACK) |

## Schritt 4: Dokumentieren

Erstelle eine Tabelle wie oben und ordne jedes beobachtete Paket einer **Schicht des TCP/IP-Modells** zu:

| Paket | Schicht | Protokoll |
|-------|---------|-----------|
| DNS-Anfrage/Antwort | 4 – Anwendung | DNS |
| SYN/SYN-ACK/ACK | 3 – Transport | TCP |
| GET-Request | 4 – Anwendung | HTTP |
| IP-Header | 2 – Internet | IP |

## Tipps für die Analyse

- **DNS-Pakete** erkennst du am Ziel-Port 53
- **HTTP-Pakete** erkennst du am Ziel-Port 80
- Der **TCP-Dreiwege-Handshake** besteht immer aus 3 Paketen (SYN → SYN-ACK → ACK)
- Klicke auf ein Paket, um dessen Details zu sehen

---

[Zurück zur Übersicht](../04-TCP-IP-Modell.md)
