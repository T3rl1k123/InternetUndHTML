# DS 11 – CSS-Layout mit Grid

> **Themenfeld E.2 – HTML-Dokumente** · Doppelstunde 11 (6 von 8)

---

## Lernziele dieser Stunde

- Du kannst CSS Grid verwenden, um Seitenlayouts zu erstellen.
- Du verstehst die Begriffe Grid-Container, Grid-Items, Zeilen und Spalten.
- Du kannst `grid-template-columns` und `grid-template-rows` einsetzen.
- Du kannst mit `gap` Abstände zwischen Grid-Zellen erstellen.
- Du kannst einfache responsive Layouts mit Grid erstellen.

---

## 1. Warum brauchen wir ein Layout-System?

Bisher haben wir einzelne Elemente gestaltet. Aber wie ordnet man Elemente **nebeneinander** an? Zum Beispiel:

```
┌────────────────────────────────────────┐
│              Header                     │
├──────────────────────┬─────────────────┤
│                      │                 │
│     Hauptinhalt      │   Seitenleiste  │
│                      │                 │
├──────────────────────┴─────────────────┤
│              Footer                     │
└────────────────────────────────────────┘
```

Dafür gibt es **CSS Grid** – ein mächtiges Layout-System.

---

## 2. CSS Grid – Grundkonzept

CSS Grid teilt einen Container in ein **Raster** aus Zeilen und Spalten:

```css
.container {
    display: grid;                          /* Grid aktivieren */
    grid-template-columns: 200px 200px 200px;  /* 3 Spalten à 200px */
    grid-template-rows: 100px 100px;           /* 2 Zeilen à 100px */
    gap: 10px;                              /* Abstand zwischen Zellen */
}
```

```
┌──────────┬──────────┬──────────┐
│  Item 1  │  Item 2  │  Item 3  │  ← Zeile 1 (100px)
├──────────┼──────────┼──────────┤
│  Item 4  │  Item 5  │  Item 6  │  ← Zeile 2 (100px)
└──────────┴──────────┴──────────┘
   200px      200px      200px
```

### Begriffe

| Begriff | Erklärung |
|---------|-----------|
| **Grid-Container** | Das Elternelement mit `display: grid` |
| **Grid-Items** | Die direkten Kindelemente des Containers |
| **Grid-Zeile (Row)** | Eine horizontale Reihe |
| **Grid-Spalte (Column)** | Eine vertikale Spalte |
| **Grid-Zelle (Cell)** | Ein einzelnes Feld (Kreuzung aus Zeile und Spalte) |
| **Gap** | Abstand zwischen den Zellen |

---

## 3. Spalten definieren mit `grid-template-columns`

### Feste Breiten

```css
.container {
    display: grid;
    grid-template-columns: 200px 300px 200px;  /* 3 Spalten mit festen Breiten */
}
```

### Flexible Breiten mit `fr` (Fraction)

Die Einheit `fr` verteilt den **verfügbaren Platz** proportional:

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;   /* 3 gleich breite Spalten */
}
```

```css
.container {
    display: grid;
    grid-template-columns: 2fr 1fr;   /* Erste Spalte doppelt so breit */
}
```

```
┌──────────────────┬─────────┐
│      2fr         │   1fr   │
│   (⅔ der Breite) │ (⅓)    │
└──────────────────┴─────────┘
```

### Mischung aus fest und flexibel

```css
.container {
    display: grid;
    grid-template-columns: 250px 1fr;   /* Seitenleiste fest, Hauptinhalt flexibel */
}
```

### `repeat()` – Wiederholungen

```css
/* Statt: grid-template-columns: 1fr 1fr 1fr 1fr; */
grid-template-columns: repeat(4, 1fr);   /* 4 gleiche Spalten */

/* 3 Spalten à 200px */
grid-template-columns: repeat(3, 200px);
```

---

## 4. Zeilen definieren mit `grid-template-rows`

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 80px auto 60px;   /* Header fest, Inhalt flexibel, Footer fest */
}
```

> `auto` = Die Zeile passt sich an den Inhalt an.

---

## 5. Abstände mit `gap`

