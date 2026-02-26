# DS 12 – Formulare und JavaScript-Grundlagen

> **Themenfeld E.2 – HTML-Dokumente** · Doppelstunde 12 (7 von 8)

---

## Lernziele dieser Stunde

- Du kannst HTML-Formulare mit verschiedenen Eingabeelementen erstellen.
- Du kennst die wichtigsten `<input>`-Typen.
- Du verstehst, wie Formulardaten an einen Server gesendet werden.
- Du kannst einfaches JavaScript nutzen, um Formulardaten zu verarbeiten.
- Du verstehst die Verbindung zwischen Formularen und der Client-Server-Architektur.

---

## 1. HTML-Formulare

Formulare ermöglichen es Benutzern, **Daten einzugeben und an einen Server zu senden** – z. B. Anmeldedaten, Suchbegriffe, Bestellungen, Kontaktanfragen.

### Das `<form>`-Element

```html
<form action="verarbeitung.php" method="POST">
    <!-- Hier kommen die Eingabefelder -->
</form>
```

| Attribut | Bedeutung |
|----------|-----------|
| `action` | URL, an die die Daten gesendet werden |
| `method` | HTTP-Methode: `GET` oder `POST` |

### GET vs. POST

| Eigenschaft | GET | POST |
|-------------|-----|------|
| Daten sichtbar in | URL (`?name=wert&...`) | HTTP-Body (nicht sichtbar) |
| Datenmenge | Begrenzt (~2000 Zeichen) | Praktisch unbegrenzt |
| Verwendung | Suchformulare, Filter | Login, Registrierung, Daten senden |
| Lesezeichen-fähig | Ja | Nein |
| Sicherheit | Weniger sicher (Daten in URL) | Sicherer (Daten nicht in URL) |

> **Verbindung zu E.1:** Das `method`-Attribut bestimmt die HTTP-Methode, die wir in DS 05 kennengelernt haben. Bei `GET` werden die Daten an die URL angehängt, bei `POST` im Body der HTTP-Anfrage gesendet.

---

## 2. Eingabeelemente

### Textfeld `<input type="text">`

```html
<label for="name">Name:</label>
<input type="text" id="name" name="name" placeholder="Dein Name">
```

> **Das `<label>`-Element** beschriftet ein Eingabefeld. Das `for`-Attribut verknüpft es mit dem `id` des Eingabefelds.

### Wichtige Input-Typen

```html
<!-- Textfeld -->
<input type="text" name="vorname" placeholder="Vorname">

<!-- Passwort (Zeichen werden verdeckt) -->
<input type="password" name="passwort" placeholder="Passwort">

<!-- E-Mail (Browser prüft Format) -->
<input type="email" name="email" placeholder="deine@email.de">

<!-- Zahl -->
<input type="number" name="alter" min="0" max="120">

<!-- Bereich (Schieberegler) -->
<input type="range" name="lautstaerke" min="0" max="100">

<!-- Datum -->
<input type="date" name="geburtsdatum">

<!-- Farbe -->
<input type="color" name="lieblingsfarbe">

<!-- Checkbox (Mehrfachauswahl) -->
<input type="checkbox" name="agb" id="agb">
<label for="agb">Ich akzeptiere die AGB</label>

<!-- Radio-Buttons (Einfachauswahl) -->
<input type="radio" name="geschlecht" value="m" id="m">
<label for="m">Männlich</label>
<input type="radio" name="geschlecht" value="w" id="w">
<label for="w">Weiblich</label>
<input type="radio" name="geschlecht" value="d" id="d">
<label for="d">Divers</label>

<!-- Datei-Upload -->
<input type="file" name="foto">

<!-- Verstecktes Feld (nicht sichtbar) -->
<input type="hidden" name="formular_id" value="12345">
```

### Mehrzeiliges Textfeld `<textarea>`

