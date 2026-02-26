# Internet und HTML – Lerneinheit Informatik Klasse 11

> **Themenfelder E.1 (Internetprotokolle) und E.2 (HTML-Dokumente)**  
> nach dem Kerncurriculum Gymnasiale Oberstufe (KCGO) Informatik, Hessen

---

## Übersicht

Diese Lerneinheit umfasst ca. **13 Doppelstunden** und deckt die verbindlichen Themenfelder E.1 und E.2 der Einführungsphase ab:

| # | Thema | Themenfeld | Werkzeug |
|---|-------|------------|----------|
| **DS 01** | [Rechnernetze – Aufbau und Komponenten](E1-Internetprotokolle/01-Rechnernetze.md) | E.1 | Filius |
| **DS 02** | [IP-Adressen und Routing](E1-Internetprotokolle/02-IP-Adressen-und-Routing.md) | E.1 | Filius |
| **DS 03** | [Das Domain Name System (DNS)](E1-Internetprotokolle/03-DNS.md) | E.1 | Filius |
| **DS 04** | [Das TCP/IP-Referenzmodell](E1-Internetprotokolle/04-TCP-IP-Modell.md) | E.1 | Filius |
| **DS 05** | [Client-Server-Architektur, Protokolle und Sicherheit](E1-Internetprotokolle/05-Client-Server-und-Sicherheit.md) | E.1 | Filius + Python |
| **DS 06** | [HTML-Grundgerüst und erste Schritte](E2-HTML-Dokumente/01-HTML-Grundgeruest.md) | E.2 | CodePen |
| **DS 07** | [HTML-Elemente: Texte, Listen, Bilder, Medien](E2-HTML-Dokumente/02-HTML-Elemente.md) | E.2 | CodePen |
| **DS 08** | [Dokumentstruktur und der Dokumentbaum](E2-HTML-Dokumente/03-Dokumentstruktur.md) | E.2 | CodePen |
| **DS 09** | [Hyperlinks und Seitenvernetzung](E2-HTML-Dokumente/04-Hyperlinks.md) | E.2 | CodePen |
| **DS 10** | [CSS-Grundlagen: Selektoren und Eigenschaften](E2-HTML-Dokumente/05-CSS-Grundlagen.md) | E.2 | CodePen |
| **DS 11** | [CSS-Layout mit Grid](E2-HTML-Dokumente/06-CSS-Layout-Grid.md) | E.2 | CodePen |
| **DS 12** | [Formulare und JavaScript-Grundlagen](E2-HTML-Dokumente/07-Formulare-und-JavaScript.md) | E.2 | CodePen |
| **DS 13** | [Abschlussprojekt: Eigene Website](E2-HTML-Dokumente/08-Abschlussprojekt.md) | E.2 | CodePen |

---

## Werkzeuge

### Filius (Netzwerksimulation)
- **Download:** [https://www.lernsoftware-filius.de/Herunterladen](https://www.lernsoftware-filius.de/Herunterladen)
- Filius ist eine kostenlose Lernsoftware zur Simulation von Rechnernetzen
- Läuft auf Windows, macOS und Linux (Java erforderlich)

### CodePen (HTML/CSS/JS-Editor)
- **URL:** [https://codepen.io/pen/](https://codepen.io/pen/)
- Online-Editor für HTML, CSS und JavaScript – keine Installation nötig
- Ergebnisse werden live angezeigt
- Alternative: [JSFiddle](https://jsfiddle.net/) oder [HTML-Online](https://html-online.com/editor/)

### Thonny (Python-Programmierung)
- **Download:** [https://thonny.org/](https://thonny.org/)
- Wird für die Python-Netzwerkbeispiele in DS 05 genutzt

---

## Voraussetzungen

- Grundkenntnisse in **Python** (Variablen, Schleifen, Funktionen)
- Keine Vorkenntnisse in HTML, CSS oder Netzwerktechnik erforderlich

---

## Struktur des Repositories

```
InternetUndHTML/
├── README.md                          ← diese Datei
├── E1-Internetprotokolle/
│   ├── README.md                      ← Überblick Themenfeld E.1
│   ├── 01-Rechnernetze.md
│   ├── 02-IP-Adressen-und-Routing.md
│   ├── 03-DNS.md
│   ├── 04-TCP-IP-Modell.md
│   ├── 05-Client-Server-und-Sicherheit.md
│   ├── filius-anleitungen/            ← Schritt-für-Schritt-Anleitungen für Filius
│   └── python/                        ← Python-Beispiele (Client/Server)
└── E2-HTML-Dokumente/
    ├── README.md                      ← Überblick Themenfeld E.2
    ├── 01-HTML-Grundgeruest.md
    ├── 02-HTML-Elemente.md
    ├── 03-Dokumentstruktur.md
    ├── 04-Hyperlinks.md
    ├── 05-CSS-Grundlagen.md
    ├── 06-CSS-Layout-Grid.md
    ├── 07-Formulare-und-JavaScript.md
    ├── 08-Abschlussprojekt.md
    ├── beispiele/                     ← HTML/CSS-Beispieldateien
    └── vorlagen/                      ← Vorlagen für Übungen und Projekt
```

---

## Bezug zum KCGO

### Themenfeld E.1 – Internetprotokolle
- **Rechnernetze:** Aufbau und Bestandteile, Funktion von Komponenten
- **Grundlagen des Internets:** IP-Adresse, Domain Name System (DNS), TCP/IP-Referenzmodell
- **Client-Server-Architektur:** Client, Server, Dienst, Protokoll, Sicherheitsaspekte

### Themenfeld E.2 – HTML-Dokumente
- **HTML5:** Grundgerüst, grundlegende Elemente, Tags, Attribute, Hyperlinks
- **Struktur von HTML-Dokumenten:** Dokumentbaum, Schachtelung, strukturierende Elemente
- **CSS3:** Selektoren, grundlegende CSS-Attribute, Grid-Layout
- **Formulare:** Formularelemente und Versand der Eingabedaten

---

## Lizenz

Dieses Material steht unter der [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de)-Lizenz und darf frei verwendet, verändert und weitergegeben werden.