```css
.container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;               /* Gleicher Abstand überall */
    /* oder: */
    row-gap: 20px;           /* Nur zwischen Zeilen */
    column-gap: 10px;        /* Nur zwischen Spalten */
}
```

---

## 6. Grid-Items positionieren

### Automatische Platzierung

Standardmäßig werden Grid-Items einfach der Reihe nach in die Zellen gesetzt.

### Gezielte Platzierung mit `grid-column` und `grid-row`

Du kannst ein Item über **mehrere Zellen** strecken:

```css
.header {
    grid-column: 1 / 3;   /* Von Spalte 1 bis Spalte 3 (= 2 Spalten breit) */
}

.sidebar {
    grid-row: 2 / 4;      /* Von Zeile 2 bis Zeile 4 (= 2 Zeilen hoch) */
}
```

### Kurzschreibweise: `span`

```css
.header {
    grid-column: span 3;   /* 3 Spalten breit */
}
```

---

## 7. Komplett-Beispiel: Seitenlayout

### HTML

```html
<div class="page">
    <header class="header">
        <h1>Meine Website</h1>
    </header>
    
    <nav class="nav">
        <a href="#">Home</a>
        <a href="#">Über mich</a>
        <a href="#">Projekte</a>
        <a href="#">Kontakt</a>
    </nav>
    
    <main class="main">
        <h2>Willkommen!</h2>
        <p>Das ist der Hauptinhalt der Seite.</p>
        <p>Hier steht der wichtigste Text.</p>
    </main>
    
    <aside class="sidebar">
        <h3>Sidebar</h3>
        <p>Zusätzliche Informationen</p>
    </aside>
    
    <footer class="footer">
        <p>&copy; 2026 Meine Website</p>
    </footer>
</div>
```

### CSS

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;    /* Padding und Border werden in die Breite eingerechnet */
}

body {
    font-family: Arial, sans-serif;
}

.page {
    display: grid;
    grid-template-columns: 1fr 250px;
    grid-template-rows: auto auto 1fr auto;
    min-height: 100vh;         /* 100vh = 100% der Fensterhöhe */
    gap: 0;
}

.header {
    grid-column: 1 / -1;          /* Ganze Breite */
    background: #2c3e50;
    color: white;
    padding: 20px;
    text-align: center;
}

.nav {
    grid-column: 1 / -1;          /* Ganze Breite */
    background: #34495e;
    padding: 10px 20px;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
    gap: 10px;
    text-align: center;
}

.nav a {
    color: white;
    text-decoration: none;
}

.nav a:hover {
    text-decoration: underline;
}

.main {
    padding: 20px;
}

.sidebar {
    background: #ecf0f1;
    padding: 20px;
}

.footer {
    grid-column: 1 / -1;          /* Ganze Breite */
    background: #2c3e50;
    color: white;
    padding: 15px;
    text-align: center;
}
```

### Ergebnis

```
┌────────────────────────────────────────┐
│              HEADER                     │  ← grid-column: 1 / -1
├────────────────────────────────────────┤
│  Home | Über mich | Projekte | Kontakt │  ← grid-column: 1 / -1
├──────────────────────┬─────────────────┤
│                      │                 │
│     MAIN (1fr)       │ SIDEBAR (250px) │
│                      │                 │
├──────────────────────┴─────────────────┤
│              FOOTER                     │  ← grid-column: 1 / -1
└────────────────────────────────────────┘
```

> **`grid-column: 1 / -1`** bedeutet: von der ersten bis zur letzten Spalte.

---

## 8. Karten-Layout (Cards)

Ein häufiges Muster – z. B. für Portfolios, Produktlisten, Bildergalerien:

### HTML

```html
<div class="cards">
    <div class="card">
        <h3>Projekt 1</h3>
        <p>Beschreibung des ersten Projekts.</p>
    </div>
    <div class="card">
        <h3>Projekt 2</h3>
        <p>Beschreibung des zweiten Projekts.</p>
    </div>
    <div class="card">
        <h3>Projekt 3</h3>
        <p>Beschreibung des dritten Projekts.</p>
    </div>
    <div class="card">
        <h3>Projekt 4</h3>
        <p>Beschreibung des vierten Projekts.</p>
    </div>
