# DS 08 – Dokumentstruktur und der Dokumentbaum

> **Themenfeld E.2 – HTML-Dokumente** · Doppelstunde 8 (3 von 8)

---

## Lernziele dieser Stunde

- Du kannst den Aufbau eines HTML-Dokuments als Baumstruktur (Dokumentbaum/DOM) darstellen.
- Du verstehst die Begriffe Elternelement, Kindelement und Geschwisterelemente.
- Du kannst HTML-Elemente korrekt verschachteln.
- Du kennst die semantischen Strukturelemente von HTML5.
- Du kannst eine Webseite mit sinnvoller Struktur aufbauen.

---

## 1. Der Dokumentbaum (DOM)

Jedes HTML-Dokument hat eine **Baumstruktur** – den sogenannten **DOM** (Document Object Model). Der Browser baut aus dem HTML-Code intern diesen Baum auf.

### Beispiel-HTML

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <title>Meine Seite</title>
</head>
<body>
    <h1>Willkommen</h1>
    <p>Ein <strong>wichtiger</strong> Text.</p>
</body>
</html>
```

### Als Baumstruktur dargestellt

```
html
├── head
│   └── title
│       └── "Meine Seite"
└── body
    ├── h1
    │   └── "Willkommen"
    └── p
        ├── "Ein "
        ├── strong
        │   └── "wichtiger"
        └── " Text."
```

### Begriffe

| Begriff | Erklärung | Beispiel |
|---------|-----------|---------|
| **Wurzelelement** | Das oberste Element | `<html>` |
| **Elternelement** (Parent) | Enthält andere Elemente | `<body>` ist Eltern von `<h1>` |
| **Kindelement** (Child) | Ist in einem anderen Element enthalten | `<h1>` ist Kind von `<body>` |
| **Geschwister** (Siblings) | Elemente auf der gleichen Ebene | `<h1>` und `<p>` sind Geschwister |
| **Nachfahre** (Descendant) | Kindelement, Enkel, ... | `<strong>` ist Nachfahre von `<body>` |

> **Python-Vergleich:** Die Baumstruktur ist vergleichbar mit verschachtelten Listen in Python:
> ```python
> html = ["head", ["title", "Meine Seite"],
>         "body", ["h1", "Willkommen",
>                  "p", ["Ein ", "strong", ["wichtiger"], " Text."]]]
> ```

---

## 2. Regeln für die Verschachtelung

### ✅ Richtig verschachtelt

Elemente müssen in der **umgekehrten Reihenfolge** geschlossen werden, in der sie geöffnet wurden:

```html
<p>Ein <strong>wichtiger</strong> Text.</p>
```

Wie Klammern in Mathe: `( [ ] )` – die innere Klammer wird zuerst geschlossen.

### ❌ Falsch verschachtelt

```html
<p>Ein <strong>wichtiger</p> Text.</strong>
```

Das ist wie `( [ ) ]` – funktioniert nicht!

### Blockebenen- vs. Inline-Elemente

| Typ | Verhalten | Beispiele |
|-----|-----------|-----------|
| **Block** | Nimmt die ganze Breite ein, beginnt in neuer Zeile | `<div>`, `<p>`, `<h1>`-`<h6>`, `<ul>`, `<table>`, `<section>` |
| **Inline** | Nimmt nur so viel Platz wie nötig, bleibt in der Zeile | `<span>`, `<strong>`, `<em>`, `<a>`, `<img>`, `<code>` |

### Verschachtelungsregeln

- **Block-Elemente** können Block- und Inline-Elemente enthalten
- **Inline-Elemente** sollten nur Inline-Elemente oder Text enthalten
- `<p>` darf **keine** Block-Elemente enthalten (kein `<div>` in `<p>`!)

```html
<!-- ✅ Richtig -->
<div>
    <p>Text mit <strong>fetten</strong> Wörtern.</p>
</div>

<!-- ❌ Falsch: Block-Element (div) in Inline-Element (span) -->
<span>
    <div>Das geht nicht!</div>
