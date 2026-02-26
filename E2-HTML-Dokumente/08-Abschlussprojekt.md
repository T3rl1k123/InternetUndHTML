# DS 13 – Abschlussprojekt: Eigene mehrseitige Website

> **Themenfeld E.2 – HTML-Dokumente** · Doppelstunde 13 (8 von 8)

---

## Projektbeschreibung

In dieser Doppelstunde (und ggf. als Hausarbeit) erstellt ihr eine **eigene mehrseitige Website** zu einem Thema eurer Wahl. Dabei wendet ihr alle Kenntnisse aus E.2 an.

---

## Themenwahl

Wähle ein Thema, das dich interessiert. Hier einige Vorschläge:

- **Persönliches Portfolio** – Steckbrief, Hobbys, Projekte
- **Informatik-Lexikon** – Begriffe aus E.1 und E.2 erklärt
- **Fan-Seite** – Für ein Spiel, eine Serie, einen Sport, eine Band
- **Reise-Guide** – Für eine Stadt oder ein Land
- **Schulprojekt** – Dokumentation eines Schulprojekts
- **Kochbuch** – Rezeptsammlung mit Bildern
- **Netzwerk-Guide** – Alles über Rechnernetze (Bezug zu E.1!)

---

## Anforderungen

### Pflichtanforderungen (mindestens)

| Kriterium | Beschreibung | Bezug |
|-----------|-------------|-------|
| **Mindestens 3 Seiten/Abschnitte** | z. B. Startseite, Info, Kontakt | DS 09 |
| **HTML-Grundgerüst** | Korrektes `<!DOCTYPE html>`, `<head>`, `<body>` | DS 06 |
| **Verschiedene HTML-Elemente** | `<h1>`–`<h3>`, `<p>`, Listen, Bilder, Tabelle | DS 07 |
| **Semantische Struktur** | `<header>`, `<nav>`, `<main>`, `<footer>`, `<section>` | DS 08 |
| **Navigation** | Links zwischen allen Seiten/Abschnitten | DS 09 |
| **Externes CSS** | Separates Stylesheet (in CodePen: CSS-Feld) | DS 10 |
| **CSS-Selektoren** | Mindestens Element-, Klassen- und ID-Selektor | DS 10 |
| **Grid-Layout** | Mindestens ein Layout mit CSS Grid | DS 11 |
| **Formular** | Mindestens ein Formular mit 3+ Eingabefeldern | DS 12 |

### Optionale Erweiterungen (⭐ für Zusatzpunkte)

| Erweiterung | Beschreibung |
|-------------|-------------|
| ⭐ JavaScript-Interaktion | Formular wird mit JS ausgewertet |
| ⭐ Responsive Design | Grid passt sich an Bildschirmgröße an (`auto-fit`/`minmax`) |
| ⭐ Externe Links | Sinnvolle Links zu weiterführenden Quellen |
| ⭐ Bilder sinnvoll eingesetzt | Bilder mit `alt`-Text, passend zum Inhalt |
| ⭐ Karten-Layout | Grid-basiertes Card-Layout |
| ⭐ Besonderes CSS | Hover-Effekte, Animationen, Schatten |
| ⭐ Bezug zu E.1 | Inhalte zu Netzwerken/Protokollen |

---

## Bewertungskriterien

| Bereich | Kriterien | Punkte |
|---------|-----------|--------|
| **HTML-Struktur** | Korrektes Grundgerüst, sinnvolle Verschachtelung, semantische Elemente | /10 |
| **HTML-Inhalt** | Vielfältige Elemente, sinnvoller Inhalt, Bilder, Tabellen, Listen | /10 |
| **CSS-Gestaltung** | Selektoren korrekt verwendet, ansprechendes Design, Box-Modell | /10 |
| **Grid-Layout** | Sinnvolles Layout, korrekt umgesetzt | /10 |
| **Formular** | Verschiedene Input-Typen, Labels, Validierung | /10 |
| **Navigation/Links** | Funktionierende Links, Navigation auf allen Seiten | /5 |
| **Gesamteindruck** | Originalität, Sorgfalt, Vollständigkeit | /5 |
| **Bonuspunkte** | Optionale Erweiterungen | bis +10 |
| **Gesamt** | | / 60 (+10) |

---

## Projektvorlage

Du kannst die folgende Vorlage als Startpunkt verwenden. Die Vorlage ist auch als Dateien im Ordner [`vorlagen/`](vorlagen/) verfügbar.

### HTML-Vorlage