</div>
```

### CSS

```css
.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);   /* 3 Spalten */
    gap: 20px;
    padding: 20px;
}

.card {
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.card:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    background: #f0f0f0;
}
```

---

## 9. Responsives Design (Ausblick)

Mit `auto-fit` und `minmax()` passt sich das Grid automatisch an die Bildschirmgröße an:

```css
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```

- Auf einem großen Bildschirm: 3-4 Karten nebeneinander
- Auf einem Tablet: 2 Karten nebeneinander
- Auf einem Smartphone: 1 Karte pro Zeile

> **`minmax(250px, 1fr)`** = Jede Spalte ist mindestens 250px breit, darf aber wachsen.

---

## 🔨 Erarbeitungsaufgabe: Seitenlayout erstellen

Erstelle in CodePen ein vollständiges Seitenlayout mit CSS Grid:

### Anforderungen

1. Ein **Grid-Layout** mit:
   - Header (volle Breite)
   - Navigation (volle Breite)
   - Hauptbereich + Seitenleiste nebeneinander
   - Footer (volle Breite)

2. **Styling:**
   - Header und Footer mit Hintergrundfarbe
   - Navigation mit horizontalen Links
   - Seitenleiste visuell abgesetzt (andere Hintergrundfarbe)

3. Verwende das Komplett-Beispiel als Startpunkt und passe es nach deinem Geschmack an:
   - Eigene Farben
   - Eigene Inhalte
   - Optional: Karten-Layout im Hauptbereich

---

## 📝 Übungsaufgaben

### Aufgabe 1: Grid-Spalten
Was ergibt jeder der folgenden Grid-Werte? Zeichne das Ergebnis.

```css
/* a) */ grid-template-columns: 100px 200px 100px;
/* b) */ grid-template-columns: 1fr 1fr;
/* c) */ grid-template-columns: 2fr 1fr 1fr;
/* d) */ grid-template-columns: 300px 1fr;
/* e) */ grid-template-columns: repeat(4, 1fr);
```

<details>
<summary>Lösung anzeigen</summary>

a) 3 Spalten: 100px, 200px, 100px (fest)
b) 2 gleich breite Spalten (je 50%)
c) 3 Spalten: erste = 50%, zweite = 25%, dritte = 25%
d) 2 Spalten: Erste fest 300px, zweite füllt den Rest
e) 4 gleich breite Spalten (je 25%)
</details>

### Aufgabe 2: Bilderalbum
Erstelle ein Bilderalbum mit CSS Grid:
- 3 Spalten auf dem Desktop
- Verwende Placeholder-Bilder: `<img src="https://via.placeholder.com/300x200">`
- Abstände zwischen den Bildern: 10px
- Bilder sollen die volle Spaltenbreite ausfüllen (`width: 100%`)

### Aufgabe 3: Dashboard
Erstelle ein „Dashboard"-Layout:

```
┌────────────────────────────────────────┐
│              Überschrift                │
├────────┬────────┬────────┬────────────┤
│ Info 1 │ Info 2 │ Info 3 │   Info 4   │
├────────┴────────┴────────┴────────────┤
│           Hauptdiagramm                │
├───────────────────────┬────────────────┤
│     Tabelle           │   Details      │
└───────────────────────┴────────────────┘
```

### Aufgabe 4: Responsive Karten
Erstelle 6 Karten mit `auto-fit` und `minmax()`, die sich automatisch anpassen:
- Bei voller Breite: 3 Karten pro Zeile
- Bei schmalerem Fenster: 2 Karten
- Bei noch schmalerem Fenster: 1 Karte

Teste es, indem du das Browserfenster schmaler ziehst!

---

## 🔗 Weiterführende Links

- [MDN – CSS Grid Layout](https://developer.mozilla.org/de/docs/Web/CSS/CSS_grid_layout)
- [CSS-Tricks – A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Grid Garden – Lernspiel für CSS Grid](https://cssgridgarden.com/#de)
- [Grid by Example](https://gridbyexample.com/)

---

[← Zurück: DS 10](05-CSS-Grundlagen.md) · [Weiter → DS 12: Formulare und JavaScript](07-Formulare-und-JavaScript.md)