</span>
```

---

## 3. Semantische Strukturelemente (HTML5)

HTML5 bietet spezielle Elemente, um die **Bedeutung** (Semantik) der Seitenstruktur auszudrücken:

```
┌──────────────────────────────────────────────┐
│ <header>                                      │
│   Logo, Navigation                            │
├──────────────────────────────────────────────┤
│ <nav>                                         │
│   Hauptnavigation                             │
├──────────────────────────────────────────────┤
│ <main>                                        │
│   ┌─────────────────────┐ ┌────────────────┐ │
│   │ <article>           │ │ <aside>        │ │
│   │                     │ │   Seitenleiste │ │
│   │ <section>           │ │                │ │
│   │   Abschnitt 1       │ │                │ │
│   │ </section>          │ │                │ │
│   │                     │ │                │ │
│   │ <section>           │ │                │ │
│   │   Abschnitt 2       │ │                │ │
│   │ </section>          │ │                │ │
│   │                     │ │                │ │
│   └─────────────────────┘ └────────────────┘ │
├──────────────────────────────────────────────┤
│ <footer>                                      │
│   Impressum, Copyright                        │
└──────────────────────────────────────────────┘
```

### Die wichtigsten Strukturelemente

| Element | Bedeutung | Verwendung |
|---------|-----------|-----------|
| `<header>` | Kopfbereich | Logo, Seitenname, Hauptnavigation |
| `<nav>` | Navigation | Navigationslinks |
| `<main>` | Hauptinhalt | Der zentrale Inhalt der Seite (nur 1x pro Seite!) |
| `<section>` | Thematischer Abschnitt | Zusammengehörige Inhalte |
| `<article>` | Eigenständiger Inhalt | Blogbeitrag, Nachricht, Kommentar |
| `<aside>` | Nebeninhalt | Seitenleiste, weiterführende Links |
| `<footer>` | Fußbereich | Copyright, Impressum, Kontakt |
| `<div>` | Allgemeiner Container | Wenn kein semantisches Element passt |
| `<span>` | Inline-Container | Text innerhalb eines Absatzes auszeichnen |

### Unterschied: `<div>` vs. semantische Elemente

```html
<!-- ❌ Ohne Semantik – unklar, was was ist -->
<div class="oben">
    <div class="links">Navigation</div>
</div>
<div class="mitte">Inhalt</div>
<div class="unten">Copyright</div>

<!-- ✅ Mit Semantik – sofort verständlich -->
<header>
    <nav>Navigation</nav>
</header>
<main>Inhalt</main>
<footer>Copyright</footer>
```

> **Warum Semantik wichtig ist:**
> - Suchmaschinen verstehen die Seite besser
> - Screenreader (für sehbehinderte Menschen) können die Seite vorlesen
> - Der Code ist besser lesbar und wartbar

---

## 4. Eine Seite strukturieren – Komplett-Beispiel

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Informatik-Blog</title>
</head>
<body>

    <header>
        <h1>Informatik-Blog</h1>
        <nav>
            <a href="#netzwerke">Netzwerke</a> |
            <a href="#html">HTML</a> |
            <a href="#python">Python</a>
        </nav>
    </header>

    <main>
        <article id="netzwerke">
            <h2>Rechnernetze</h2>
            <section>
                <h3>Was ist ein Netzwerk?</h3>
                <p>Ein Rechnernetz verbindet mehrere Computer miteinander...</p>
            </section>
            <section>
                <h3>Netzwerkkomponenten</h3>
                <p>Die wichtigsten Komponenten sind Switch und Router...</p>
            </section>
        </article>

        <article id="html">
            <h2>HTML-Grundlagen</h2>
            <p>HTML steht für Hypertext Markup Language...</p>
        </article>

        <aside>
            <h3>Nützliche Links</h3>
            <ul>
                <li><a href="https://developer.mozilla.org/de/">MDN Web Docs</a></li>
                <li><a href="https://www.inf-schule.de/">inf-schule.de</a></li>
            </ul>
        </aside>
    </main>

    <footer>
        <p>&copy; 2026 Informatik-Klasse 11</p>
    </footer>

</body>
</html>
```

### Dokumentbaum dieses Beispiels

```
html
├── head
│   ├── meta
│   └── title
└── body
    ├── header
    │   ├── h1
    │   └── nav
    │       ├── a
    │       ├── a
    │       └── a
    ├── main
    │   ├── article#netzwerke
    │   │   ├── h2
    │   │   ├── section
    │   │   │   ├── h3
    │   │   │   └── p
    │   │   └── section
    │   │       ├── h3
    │   │       └── p
    │   ├── article#html
    │   │   ├── h2
    │   │   └── p
    │   └── aside
    │       ├── h3
    │       └── ul
    └── footer
        └── p
```

---

## 🔨 Erarbeitungsaufgabe: Dokumentbaum zeichnen und Seite strukturieren

