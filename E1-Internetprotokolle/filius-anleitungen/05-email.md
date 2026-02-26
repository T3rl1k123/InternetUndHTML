# Filius-Anleitung: E-Mail-Kommunikation simulieren

> Zu [DS 05 – Client-Server und Sicherheit](../05-Client-Server-und-Sicherheit.md)

---

## Ziel

E-Mail-Kommunikation mit SMTP und POP3 in Filius simulieren und die Protokolle im Datenaustausch analysieren.

## Netzplan

```
Netzwerk: 192.168.1.0/24

  PC-Anna (192.168.1.1) ─────┐
                              Switch
  PC-Bob (192.168.1.2) ──────┤
  Mailserver (192.168.1.10) ──┤
  DNS-Server (192.168.1.20) ──┘
```

## Schritt 1: Netzwerk aufbauen (Entwurfsmodus)

| Gerät | IP-Adresse | Subnetzmaske | DNS-Server |
|-------|-----------|-------------|------------|
| PC-Anna | `192.168.1.1` | `255.255.255.0` | `192.168.1.20` |
| PC-Bob | `192.168.1.2` | `255.255.255.0` | `192.168.1.20` |
| Mailserver | `192.168.1.10` | `255.255.255.0` | – |
| DNS-Server | `192.168.1.20` | `255.255.255.0` | – |

## Schritt 2: DNS-Server einrichten (Aktionsmodus)

1. Doppelklicke auf den DNS-Server
2. Installiere und starte den **DNS-Server**
3. Füge hinzu: `mail.schule.de` → `192.168.1.10`

## Schritt 3: Mailserver einrichten

1. Doppelklicke auf den Mailserver
2. Installiere den **E-Mail-Server**
3. Starte den E-Mail-Server
4. Richte Benutzerkonten ein:
   - Benutzername: `anna`, Passwort: `anna123`, E-Mail: `anna@schule.de`
   - Benutzername: `bob`, Passwort: `bob456`, E-Mail: `bob@schule.de`

## Schritt 4: E-Mail-Programm bei Anna einrichten

1. Doppelklicke auf PC-Anna
2. Installiere das **E-Mail-Programm**
3. Konfiguriere:
   - **Name:** Anna
   - **E-Mail-Adresse:** `anna@schule.de`
   - **POP3-Server:** `mail.schule.de`
   - **SMTP-Server:** `mail.schule.de`
   - **Benutzername:** `anna`
   - **Passwort:** `anna123`

## Schritt 5: E-Mail-Programm bei Bob einrichten

Analog zu Anna:
- E-Mail: `bob@schule.de`, Benutzername: `bob`, Passwort: `bob456`

## Schritt 6: E-Mail senden und empfangen

1. **Datenaustausch aktivieren** (Rechtsklick → Datenaustausch anzeigen) auf PC-Anna und PC-Bob
2. Bei **PC-Anna**: Verfasse eine neue E-Mail:
   - An: `bob@schule.de`
   - Betreff: „Testmail"
   - Text: „Hallo Bob, das ist eine Testmail!"
   - Klicke auf **Senden**
3. Bei **PC-Bob**: Klicke auf **E-Mails abrufen**
4. Die E-Mail von Anna sollte im Posteingang erscheinen ✅

## Schritt 7: Protokolle analysieren

### Beim Senden (Anna → Mailserver, SMTP):
Suche im Datenaustausch nach Paketen mit **Port 25** (SMTP). Du solltest sehen:
- `HELO`, `MAIL FROM:`, `RCPT TO:`, `DATA`, `QUIT`

### Beim Abrufen (Bob ← Mailserver, POP3):
Suche nach Paketen mit **Port 110** (POP3). Du solltest sehen:
- `USER`, `PASS` (⚠️ Passwort im Klartext!), `LIST`, `RETR`, `QUIT`

## Sicherheitsbeobachtung

Achte besonders auf den POP3-Austausch:
- Das Passwort `bob456` wird im **Klartext** übertragen!
- Jeder, der den Netzwerkverkehr abhört, kann es lesen
- **Das ist ein echtes Sicherheitsproblem** bei unverschlüsselten Protokollen

---

[Zurück zur Übersicht](../05-Client-Server-und-Sicherheit.md)
