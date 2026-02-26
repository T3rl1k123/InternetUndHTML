# DS 07 – HTML-Elemente: Texte, Listen, Bilder, Tabellen

> **Themenfeld E.2 – HTML-Dokumente** · Doppelstunde 7 (2 von 8)

---

## Lernziele dieser Stunde

- Du kannst verschiedene HTML-Elemente für Texte verwenden.
- Du kannst geordnete und ungeordnete Listen erstellen.
- Du kannst Bilder in eine Webseite einbinden.
- Du kannst einfache Tabellen erstellen.
- Du weißt, wann welches Element sinnvoll ist.

---

## 1. Textformatierung

### Überschriften (h1 – h6)

HTML bietet 6 Ebenen von Überschriften. `<h1>` ist die wichtigste, `<h6>` die kleinste:

```html
<h1>Überschrift 1 – Die Hauptüberschrift</h1>
<h2>Überschrift 2 – Unterüberschrift</h2>
<h3>Überschrift 3</h3>
<h4>Überschrift 4</h4>
<h5>Überschrift 5</h5>
<h6>Überschrift 6</h6>
```

> **Regel:** Verwende Überschriften hierarchisch! Nach `<h1>` kommt `<h2>`, nicht `<h4>`. Es sollte nur ein `<h1>` pro Seite geben.

### Absätze und Zeilenumbrüche

```html
<p>Das ist ein Absatz. Der Browser fügt automatisch 
Abstand zum nächsten Absatz ein.</p>

<p>Das ist ein zweiter Absatz.</p>

<p>Hier steht Text<br>und hier geht es in der nächsten Zeile weiter.</p>
```

> **Wichtig:** HTML ignoriert zusätzliche Leerzeichen und Zeilenumbrüche im Quellcode. Für einen Zeilenumbruch brauchst du `<br>`.

### Textauszeichnungen

| Element | Bedeutung | Darstellung |
|---------|-----------|-------------|
| `<strong>` | Wichtig (stark betont) | **fett** |
| `<em>` | Betont | *kursiv* |
| `<mark>` | Hervorgehoben | ==markiert== |
| `<small>` | Kleingedrucktes | klein |
| `<del>` | Gelöscht | ~~durchgestrichen~~ |
| `<ins>` | Eingefügt | unterstrichen |
| `<code>` | Code | `Monospace-Schrift` |
| `<sup>` | Hochgestellt | E = mc² |
| `<sub>` | Tiefgestellt | H₂O |

```html
<p>Das ist <strong>wichtig</strong> und das ist <em>betont</em>.</p>
<p>Wasser hat die chemische Formel H<sub>2</sub>O.</p>
<p>Die Fläche beträgt 25 m<sup>2</sup>.</p>
<p>In Python schreibt man <code>print("Hallo")</code>.</p>
```

---

## 2. Listen

### Ungeordnete Liste (Aufzählung mit Punkten)

```html
<ul>
    <li>Erster Punkt</li>
    <li>Zweiter Punkt</li>
    <li>Dritter Punkt</li>
</ul>
```

Ergebnis:
- Erster Punkt
- Zweiter Punkt
- Dritter Punkt

### Geordnete Liste (Nummerierung)

```html
<ol>
    <li>Schritt eins</li>
    <li>Schritt zwei</li>
    <li>Schritt drei</li>
</ol>
```

Ergebnis:
1. Schritt eins
2. Schritt zwei
3. Schritt drei

### Verschachtelte Listen

Listen können ineinander verschachtelt werden:

```html
<ul>
    <li>Obst
        <ul>
            <li>Äpfel</li>
            <li>Bananen</li>
        </ul>
    </li>
    <li>Gemüse
        <ul>
            <li>Karotten</li>
            <li>Brokkoli</li>
        </ul>
    </li>
</ul>
```

### Definitionsliste

Für Begriffe mit Erklärungen:

```html
<dl>
    <dt>HTML</dt>
    <dd>Hypertext Markup Language – Auszeichnungssprache für Webseiten</dd>
    
    <dt>CSS</dt>
    <dd>Cascading Style Sheets – Gestaltungssprache für Webseiten</dd>
</dl>
```

---

## 3. Bilder

Bilder werden mit dem `<img>`-Tag eingebunden. Dieses Tag ist **selbstschließend** (kein `</img>` nötig).

```html
<img src="foto.jpg" alt="Beschreibung des Bildes" width="400">
```

### Wichtige Attribute

| Attribut | Bedeutung | Pflicht? |
|----------|-----------|---------|
| `src` | Quelle/Pfad zum Bild | ✅ ja |
| `alt` | Alternativtext (wird angezeigt, wenn Bild nicht lädt) | ✅ ja |
| `width` | Breite in Pixel | optional |
| `height` | Höhe in Pixel | optional |

### Bildquellen

In CodePen kannst du Bilder von externen URLs einbinden:

```html
<!-- Bild von einer URL -->
<img src="https://via.placeholder.com/400x200" alt="Platzhalterbild" width="400">

<!-- Bild von Unsplash (lizenzfreie Fotos) -->
<img src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=400" 
     alt="Laptop mit Code" width="400">
```

> **Tipp:** Für Übungen kannst du Platzhalterbilder verwenden: `https://via.placeholder.com/BreitexHöhe`

### Bild mit Beschriftung

```html
<figure>
    <img src="https://via.placeholder.com/400x200" alt="Beispielbild">
    <figcaption>Abb. 1: Ein Beispielbild mit Beschriftung</figcaption>
</figure>
```

