# DS 09 – Hyperlinks und Seitenvernetzung

> **Themenfeld E.2 – HTML-Dokumente** · Doppelstunde 9 (4 von 8)

---

## Lernziele dieser Stunde

- Du kannst Hyperlinks mit dem `<a>`-Tag erstellen.
- Du verstehst den Unterschied zwischen absoluten und relativen Links.
- Du kannst Ankerlinks (interne Sprungmarken) verwenden.
- Du kannst eine Navigation für eine mehrseitige Website erstellen.
- Du verstehst das Konzept von Hypertext.

---

## 1. Was ist ein Hyperlink?

Ein **Hyperlink** (kurz: Link) ist eine Verknüpfung zu einer anderen Ressource – z. B. einer anderen Webseite, einer Datei oder einer Stelle auf der gleichen Seite.

> **Hypertext:** Text, der über Links miteinander verknüpft ist. Das „HT" in HTML steht für Hypertext! Hypertext war die revolutionäre Idee hinter dem World Wide Web.

### Das `<a>`-Tag

```html
<a href="https://www.example.com">Klick mich!</a>
```

| Bestandteil | Bedeutung |
|-------------|-----------|
| `<a>` | Anchor-Element (Anker) |
| `href` | Hypertext Reference – die Zieladresse |
| `"https://..."` | Die URL / der Pfad zum Ziel |
| `Klick mich!` | Der sichtbare Linktext |

---

## 2. Arten von Links

### Absolute Links (volle URL)

Verweisen auf eine **komplette Webadresse**:

```html
<a href="https://www.google.de">Google</a>
<a href="https://de.wikipedia.org/wiki/HTML">HTML in Wikipedia</a>
```

### Relative Links (innerhalb der eigenen Website)

Verweisen auf eine **andere Seite** auf dem gleichen Server:

```html
<!-- Datei im gleichen Ordner -->
<a href="kontakt.html">Kontakt</a>

<!-- Datei in einem Unterordner -->
<a href="bilder/galerie.html">Galerie</a>

<!-- Datei im übergeordneten Ordner -->
<a href="../index.html">Zurück zur Startseite</a>
```

### Verzeichnisstruktur für relative Links

```
meine-website/
├── index.html          ← Startseite
├── ueber-mich.html     ← von index.html: href="ueber-mich.html"
├── kontakt.html
├── bilder/
│   └── galerie.html    ← von index.html: href="bilder/galerie.html"
└── blog/
    ├── post1.html       ← von post1 zu index: href="../index.html"
    └── post2.html
```

### Ankerlinks (Sprungmarken auf der gleichen Seite)

Du kannst zu einer bestimmten Stelle auf der gleichen Seite springen:

```html
<!-- Der Link (springt zu dem Element mit id="kapitel2") -->
<a href="#kapitel2">Zu Kapitel 2 springen</a>

<!-- Das Ziel (irgendwo weiter unten auf der Seite) -->
<h2 id="kapitel2">Kapitel 2: CSS</h2>
```

> **Merke:** `#` vor dem Namen = Ankerlink innerhalb der Seite

### E-Mail-Links

```html
<a href="mailto:info@schule.de">E-Mail schreiben</a>
```

---

## 3. Link-Attribute

| Attribut | Wert | Bedeutung |
|----------|------|-----------|
| `href` | URL/Pfad | Ziel des Links |
| `target` | `_blank` | Öffnet den Link in einem neuen Tab |
| `target` | `_self` | Öffnet im gleichen Tab (Standard) |
| `title` | Text | Tooltip beim Hover |

```html
<!-- Öffnet in neuem Tab -->
<a href="https://www.google.de" target="_blank">Google (neuer Tab)</a>

<!-- Mit Tooltip -->
<a href="kontakt.html" title="Zur Kontaktseite">Kontakt</a>
```

---

## 4. Navigation erstellen

Eine **Navigation** ist eine Sammlung von Links, die auf verschiedene Seiten der Website verweist:

```html
<nav>
    <a href="index.html">Startseite</a>
    <a href="ueber-mich.html">Über mich</a>
    <a href="projekte.html">Projekte</a>
    <a href="kontakt.html">Kontakt</a>
</nav>
```

### Navigation als Liste (empfohlen)

```html
<nav>
    <ul>
        <li><a href="index.html">Startseite</a></li>
        <li><a href="ueber-mich.html">Über mich</a></li>
        <li><a href="projekte.html">Projekte</a></li>
        <li><a href="kontakt.html">Kontakt</a></li>
    </ul>
</nav>
```

> Die `<nav>`-Liste wird später mit CSS horizontal gestaltet (→ DS 10/11).

---

## 5. Bilder als Links

Ein Bild kann als Link verwendet werden, indem man ein `<img>` in ein `<a>` packt:

```html
<a href="https://www.example.com">
    <img src="logo.png" alt="Zum Beispiel-Website">
</a>
```

---

## 6. Links und das HTTP-Konzept

Wenn du auf einen Link klickst, passiert im Hintergrund das, was wir in E.1 gelernt haben:

