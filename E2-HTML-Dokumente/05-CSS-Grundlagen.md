# DS 10 – CSS-Grundlagen: Selektoren und Eigenschaften

> **Themenfeld E.2 – HTML-Dokumente** · Doppelstunde 10 (5 von 8)

---

## Lernziele dieser Stunde

- Du weißt, was CSS ist und wozu es dient.
- Du kennst die drei Möglichkeiten, CSS einzubinden.
- Du kannst CSS-Selektoren (Element, Klasse, ID) anwenden.
- Du kennst grundlegende CSS-Eigenschaften für Farben, Schriften und Abstände.
- Du verstehst das Box-Modell.

---

## 1. Was ist CSS?

**CSS** steht für **C**ascading **S**tyle **S**heets – zu Deutsch: gestufte Gestaltungsbögen.

- HTML definiert die **Struktur** und den **Inhalt** einer Webseite
- CSS definiert das **Aussehen** – Farben, Schriften, Abstände, Layout

### Trennung von Inhalt und Darstellung

```
HTML = WAS auf der Seite steht    →  <h1>Willkommen</h1>
CSS  = WIE es aussieht            →  h1 { color: blue; font-size: 36px; }
```

> **Warum trennen?** Man kann das Design einer ganzen Website ändern, ohne den HTML-Code anzufassen!

---

## 2. CSS einbinden – drei Wege

### a) Inline-CSS (direkt im Tag)

```html
<h1 style="color: blue; font-size: 36px;">Blaue Überschrift</h1>
```
❌ Nicht empfohlen – vermischt HTML und CSS

### b) Internes CSS (im `<head>`)

```html
<head>
    <style>
        h1 {
            color: blue;
            font-size: 36px;
        }
    </style>
</head>
```
⚠️ OK für einzelne Seiten

### c) Externes CSS (separate Datei) ✅ Empfohlen

```html
<!-- In der HTML-Datei (head-Bereich): -->
<link rel="stylesheet" href="style.css">
```

```css
/* In der Datei style.css: */
h1 {
    color: blue;
    font-size: 36px;
}
```
✅ Best Practice – eine CSS-Datei für die ganze Website

> **In CodePen** gibst du den CSS-Code einfach im **CSS-Feld** ein – das entspricht einem externen Stylesheet.

---

## 3. CSS-Syntax

Eine CSS-Regel besteht aus **Selektor** und **Deklarationsblock**:

```css
selektor {
    eigenschaft: wert;
    eigenschaft: wert;
}
```

### Beispiel

```css
h1 {
    color: blue;
    font-size: 36px;
    text-align: center;
}
```

| Teil | Bedeutung |
|------|-----------|
| `h1` | **Selektor** – welches Element wird gestaltet |
| `{ }` | **Deklarationsblock** – enthält die Regeln |
| `color: blue;` | **Deklaration** – Eigenschaft und Wert |
| `color` | **Eigenschaft** (Property) |
| `blue` | **Wert** (Value) |
| `;` | Trennt Deklarationen voneinander |

---

## 4. CSS-Selektoren

### Element-Selektor

Wählt **alle** Elemente eines Typs aus:

```css
p {
    color: #333;
}
/* → Alle <p>-Elemente werden dunkelgrau */

h1 {
    font-size: 2em;
}
/* → Alle <h1>-Elemente bekommen Schriftgröße 2em */
```

### Klassen-Selektor (`.`)

Wählt alle Elemente mit einer bestimmten **Klasse** aus:

```html
<p class="wichtig">Dieser Text ist wichtig!</p>
<p>Dieser Text ist normal.</p>
<p class="wichtig">Auch dieser ist wichtig!</p>
```

```css
.wichtig {
    color: red;
    font-weight: bold;
}
/* → Nur Elemente mit class="wichtig" werden rot und fett */
```

> **Merke:** Klassen können bei **mehreren** Elementen verwendet werden.

### ID-Selektor (`#`)

Wählt **ein einziges** Element mit einer bestimmten ID aus:

```html
<h1 id="seitentitel">Meine Website</h1>
```

```css
#seitentitel {
    color: darkblue;
    border-bottom: 2px solid gray;
}
```

> **Merke:** Eine ID darf pro Seite nur **einmal** vorkommen!

### Übersicht der Selektoren

| Selektor | Syntax | Wählt aus | Beispiel |
|----------|--------|-----------|---------|
| Element | `element` | Alle Elemente dieses Typs | `p { }` |
| Klasse | `.klassenname` | Alle mit dieser Klasse | `.wichtig { }` |
| ID | `#id` | Genau ein Element | `#titel { }` |
| Universal | `*` | Alle Elemente | `* { }` |
| Nachfahre | `a b` | b innerhalb von a | `nav a { }` |
| Gruppe | `a, b` | a und b | `h1, h2 { }` |

