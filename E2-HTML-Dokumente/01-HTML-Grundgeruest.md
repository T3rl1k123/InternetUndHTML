# DS 06 – HTML-Grundgerüst und erste Schritte

> **Themenfeld E.2 – HTML-Dokumente** · Doppelstunde 6 (1 von 8)

---

## Lernziele dieser Stunde

- Du weißt, was HTML ist und wozu es dient.
- Du kannst das HTML-Grundgerüst auswendig aufschreiben.
- Du verstehst den Unterschied zwischen öffnenden und schließenden Tags.
- Du kannst Attribute und Attributwerte verwenden.
- Du kannst eine erste einfache Webseite in CodePen erstellen.

---

## 1. Was ist HTML?

**HTML** steht für **H**yper**T**ext **M**arkup **L**anguage – auf Deutsch: Hypertext-Auszeichnungssprache.

- HTML ist **keine Programmiersprache**, sondern eine **Auszeichnungssprache**
- HTML beschreibt die **Struktur** und den **Inhalt** einer Webseite
- Der Browser **interpretiert** den HTML-Code und zeigt die Webseite an
- HTML wurde von **Tim Berners-Lee** 1991 erfunden
- Die aktuelle Version ist **HTML5**

### HTML vs. Programmiersprache

| HTML | Python |
|------|--------|
| Beschreibt Struktur | Steuert Ablauf |
| Keine Schleifen/Bedingungen | Schleifen, Bedingungen, Funktionen |
| Wird vom Browser angezeigt | Wird vom Interpreter ausgeführt |
| Tags: `<h1>Hallo</h1>` | Code: `print("Hallo")` |

---

## 2. Tags – Die Bausteine von HTML

HTML besteht aus **Tags** (Auszeichnungen), die den Inhalt strukturieren.

### Aufbau eines Tags

```html
<tagname>Inhalt</tagname>
  ↑                 ↑
  öffnendes Tag     schließendes Tag (mit /)
```

### Beispiele

```html
<h1>Das ist eine Überschrift</h1>
<p>Das ist ein Absatz.</p>
<strong>Das ist fett gedruckt.</strong>
```

### Selbstschließende Tags

Manche Tags haben keinen Inhalt und brauchen kein schließendes Tag:

```html
<br>          <!-- Zeilenumbruch -->
<hr>          <!-- Horizontale Linie -->
<img src="bild.jpg">  <!-- Bild -->
```

---

## 3. Attribute

Tags können **Attribute** haben, die zusätzliche Informationen enthalten:

```html
<tagname attribut="wert">Inhalt</tagname>
```

### Beispiele

```html
<a href="https://www.google.de">Link zu Google</a>
   ↑      ↑
   Attribut  Attributwert

<img src="foto.jpg" alt="Ein Foto" width="300">
     ↑               ↑              ↑
     Quelle           Alternativtext  Breite
```

### Regeln für Attribute

- Attribute stehen immer im **öffnenden Tag**
- Der Attributwert steht in **Anführungszeichen** (doppelt `"` oder einfach `'`)
- Ein Tag kann **mehrere Attribute** haben
- Die Reihenfolge der Attribute ist egal

---

## 4. Das HTML-Grundgerüst

Jede HTML-Seite hat das gleiche Grundgerüst:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine erste Webseite</title>
</head>
<body>
    <h1>Hallo Welt!</h1>
    <p>Das ist meine erste Webseite.</p>
</body>
</html>
```

### Erklärung der Bestandteile

| Zeile | Bedeutung |
|-------|-----------|
| `<!DOCTYPE html>` | Sagt dem Browser: „Das ist ein HTML5-Dokument" |
| `<html lang="de">` | Wurzelelement, umschließt alles. `lang="de"` = Sprache Deutsch |
| `<head>` | **Kopfbereich** – Metadaten, nicht sichtbar auf der Seite |
| `<meta charset="UTF-8">` | Zeichenkodierung (für Umlaute ä, ö, ü) |
| `<meta name="viewport" ...>` | Für mobile Geräte optimieren |
| `<title>` | Titel der Seite (im Browser-Tab sichtbar) |
| `<body>` | **Körper** – Alles was auf der Seite sichtbar ist |
| `<h1>` | Überschrift 1. Ordnung (die größte) |
| `<p>` | Absatz (paragraph) |

### Merkregel: head vs. body

```
<head> = Das Gehirn  → Metadaten, Infos FÜR den Browser
<body> = Der Körper  → Inhalt, der AUF der Seite angezeigt wird
```

---

## 5. Erste Schritte in CodePen

### CodePen öffnen

1. Gehe zu [https://codepen.io/pen/](https://codepen.io/pen/)
2. Du siehst drei Editorbereiche: **HTML**, **CSS**, **JS**

> **Wichtig:** In CodePen gibst du im HTML-Feld nur den Inhalt ein, der normalerweise im `<body>` steht. Das Grundgerüst (`<!DOCTYPE>`, `<html>`, `<head>`, ...) ergänzt CodePen automatisch.

### Dein erstes HTML in CodePen

Gib im **HTML-Feld** ein:

```html
<h1>Hallo Welt!</h1>
<p>Das ist meine erste Webseite in CodePen.</p>
<p>HTML ist <strong>super einfach</strong> zu lernen!</p>
```

Du solltest sofort in der Vorschau sehen:
- Eine große Überschrift „Hallo Welt!"
- Zwei Absätze, wobei „super einfach" fett gedruckt ist

---

## 6. Kommentare

Du kannst Kommentare in deinen HTML-Code schreiben. Sie werden **nicht** auf der Seite angezeigt, helfen aber beim Verstehen des Codes:

```html
<!-- Das ist ein Kommentar -->
<h1>Sichtbare Überschrift</h1>
<!-- TODO: Hier kommt noch mehr Inhalt hin -->
```

> **Vergleich mit Python:** In Python beginnen Kommentare mit `#`, in HTML stehen sie zwischen `<!--` und `-->`.