```html
<label for="nachricht">Nachricht:</label>
<textarea id="nachricht" name="nachricht" rows="5" cols="40" 
          placeholder="Deine Nachricht..."></textarea>
```

### Auswahlmenü `<select>`

```html
<label for="land">Land:</label>
<select id="land" name="land">
    <option value="">– Bitte wählen –</option>
    <option value="de">Deutschland</option>
    <option value="at">Österreich</option>
    <option value="ch">Schweiz</option>
</select>
```

### Absende-Button

```html
<!-- Variante 1: input -->
<input type="submit" value="Absenden">

<!-- Variante 2: button (flexibler) -->
<button type="submit">Absenden</button>

<!-- Reset-Button (Formular leeren) -->
<button type="reset">Zurücksetzen</button>
```

---

## 3. Ein vollständiges Formular

### HTML

```html
<form id="kontaktformular">
    <h2>Kontaktformular</h2>
    
    <div class="form-group">
        <label for="name">Name: *</label>
        <input type="text" id="name" name="name" required>
    </div>
    
    <div class="form-group">
        <label for="email">E-Mail: *</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <div class="form-group">
        <label for="betreff">Betreff:</label>
        <select id="betreff" name="betreff">
            <option value="anfrage">Allgemeine Anfrage</option>
            <option value="feedback">Feedback</option>
            <option value="fehler">Fehlermeldung</option>
        </select>
    </div>
    
    <div class="form-group">
        <label for="nachricht">Nachricht: *</label>
        <textarea id="nachricht" name="nachricht" rows="5" required></textarea>
    </div>
    
    <div class="form-group">
        <input type="checkbox" id="datenschutz" name="datenschutz" required>
        <label for="datenschutz">Ich habe die Datenschutzerklärung gelesen *</label>
    </div>
    
    <button type="submit">Absenden</button>
    <button type="reset">Zurücksetzen</button>
</form>
```

### CSS für das Formular

```css
form {
    max-width: 500px;
    margin: 20px auto;
    font-family: Arial, sans-serif;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"],
input[type="email"],
select,
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
    box-sizing: border-box;
}

input:focus,
textarea:focus,
select:focus {
    border-color: #2c3e50;
    outline: none;
    box-shadow: 0 0 3px rgba(44, 62, 80, 0.3);
}

button {
    padding: 10px 20px;
    font-size: 14px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-right: 10px;
}

button[type="submit"] {
    background: #2c3e50;
    color: white;
}

button[type="submit"]:hover {
    background: #34495e;
}

button[type="reset"] {
    background: #e0e0e0;
}
```

### Validierung mit HTML5

HTML5 bietet eingebaute Formularvalidierung:

```html
<!-- Pflichtfeld -->
<input type="text" required>

<!-- Mindestlänge -->
<input type="password" minlength="8">

<!-- Muster (Regex) -->
<input type="text" pattern="[A-Za-z]{3,}" title="Mindestens 3 Buchstaben">

<!-- Zahlenbereich -->
<input type="number" min="1" max="100">
```

---

## 4. JavaScript-Grundlagen für Formulare

JavaScript ermöglicht es, Formulardaten **im Browser** zu verarbeiten (auf der Client-Seite), bevor sie an einen Server gesendet werden.

### JavaScript einbinden

In CodePen einfach ins **JS-Feld** schreiben. In einer echten HTML-Datei:

```html
<script>
    // JavaScript-Code hier
</script>
```

### Zugriff auf Formularfelder

```javascript
// Element mit der ID "name" holen
let namefeld = document.getElementById("name");

// Wert auslesen
let wert = namefeld.value;

// Wert setzen
namefeld.value = "Neuer Text";
```

### Auf Formular-Absendung reagieren