```
1. Browser liest das href-Attribut: "https://www.example.com/seite.html"
2. DNS-Auflösung: www.example.com → 93.184.216.34
3. TCP-Verbindung zum Server (Port 443 bei HTTPS)
4. HTTP-Anfrage: GET /seite.html HTTP/1.1
5. Server antwortet mit dem HTML-Code
6. Browser zeigt die neue Seite an
```

> So verbinden sich die Themenfelder E.1 und E.2!

---

## 🔨 Erarbeitungsaufgabe: Mehrseitige Mini-Website

Erstelle in CodePen eine **mehrseitige Mini-Website** (oder simuliere sie mit Ankerlinks). Die Website hat ein Thema deiner Wahl und besteht aus mindestens 3 „Seiten":

### Variante A: Mit Ankerlinks (in einem CodePen)

Da CodePen nur eine Seite unterstützt, simuliere mehrere Seiten mit **Ankerlinks**:

```html
<!-- Navigation -->
<nav>
    <a href="#home">Home</a> |
    <a href="#info">Info</a> |
    <a href="#kontakt">Kontakt</a>
</nav>

<!-- "Seite" 1 -->
<section id="home">
    <h1>Willkommen</h1>
    <p>...</p>
</section>

<!-- "Seite" 2 -->
<section id="info">
    <h2>Informationen</h2>
    <p>...</p>
</section>

<!-- "Seite" 3 -->
<section id="kontakt">
    <h2>Kontakt</h2>
    <p>...</p>
</section>
```

### Variante B: Mit echten HTML-Dateien (lokal)

Erstelle drei HTML-Dateien in einem Ordner und öffne sie im Browser:
- `index.html` (Startseite)
- `info.html` (Informationen)
- `kontakt.html` (Kontakt)

Jede Seite hat die gleiche Navigation mit Links zu den anderen Seiten.

> **Vorlage:** Siehe [`vorlagen/mehrseitige-website/`](vorlagen/)

### Anforderungen

1. Eine **Navigation** mit Links zu allen Seiten/Abschnitten
2. Mindestens ein **externer Link** (zu einer echten Website)
3. Mindestens ein **Bild als Link**
4. Mindestens ein **E-Mail-Link**
5. Sinnvolle Verwendung von semantischen Elementen (`<header>`, `<nav>`, `<main>`, `<footer>`)

---

## 📝 Übungsaufgaben

### Aufgabe 1: Linktypen bestimmen
Bestimme für jeden Link den Typ (absolut, relativ, Ankerlink, E-Mail):

```html
<a href="https://www.mozilla.org">Mozilla</a>
<a href="seite2.html">Seite 2</a>
<a href="#fazit">Zum Fazit</a>
<a href="../index.html">Startseite</a>
<a href="mailto:hans@example.com">Mail an Hans</a>
<a href="bilder/foto.html">Fotos</a>
```

<details>
<summary>Lösung anzeigen</summary>

1. `https://www.mozilla.org` → **absoluter Link**
2. `seite2.html` → **relativer Link** (gleicher Ordner)
3. `#fazit` → **Ankerlink** (gleiche Seite)
4. `../index.html` → **relativer Link** (übergeordneter Ordner)
5. `mailto:hans@example.com` → **E-Mail-Link**
6. `bilder/foto.html` → **relativer Link** (Unterordner)
</details>

### Aufgabe 2: Pfade bestimmen
Gegeben ist die Verzeichnisstruktur:

```
website/
├── index.html
├── css/
│   └── style.css
├── seiten/
│   ├── about.html
│   └── projekte/
│       └── projekt1.html
└── bilder/
    └── logo.png
```

Gib den korrekten relativen Pfad an:
1. Von `index.html` zu `about.html`
2. Von `about.html` zu `index.html`
3. Von `projekt1.html` zu `logo.png`
4. Von `index.html` zu `logo.png`
5. Von `projekt1.html` zu `about.html`

<details>
<summary>Lösung anzeigen</summary>

1. `seiten/about.html`
2. `../index.html`
3. `../../bilder/logo.png`
4. `bilder/logo.png`
5. `../about.html`
</details>

### Aufgabe 3: Inhaltsverzeichnis mit Ankerlinks
Erstelle eine lange Webseite (z. B. eine FAQ-Seite) mit:
- Einem Inhaltsverzeichnis am Anfang (mit Ankerlinks)
- Mindestens 5 Abschnitten mit jeweils einer Überschrift
- Einem „Zurück nach oben"-Link am Ende jedes Abschnitts

### Aufgabe 4: Vernetzte Wikipedia-Seite
Erstelle eine „Mini-Wikipedia"-Seite über ein Informatik-Thema (z. B. Netzwerke). Der Text soll:
- Mindestens 5 interne Ankerlinks zwischen verschiedenen Abschnitten haben
- Mindestens 3 externe Links zu echten Wikipedia-Artikeln enthalten
- Ein Inhaltsverzeichnis mit Ankerlinks haben

---

## 🔗 Weiterführende Links

- [MDN – Hyperlinks erstellen](https://developer.mozilla.org/de/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks)
- [selfhtml – Links](https://wiki.selfhtml.org/wiki/HTML/Tutorials/Links)

---

[← Zurück: DS 08](03-Dokumentstruktur.md) · [Weiter → DS 10: CSS-Grundlagen](05-CSS-Grundlagen.md)