---

## 🔨 Erarbeitungsaufgabe: Steckbrief-Seite

Erstelle in CodePen einen persönlichen **Steckbrief** mit folgenden Elementen:

1. Eine Überschrift mit deinem Namen (`<h1>`)
2. Eine kleinere Überschrift „Über mich" (`<h2>`)
3. Einen Absatz mit 2-3 Sätzen über dich (`<p>`)
4. Eine Überschrift „Meine Hobbys" (`<h2>`)
5. Einen Absatz, in dem dein Lieblingshobby **fett** (`<strong>`) hervorgehoben ist
6. Eine horizontale Linie (`<hr>`)
7. Einen Absatz mit dem aktuellen Datum

### Beispiel-Ergebnis

```html
<h1>Max Mustermann</h1>
<h2>Über mich</h2>
<p>Ich bin 16 Jahre alt und gehe in die 11. Klasse. 
Ich interessiere mich für Informatik und Musik.</p>
<h2>Meine Hobbys</h2>
<p>Mein Lieblingshobby ist <strong>Programmieren</strong>. 
Außerdem spiele ich gerne Gitarre.</p>
<hr>
<p>Stand: Februar 2026</p>
```

---

## 📝 Übungsaufgaben

### Aufgabe 1: Fehler finden
Finde und korrigiere die Fehler in folgendem HTML-Code:

```html
<h1>Willkommen auf meiner Seite<h1>
<p>Das ist ein Absatz<p/>
<strong>Dieser Text ist fett.
<h3>Eine Überschrift</h2>
```

<details>
<summary>Lösung anzeigen</summary>

```html
<h1>Willkommen auf meiner Seite</h1>       <!-- Schließendes Tag fehlte / -->
<p>Das ist ein Absatz</p>                   <!-- Schließendes Tag war falsch -->
<strong>Dieser Text ist fett.</strong>      <!-- Schließendes Tag fehlte -->
<h3>Eine Überschrift</h3>                   <!-- h2 statt h3 als schließendes Tag -->
```
</details>

### Aufgabe 2: Grundgerüst aus dem Kopf
Schreibe das HTML-Grundgerüst auswendig auf (auf Papier oder in einem Editor), ohne die Vorlage anzuschauen. Prüfe danach.

### Aufgabe 3: Tags und Attribute
Erkläre den Unterschied:
1. Was ist ein Tag?
2. Was ist ein Attribut?
3. Was ist ein Attributwert?

Nenne zu jedem ein Beispiel.

<details>
<summary>Lösung anzeigen</summary>

1. **Tag:** Ein HTML-Baustein, der Inhalt strukturiert, z. B. `<p>` (Absatz)
2. **Attribut:** Eine zusätzliche Eigenschaft eines Tags, z. B. `href` (bei Links)
3. **Attributwert:** Der Wert des Attributs, z. B. `"https://www.google.de"` (die URL)

Beispiel: `<a href="https://www.google.de">` – Tag: `a`, Attribut: `href`, Wert: `https://www.google.de`
</details>

### Aufgabe 4: Experimentieren
Probiere in CodePen aus:
1. Was passiert, wenn du `<h1>` bis `<h6>` ausprobierst? Wie unterscheiden sich die Überschriften?
2. Was passiert, wenn du mehrere Leerzeilen in einem `<p>`-Element schreibst?
3. Was passiert, wenn du das schließende `</p>`-Tag weglässt?

---

## 🔗 Weiterführende Links

- [MDN – HTML Grundlagen](https://developer.mozilla.org/de/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [selfhtml – HTML-Element-Referenz](https://wiki.selfhtml.org/wiki/HTML/Elemente)
- [CodePen](https://codepen.io/pen/) – Online-Editor

---

[← Zurück: E.1](../E1-Internetprotokolle/05-Client-Server-und-Sicherheit.md) · [Weiter → DS 07: HTML-Elemente](02-HTML-Elemente.md)