### Kombinierte Selektoren

```css
/* Alle Links innerhalb von nav */
nav a {
    text-decoration: none;
    color: white;
}

/* Alle h1 UND h2 */
h1, h2 {
    font-family: Arial, sans-serif;
}

/* Nur p-Elemente mit der Klasse "intro" */
p.intro {
    font-size: 1.2em;
}
```

---

## 5. Wichtige CSS-Eigenschaften

### Farben

```css
/* Benannte Farben */
color: red;
color: blue;
color: darkgreen;

/* Hex-Farben (#RRGGBB) */
color: #ff0000;    /* Rot */
color: #00ff00;    /* Grün */
color: #0000ff;    /* Blau */
color: #333333;    /* Dunkelgrau */

/* RGB-Farben */
color: rgb(255, 0, 0);      /* Rot */
color: rgb(100, 150, 200);  /* Hellblau */

/* RGBA (mit Transparenz) */
color: rgba(0, 0, 0, 0.5);  /* 50% transparentes Schwarz */
```

### Schriften (Typografie)

```css
body {
    font-family: Arial, Helvetica, sans-serif;  /* Schriftart */
    font-size: 16px;          /* Schriftgröße */
    font-weight: bold;        /* Schriftstärke: normal, bold */
    font-style: italic;       /* Schriftstil: normal, italic */
    line-height: 1.5;         /* Zeilenhöhe */
    text-align: center;       /* Ausrichtung: left, center, right, justify */
    text-decoration: none;    /* Unterstreichung entfernen */
    text-transform: uppercase; /* Großbuchstaben */
}
```

### Hintergrund

```css
body {
    background-color: #f5f5f5;
    background-image: url("hintergrund.jpg");
    background-size: cover;
    background-repeat: no-repeat;
}
```

---

## 6. Das Box-Modell

**Jedes HTML-Element ist eine Box.** Das Box-Modell beschreibt, wie viel Platz ein Element einnimmt:

```
┌─────────────────────────────────────────┐
│                 MARGIN                   │  ← Außenabstand
│  ┌───────────────────────────────────┐  │
│  │             BORDER                │  │  ← Rahmen
│  │  ┌─────────────────────────────┐  │  │
│  │  │          PADDING            │  │  │  ← Innenabstand
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │       CONTENT         │  │  │  │  ← Inhalt
│  │  │  │   (Text, Bilder...)   │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### CSS-Eigenschaften für das Box-Modell

```css
.box {
    /* Innenabstand (zwischen Inhalt und Rahmen) */
    padding: 20px;              /* Alle Seiten gleich */
    padding: 10px 20px;         /* Oben/Unten  Links/Rechts */
    padding: 10px 20px 15px 5px; /* Oben Rechts Unten Links */
    
    /* Rahmen */
    border: 2px solid black;    /* Dicke  Stil  Farbe */
    border-radius: 10px;        /* Abgerundete Ecken */
    
    /* Außenabstand (zwischen Element und Nachbarn) */
    margin: 20px;               /* Alle Seiten gleich */
    margin: 0 auto;             /* Oben/Unten 0, Links/Rechts automatisch (zentriert!) */
    
    /* Breite und Höhe */
    width: 300px;
    height: 200px;
    max-width: 100%;            /* Nie breiter als das Elternelement */
}
```

### Rahmenstile

```css
border: 1px solid black;    /* Durchgezogen ──── */
border: 2px dashed red;     /* Gestrichelt - - - */
border: 3px dotted blue;    /* Gepunktet · · · · */
border: none;               /* Kein Rahmen */
```

---

## 🔨 Erarbeitungsaufgabe: Steckbrief gestalten

Nimm deinen Steckbrief aus DS 06 (oder erstelle einen neuen) und gestalte ihn mit CSS.

### Minimalanforderungen

Im **CSS-Feld** von CodePen:

```css
/* 1. Grundgestaltung für die ganze Seite */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
    max-width: 700px;
    margin: 0 auto;
    padding: 20px;
}

/* 2. Überschrift gestalten (Element-Selektor) */
h1 {
    color: /* wähle eine Farbe */;
    text-align: center;
    border-bottom: 2px solid /* Farbe */;
    padding-bottom: 10px;
}