```javascript
// Das Formular abfangen und verarbeiten
document.getElementById("kontaktformular").addEventListener("submit", function(event) {
    event.preventDefault();  // Verhindert das Absenden an einen Server
    
    // Werte auslesen
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let nachricht = document.getElementById("nachricht").value;
    
    // Ausgabe
    alert("Danke, " + name + "!\nDeine Nachricht wurde empfangen.");
    
    // Oder: In der Seite anzeigen
    document.getElementById("ausgabe").innerHTML = 
        "<h3>Empfangene Daten:</h3>" +
        "<p><strong>Name:</strong> " + name + "</p>" +
        "<p><strong>E-Mail:</strong> " + email + "</p>" +
        "<p><strong>Nachricht:</strong> " + nachricht + "</p>";
});
```

> **Python-Vergleich:**
> - `document.getElementById("name")` ≈ eine Variable `name` aus einer Eingabe holen
> - `alert("Hallo")` ≈ `print("Hallo")`
> - `event.preventDefault()` ≈ verhindert die Standardaktion (wie `return` in einer Funktion)

### JavaScript-Variablen und Grundlagen

```javascript
// Variablen
let name = "Max";           // Veränderbare Variable
const pi = 3.14159;         // Konstante (unveränderlich)

// Ausgabe
console.log("Hallo Welt");  // In die Entwicklerkonsole (F12)
alert("Hallo Welt");        // Popup-Fenster

// Bedingung
if (name === "") {
    alert("Bitte einen Namen eingeben!");
} else {
    alert("Hallo, " + name + "!");
}

// HTML-Element ändern
document.getElementById("ausgabe").textContent = "Neuer Text";
document.getElementById("ausgabe").style.color = "red";
```

---

## 5. Verbindung zu E.1: Was passiert beim Absenden?

Wenn ein Formular an einen Server gesendet wird, läuft folgender Prozess ab:

```
Benutzer                Browser               Webserver
   │                       │                      │
   │-- Klickt "Absenden" ->│                      │
   │                       │                      │
   │                       │-- POST /kontakt.php ->│
   │                       │   name=Max&           │
   │                       │   email=max@test.de&  │
   │                       │   nachricht=Hallo     │
   │                       │                      │
   │                       │<-- HTTP 200 OK -------│
   │                       │   "Danke für deine    │
   │                       │    Nachricht!"        │
   │                       │                      │
   │<-- Zeigt Antwort -----│                      │
```

> Das ist genau die **Client-Server-Architektur** mit **HTTP POST** aus Themenfeld E.1!

---

## 🔨 Erarbeitungsaufgabe: Interaktives Formular

Erstelle in CodePen ein **Anmeldeformular für eine Schulveranstaltung** mit JavaScript-Verarbeitung.

### Anforderungen

**HTML:**
1. Name (Pflichtfeld)
2. E-Mail (Pflichtfeld, Typ email)
3. Klasse (Select mit Optionen: 10a, 10b, 11a, 11b, 12a, 12b)
4. Veranstaltung (Radio-Buttons: Sportfest, Konzert, Filmabend)
5. Vegetarisches Essen? (Checkbox)
6. Anmerkungen (Textarea, optional)
7. Absende- und Zurücksetzen-Button

**CSS:**
- Ansprechendes Formular-Design (nutze das Beispiel-CSS als Vorlage)

**JavaScript:**
- Beim Absenden: Formulardaten auslesen und auf der Seite anzeigen
- Zusätzlich: Prüfe per JavaScript, ob alle Pflichtfelder ausgefüllt sind

### Starthilfe für JavaScript

```javascript
document.getElementById("anmeldeformular").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let name = document.getElementById("name").value;
    // ... weitere Felder auslesen
    
    // Radio-Button auslesen:
    let veranstaltung = document.querySelector('input[name="veranstaltung"]:checked');
    if (veranstaltung) {
        veranstaltung = veranstaltung.value;
    }
    
    // Checkbox auslesen:
    let vegetarisch = document.getElementById("vegetarisch").checked;  // true oder false
    
    // Anzeigen
    let ausgabe = document.getElementById("ausgabe");
    ausgabe.innerHTML = "<h3>Anmeldung erfolgreich!</h3>";
    ausgabe.innerHTML += "<p>Name: " + name + "</p>";
    // ... weitere Felder anzeigen
});
```