---

## 4. Tabellen

Tabellen eignen sich für **tabellarische Daten** (nicht für Layouts!).

```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Alter</th>
            <th>Stadt</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Anna</td>
            <td>16</td>
            <td>Frankfurt</td>
        </tr>
        <tr>
            <td>Ben</td>
            <td>17</td>
            <td>Kassel</td>
        </tr>
        <tr>
            <td>Clara</td>
            <td>16</td>
            <td>Darmstadt</td>
        </tr>
    </tbody>
</table>
```

### Tabellenelemente

| Element | Bedeutung |
|---------|-----------|
| `<table>` | Die gesamte Tabelle |
| `<thead>` | Tabellenkopf |
| `<tbody>` | Tabellenkörper |
| `<tr>` | Tabellenzeile (table row) |
| `<th>` | Kopfzelle (table header) – fett und zentriert |
| `<td>` | Datenzelle (table data) |

### Merkregel

```
table  → Die Tabelle selbst
  thead → Kopfbereich
    tr  → Eine Zeile
      th → Eine Kopf-Zelle
  tbody → Datenbereich
    tr  → Eine Zeile
      td → Eine Daten-Zelle
```

---

## 5. Sonderzeichen und Entities

Manche Zeichen haben in HTML eine besondere Bedeutung. Um sie als Text darzustellen, verwendet man **HTML-Entities**:

| Zeichen | Entity | Bedeutung |
|---------|--------|-----------|
| `<` | `&lt;` | Kleiner als (less than) |
| `>` | `&gt;` | Größer als (greater than) |
| `&` | `&amp;` | Und-Zeichen (ampersand) |
| `"` | `&quot;` | Anführungszeichen |
| ` ` | `&nbsp;` | Geschütztes Leerzeichen |
| `©` | `&copy;` | Copyright |
| `€` | `&euro;` | Euro-Zeichen |

```html
<p>In HTML schreibt man Tags mit &lt;tagname&gt;.</p>
<p>Preis: 19,99 &euro;</p>
<p>&copy; 2026 Meine Schule</p>
```

---

## 🔨 Erarbeitungsaufgabe: Informationsseite erstellen

Erstelle in CodePen eine Informationsseite über ein Thema deiner Wahl (z. B. dein Lieblingsspiel, eine Sportart, ein Land, ein Tier, …). Die Seite muss enthalten:

1. **Mindestens 2 Überschriftsebenen** (`<h1>`, `<h2>`)
2. **Mindestens 3 Absätze** mit Text (`<p>`)
3. **Textauszeichnungen**: mindestens 2 verschiedene (z. B. `<strong>`, `<em>`)
4. **Eine ungeordnete Liste** (z. B. Eigenschaften, Fakten)
5. **Eine geordnete Liste** (z. B. Top-5, Anleitung)
6. **Ein Bild** (von einer URL, z. B. Placeholder oder Unsplash)
7. **Eine Tabelle** mit mindestens 3 Zeilen und 3 Spalten

> **Beispielthema:** Eine Seite über Python-Programmierung mit einer Tabelle der Datentypen, einer Liste der wichtigsten Befehle und einem Screenshot.

---

## 📝 Übungsaufgaben

### Aufgabe 1: Stundenplan
Erstelle deinen Stundenplan als HTML-Tabelle:
- Spalten: Montag bis Freitag
- Zeilen: 1. bis 6. Stunde
- Verwende `<th>` für die Kopfzeile (Wochentage) und die erste Spalte (Stundennumern)

### Aufgabe 2: Rezept
Erstelle eine Webseite für ein Kochrezept (oder Backrezept):
- Überschrift mit dem Namen des Gerichts
- Eine Zutatenliste (ungeordnete Liste)
- Die Zubereitungsschritte (geordnete Liste)
- Ein Bild des Gerichts (Placeholder-URL ist OK)
- Nährwertinformationen als Tabelle

### Aufgabe 3: Code-Quiz
Was zeigt der Browser an? Überlege zuerst, dann probiere es in CodePen aus:

```html
<p>Zeile 1

Zeile 2


Zeile 3</p>
```

<details>
<summary>Lösung anzeigen</summary>

Der Browser zeigt alles **in einer Zeile** an: „Zeile 1 Zeile 2 Zeile 3"

HTML ignoriert zusätzliche Leerzeichen und Zeilenumbrüche. Für echte Zeilenumbrüche brauchst du `<br>` oder separate `<p>`-Elemente.
</details>

### Aufgabe 4: Python-Vergleich
Erstelle eine HTML-Tabelle, die Python-Konzepte ihren HTML-Entsprechungen gegenüberstellt:

| Python | HTML |
|--------|------|
| `print("text")` | `<p>text</p>` |
| `# Kommentar` | `<!-- Kommentar -->` |
| `liste = [1,2,3]` | `<ul><li>1</li>...</ul>` |

---

## 🔗 Weiterführende Links

- [MDN – HTML-Elemente Referenz](https://developer.mozilla.org/de/docs/Web/HTML/Element)
- [selfhtml – Textstrukturierung](https://wiki.selfhtml.org/wiki/HTML/Textstrukturierung)
- [Unsplash – Lizenzfreie Fotos](https://unsplash.com/)

---

[← Zurück: DS 06](01-HTML-Grundgeruest.md) · [Weiter → DS 08: Dokumentstruktur](03-Dokumentstruktur.md)