/* 3. Klasse für hervorgehobene Absätze */
.highlight {
    background-color: /* helle Farbe */;
    padding: 15px;
    border-left: 4px solid /* Farbe */;
    border-radius: 5px;
}

/* 4. Bilder gestalten */
img {
    max-width: 100%;
    border-radius: 10px;
    border: 1px solid #ddd;
}
```

Im **HTML-Feld** die Klasse verwenden:
```html
<p class="highlight">Dieser Absatz wird besonders hervorgehoben!</p>
```

### Erweiterte Anforderungen

- Verwende mindestens **3 verschiedene Selektoren** (Element, Klasse, ID)
- Setze **Farben** mit Hex-Werten oder RGB ein
- Nutze **Padding** und **Margin** für Abstände
- Füge mindestens einen **Rahmen** hinzu
- Experimentiere mit **border-radius** für runde Ecken

---

## 📝 Übungsaufgaben

### Aufgabe 1: Selektoren zuordnen
Welcher Selektor wählt welche Elemente aus?

HTML:
```html
<h1 id="titel">Willkommen</h1>
<p class="intro">Einleitung</p>
<p>Normaler Text</p>
<p class="intro">Noch eine Einleitung</p>
<footer>Fußzeile</footer>
```

| CSS-Regel | Betroffen? |
|-----------|-----------|
| `p { color: gray; }` | ? |
| `.intro { font-size: 18px; }` | ? |
| `#titel { color: blue; }` | ? |
| `p.intro { font-weight: bold; }` | ? |

<details>
<summary>Lösung anzeigen</summary>

| CSS-Regel | Betroffen |
|-----------|-----------|
| `p { }` | Alle 3 `<p>`-Elemente |
| `.intro { }` | Beide `<p class="intro">` |
| `#titel { }` | Nur der `<h1 id="titel">` |
| `p.intro { }` | Beide `<p class="intro">` (p-Elemente mit Klasse intro) |
</details>

### Aufgabe 2: Box-Modell berechnen
Ein Element hat folgende CSS-Eigenschaften:
```css
.box {
    width: 200px;
    padding: 20px;
    border: 5px solid black;
    margin: 10px;
}
```

Berechne:
1. Die Gesamtbreite des sichtbaren Elements (Content + Padding + Border)
2. Den Gesamtplatzbedarf (inkl. Margin)

<details>
<summary>Lösung anzeigen</summary>

1. Sichtbare Breite: 200px (Content) + 2×20px (Padding) + 2×5px (Border) = **250px**
2. Gesamtplatz: 250px + 2×10px (Margin) = **270px**

> **Tipp:** `box-sizing: border-box;` lässt Width Padding und Border einschließen!
</details>

### Aufgabe 3: Farbmischer (Python-Bezug)
Schreibe ein Python-Programm, das eine RGB-Farbe als Hex-Code ausgibt:

```python
r = int(input("Rot (0-255): "))
g = int(input("Grün (0-255): "))
b = int(input("Blau (0-255): "))
# Tipp: f"#{r:02x}{g:02x}{b:02x}"
```

<details>
<summary>Lösung anzeigen</summary>

```python
r = int(input("Rot (0-255): "))
g = int(input("Grün (0-255): "))
b = int(input("Blau (0-255): "))

hex_farbe = f"#{r:02x}{g:02x}{b:02x}"
print(f"RGB({r}, {g}, {b}) = {hex_farbe}")
print(f"Verwende in CSS: color: {hex_farbe};")
```
</details>

### Aufgabe 4: Dark Mode
Erstelle zwei Versionen deines Steckbriefs:
1. **Light Mode:** Heller Hintergrund, dunkler Text
2. **Dark Mode:** Dunkler Hintergrund (`#1a1a2e`), heller Text (`#e0e0e0`), Akzentfarbe (`#00d2ff`)

> **Tipp:** Du brauchst nur die CSS-Farben zu ändern – das HTML bleibt gleich. Das zeigt die Trennung von Inhalt und Design!

---

## 🔗 Weiterführende Links

- [MDN – CSS Grundlagen](https://developer.mozilla.org/de/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [MDN – CSS-Referenz](https://developer.mozilla.org/de/docs/Web/CSS/Reference)
- [CSS-Tricks – Box-Modell](https://css-tricks.com/the-css-box-model/)
- [Coolors – Farbpaletten-Generator](https://coolors.co/)
- [Google Fonts](https://fonts.google.com/) – Kostenlose Webfonts

---

[← Zurück: DS 09](04-Hyperlinks.md) · [Weiter → DS 11: CSS-Layout mit Grid](06-CSS-Layout-Grid.md)