### Teil 1: Dokumentbaum zeichnen
Zeichne den Dokumentbaum für folgenden HTML-Code:

```html
<body>
    <header>
        <h1>Meine Schule</h1>
    </header>
    <main>
        <section>
            <h2>Fächer</h2>
            <ul>
                <li>Informatik</li>
                <li>Mathematik</li>
            </ul>
        </section>
        <section>
            <h2>AG-Angebote</h2>
            <p>Wir bieten <strong>Robotik</strong> und <em>Webdesign</em> an.</p>
        </section>
    </main>
    <footer>
        <p>Kontakt: info@schule.de</p>
    </footer>
</body>
```

### Teil 2: Schulwebseite strukturieren
Erstelle in CodePen die Struktur einer Schulwebseite. Verwende die semantischen Elemente:

1. `<header>` mit Schulname und Navigation
2. `<main>` mit mindestens 2 `<section>`-Abschnitten
3. `<aside>` mit Seitenleiste (z. B. aktuelle Termine)
4. `<footer>` mit Copyright und Kontakt

> **Tipp:** Der Inhalt muss nicht lang sein – es geht um die **Struktur**!

---

## 📝 Übungsaufgaben

### Aufgabe 1: Verschachtelungsfehler
Finde und korrigiere die Verschachtelungsfehler:

```html
<p>Das ist <strong>fett und <em>kursiv</p></em></strong>
<p><div>Ein Block in einem Absatz</div></p>
<ul><p>Text in der Liste</p></ul>
```

<details>
<summary>Lösung anzeigen</summary>

```html
<!-- 1. Richtige Verschachtelungsreihenfolge -->
<p>Das ist <strong>fett und <em>kursiv</em></strong></p>

<!-- 2. Kein Block-Element (div) in einem p-Element -->
<div><p>Ein Block mit einem Absatz</p></div>

<!-- 3. Nur li-Elemente direkt in ul -->
<ul><li><p>Text in der Liste</p></li></ul>
<!-- oder einfacher: -->
<ul><li>Text in der Liste</li></ul>
```
</details>

### Aufgabe 2: DOM-Fragen
Beantworte für das Komplett-Beispiel (Informatik-Blog):
1. Was ist das Elternelement von `<h2>Rechnernetze</h2>`?
2. Welche Geschwisterelemente hat das `<aside>`-Element?
3. Wie viele Kindelemente hat das `<main>`-Element?
4. Ist `<h3>` ein Nachfahre von `<main>`?

<details>
<summary>Lösung anzeigen</summary>

1. `<article id="netzwerke">`
2. `<article id="netzwerke">` und `<article id="html">`
3. Drei: `article#netzwerke`, `article#html`, `aside`
4. Ja! `<h3>` → `<section>` → `<article>` → `<main>` (indirektes Kind / Nachfahre)
</details>

### Aufgabe 3: Semantische Zuordnung
Welches semantische Element würdest du für folgende Inhalte verwenden?

1. Der Seitenname und das Logo oben auf der Seite
2. Eine Sammlung von Links zu allen Unterseiten
3. Ein einzelner Blogbeitrag
4. „Copyright 2026" ganz unten
5. Eine Seitenleiste mit „Ähnlichen Artikeln"
6. Ein Kapitel innerhalb eines Blogbeitrags

<details>
<summary>Lösung anzeigen</summary>

1. `<header>`
2. `<nav>`
3. `<article>`
4. `<footer>`
5. `<aside>`
6. `<section>`
</details>

### Aufgabe 4: Kompletten Dokumentbaum zeichnen
Nimm deine Informationsseite aus DS 07 und zeichne den vollständigen Dokumentbaum auf Papier. Markiere:
- Eltern-Kind-Beziehungen mit Linien
- Block-Elemente in einer Farbe
- Inline-Elemente in einer anderen Farbe

---

## 🔗 Weiterführende Links

- [MDN – HTML-Dokumentstruktur](https://developer.mozilla.org/de/docs/Learn/HTML/Introduction_to_HTML/Document_and_website_structure)
- [MDN – Semantisches HTML](https://developer.mozilla.org/de/docs/Glossary/Semantics)
- [selfhtml – HTML-Struktur](https://wiki.selfhtml.org/wiki/HTML/Tutorials/Seitenstrukturierung)

---

[← Zurück: DS 07](02-HTML-Elemente.md) · [Weiter → DS 09: Hyperlinks](04-Hyperlinks.md)