```html
<!-- === Kopfbereich === -->
<header class="site-header">
    <h1>Mein Projekt</h1>
    <p class="subtitle">Ein Untertitel für mein Projekt</p>
</header>

<!-- === Navigation === -->
<nav class="main-nav">
    <a href="#home">Home</a>
    <a href="#info">Informationen</a>
    <a href="#galerie">Galerie</a>
    <a href="#kontakt">Kontakt</a>
</nav>

<!-- === Hauptinhalt === -->
<main>
    <!-- Seite 1: Home -->
    <section id="home" class="page-section">
        <h2>Willkommen!</h2>
        <p>Hier kommt eine Einleitung zu deinem Thema.</p>
        
        <!-- Karten-Grid -->
        <div class="card-grid">
            <div class="card">
                <h3>Thema 1</h3>
                <p>Beschreibung...</p>
            </div>
            <div class="card">
                <h3>Thema 2</h3>
                <p>Beschreibung...</p>
            </div>
            <div class="card">
                <h3>Thema 3</h3>
                <p>Beschreibung...</p>
            </div>
        </div>
    </section>

    <!-- Seite 2: Informationen -->
    <section id="info" class="page-section">
        <h2>Informationen</h2>
        <div class="content-grid">
            <div class="content-main">
                <p>Hier kommt der Haupttext hin...</p>
                
                <h3>Daten und Fakten</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Eigenschaft</th>
                            <th>Wert</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Eigenschaft 1</td>
                            <td>Wert 1</td>
                        </tr>
                        <tr>
                            <td>Eigenschaft 2</td>
                            <td>Wert 2</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <aside class="content-sidebar">
                <h3>Wusstest du?</h3>
                <ul>
                    <li>Fakt 1</li>
                    <li>Fakt 2</li>
                    <li>Fakt 3</li>
                </ul>
            </aside>
        </div>
    </section>

    <!-- Seite 3: Galerie -->
    <section id="galerie" class="page-section">
        <h2>Galerie</h2>
        <div class="gallery-grid">
            <figure>
                <img src="https://via.placeholder.com/400x300" alt="Bild 1">
                <figcaption>Bild 1</figcaption>
            </figure>
            <figure>
                <img src="https://via.placeholder.com/400x300" alt="Bild 2">
                <figcaption>Bild 2</figcaption>
            </figure>
            <figure>
                <img src="https://via.placeholder.com/400x300" alt="Bild 3">
                <figcaption>Bild 3</figcaption>
            </figure>
        </div>
    </section>

    <!-- Seite 4: Kontakt -->
    <section id="kontakt" class="page-section">
        <h2>Kontakt</h2>
        <form id="kontaktformular">
            <div class="form-group">
                <label for="name">Name: *</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">E-Mail: *</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="nachricht">Nachricht:</label>
                <textarea id="nachricht" name="nachricht" rows="5"></textarea>
            </div>
            <button type="submit">Absenden</button>
        </form>
        <div id="form-ausgabe"></div>
    </section>
</main>

<!-- === Fußbereich === -->
<footer class="site-footer">
    <p>&copy; 2026 – Erstellt im Informatik-Unterricht</p>
</footer>
```

### CSS-Vorlage

```css
/* === Reset und Grundlagen === */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background: #f5f5f5;
}

/* === Header === */
.site-header {
    background: #2c3e50;
    color: white;
    text-align: center;
    padding: 40px 20px;
}

.site-header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 1.2em;
    opacity: 0.8;
}

/* === Navigation === */
.main-nav {
    background: #34495e;
    padding: 15px 20px;
    display: flex;
    justify-content: center;
    gap: 20px;
    position: sticky;
    top: 0;
    z-index: 100;
}

.main-nav a {
    color: white;
    text-decoration: none;
    padding: 5px 15px;
    border-radius: 4px;
    transition: background 0.3s;
}

.main-nav a:hover {
    background: rgba(255,255,255,0.2);
}

/* === Abschnitte === */
.page-section {
    max-width: 1000px;
    margin: 30px auto;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.page-section h2 {
    color: #2c3e50;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #3498db;
}

/* === Karten-Grid === */
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.card {
    background: #ecf0f1;
    padding: 20px;
    border-radius: 8px;
    border-left: 4px solid #3498db;
}

.card h3 {
    color: #2c3e50;
    margin-bottom: 10px;
}

/* === Content-Grid (Text + Sidebar) === */
.content-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 30px;
    margin-top: 20px;
}

.content-sidebar {
    background: #ecf0f1;
    padding: 20px;
    border-radius: 8px;
}

/* === Tabelle === */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
}

th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background: #2c3e50;
    color: white;
}

tr:hover {
    background: #f5f5f5;
}

/* === Galerie-Grid === */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 15px;
    margin-top: 20px;
}

.gallery-grid img {
    width: 100%;
    border-radius: 8px;
}

.gallery-grid figcaption {
    text-align: center;
    padding: 8px;
    font-size: 0.9em;
    color: #666;
}

/* === Formular === */
.form-group {
    margin-bottom: 15px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

.form-group input,
.form-group textarea,
.form-group select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
}

button[type="submit"] {
    background: #2c3e50;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
}

button[type="submit"]:hover {
    background: #3498db;
}

#form-ausgabe {
    margin-top: 20px;
    padding: 15px;
    background: #d4edda;
    border-radius: 4px;
    display: none;
}

/* === Footer === */
.site-footer {
    background: #2c3e50;
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 30px;
}
```