---

## 📝 Übungsaufgaben

### Aufgabe 1: Input-Typen
Erstelle ein Formular, das **alle** der folgenden Input-Typen demonstriert:
`text`, `password`, `email`, `number`, `date`, `color`, `range`, `checkbox`, `radio`, `file`

Für jeden Typ: Beschrifte das Feld mit einem `<label>`.

### Aufgabe 2: BMI-Rechner
Erstelle einen **BMI-Rechner** mit:
- Eingabefeld für Gewicht (kg)
- Eingabefeld für Größe (cm)
- Button „Berechnen"
- JavaScript berechnet den BMI: `Gewicht / (Größe in m)²`
- Ergebnis wird auf der Seite angezeigt

```javascript
// Starthilfe:
let gewicht = parseFloat(document.getElementById("gewicht").value);
let groesse = parseFloat(document.getElementById("groesse").value) / 100;
let bmi = gewicht / (groesse * groesse);
```

<details>
<summary>Lösung anzeigen</summary>

**HTML:**
```html
<h2>BMI-Rechner</h2>
<div class="form-group">
    <label for="gewicht">Gewicht (kg):</label>
    <input type="number" id="gewicht" min="1" step="0.1">
</div>
<div class="form-group">
    <label for="groesse">Größe (cm):</label>
    <input type="number" id="groesse" min="1">
</div>
<button onclick="berechne()">Berechnen</button>
<div id="ergebnis"></div>
```

**JavaScript:**
```javascript
function berechne() {
    let gewicht = parseFloat(document.getElementById("gewicht").value);
    let groesse = parseFloat(document.getElementById("groesse").value) / 100;
    
    if (isNaN(gewicht) || isNaN(groesse) || groesse === 0) {
        document.getElementById("ergebnis").textContent = "Bitte gültige Werte eingeben!";
        return;
    }
    
    let bmi = gewicht / (groesse * groesse);
    let kategorie = "";
    if (bmi < 18.5) kategorie = "Untergewicht";
    else if (bmi < 25) kategorie = "Normalgewicht";
    else if (bmi < 30) kategorie = "Übergewicht";
    else kategorie = "Adipositas";
    
    document.getElementById("ergebnis").innerHTML = 
        "<p>Dein BMI: <strong>" + bmi.toFixed(1) + "</strong> (" + kategorie + ")</p>";
}
```
</details>

### Aufgabe 3: Python-Vergleich
Vergleiche die BMI-Berechnung in JavaScript und Python:

| Aufgabe | Python | JavaScript |
|---------|--------|------------|
| Eingabe | `input()` | `document.getElementById().value` |
| Ausgabe | `print()` | `document.getElementById().textContent` |
| Umwandlung | `float()` | `parseFloat()` |
| Runden | `round(x, 1)` | `x.toFixed(1)` |

### Aufgabe 4: Quiz-Formular (⭐ Herausforderung)
Erstelle ein **Quiz** über Netzwerke (Themen aus E.1) mit:
- 5 Multiple-Choice-Fragen (Radio-Buttons)
- Einem Auswerte-Button
- JavaScript, das die Antworten prüft und die Punktzahl anzeigt
- Falsche Antworten werden rot markiert, richtige grün

---

## 🔗 Weiterführende Links

- [MDN – Formulare](https://developer.mozilla.org/de/docs/Learn/Forms)
- [MDN – JavaScript Grundlagen](https://developer.mozilla.org/de/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [selfhtml – Formulare](https://wiki.selfhtml.org/wiki/HTML/Tutorials/Formulare)

---

[← Zurück: DS 11](06-CSS-Layout-Grid.md) · [Weiter → DS 13: Abschlussprojekt](08-Abschlussprojekt.md)