### JavaScript-Vorlage

```javascript
// Formular-Verarbeitung
document.getElementById("kontaktformular").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let nachricht = document.getElementById("nachricht").value;
    
    let ausgabe = document.getElementById("form-ausgabe");
    ausgabe.style.display = "block";
    ausgabe.innerHTML = "<strong>Danke, " + name + "!</strong><br>" +
                        "Deine Nachricht wurde (simuliert) gesendet.<br>" +
                        "<small>E-Mail: " + email + "</small>";
});
```

---

## Arbeitsschritte

### 1. Planung (10 Minuten)
- Thema festlegen
- Seitenstruktur skizzieren (auf Papier oder digital)
- Welche Inhalte sollen auf welche Seite?

### 2. HTML-Struktur (20 Minuten)
- Grundgerüst erstellen oder Vorlage anpassen
- Alle Inhalte einfügen (erstmal ohne Gestaltung)
- Semantische Elemente verwenden

### 3. CSS-Gestaltung (30 Minuten)
- Grid-Layout einrichten
- Farben, Schriften, Abstände festlegen
- Navigation gestalten

### 4. Feinschliff (20 Minuten)
- Formular erstellen und gestalten
- Optional: JavaScript-Interaktion
- Testen: Alle Links funktionieren? Layout OK?

### 5. Abgabe
- CodePen-Link teilen oder HTML/CSS-Dateien abgeben

---

## Tipps

- **Starte einfach:** Erstmal die Struktur, dann die Gestaltung
- **Nutze die Vorlage:** Du musst nicht bei Null anfangen
- **Teste regelmäßig:** Speichere oft und überprüfe das Ergebnis
- **Nutze die Referenzen:** [MDN Web Docs](https://developer.mozilla.org/de/) ist dein bester Freund
- **Frage nach:** Bei Problemen die vorherigen DS-Materialien konsultieren oder nachfragen

---

## 📋 Checkliste vor der Abgabe

- [ ] HTML-Grundgerüst vorhanden und korrekt
- [ ] Mindestens 3 Seiten/Abschnitte mit Inhalt
- [ ] Semantische Elemente verwendet (header, nav, main, footer, section)
- [ ] Navigation funktioniert korrekt
- [ ] CSS in separatem Stylesheet (CSS-Feld in CodePen)
- [ ] Mindestens Element-, Klassen- und ID-Selektor verwendet
- [ ] Grid-Layout für mindestens ein Element
- [ ] Formular mit mindestens 3 verschiedenen Eingabefeldern
- [ ] Bilder mit alt-Text
- [ ] Tabelle mit Kopfzeile
- [ ] Geordnete und ungeordnete Liste vorhanden
- [ ] Keine HTML-Verschachtelungsfehler
- [ ] Alle Links funktionieren

---

## 📋 Gesamtzusammenfassung E.2 – HTML-Dokumente

| Thema | Kernbegriffe |
|-------|-------------|
| **HTML-Grundgerüst** | `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`, Tags, Attribute |
| **HTML-Elemente** | `<h1>`–`<h6>`, `<p>`, `<ul>`, `<ol>`, `<img>`, `<table>` |
| **Dokumentstruktur** | DOM, Dokumentbaum, Eltern/Kind, Block/Inline |
| **Semantische Elemente** | `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` |
| **Hyperlinks** | `<a href="">`, absolut/relativ, Ankerlinks, Navigation |
| **CSS-Grundlagen** | Selektoren, Eigenschaften, Box-Modell, Farben, Schriften |
| **CSS Grid** | Grid-Container, Spalten/Zeilen, `fr`, `gap`, `repeat()` |
| **Formulare** | `<form>`, `<input>`, `<textarea>`, `<select>`, GET/POST |
| **JavaScript** | `document.getElementById()`, Events, DOM-Manipulation |

---

[← Zurück: DS 12](07-Formulare-und-JavaScript.md) · [🏠 Zur Übersicht](../README.md)
