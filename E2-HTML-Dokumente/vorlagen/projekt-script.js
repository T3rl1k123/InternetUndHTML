/* ============================================
   PROJEKTVORLAGE – JavaScript
   Interaktivität für das Kontaktformular
   und optionale Erweiterungen
   ============================================ */

// === Formular-Verarbeitung ===
document.getElementById("kontaktformular").addEventListener("submit", function(event) {
    // Standardverhalten verhindern (kein Seitenneuladen)
    event.preventDefault();

    // Eingabewerte auslesen
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let betreff = document.getElementById("betreff").value;
    let nachricht = document.getElementById("nachricht").value;

    // Ausgabe-Element finden und sichtbar machen
    let ausgabe = document.getElementById("form-ausgabe");
    ausgabe.style.display = "block";

    // Ausgabetext erstellen
    ausgabe.innerHTML = 
        "<h3>✅ Nachricht gesendet (simuliert)</h3>" +
        "<p><strong>Von:</strong> " + name + " (" + email + ")</p>" +
        "<p><strong>Betreff:</strong> " + betreff + "</p>" +
        "<p><strong>Nachricht:</strong> " + nachricht + "</p>" +
        "<p><small>Hinweis: In CodePen wird das Formular nicht wirklich " +
        "gesendet. In einer echten Website würde hier eine " +
        "Server-Verarbeitung stattfinden.</small></p>";

    // Zum Ausgabebereich scrollen
    ausgabe.scrollIntoView({ behavior: "smooth" });
});


// === OPTIONAL: Smooth Scrolling für Navigation ===
// (Lass diesen Abschnitt so oder lösche ihn, wenn nicht benötigt)
document.querySelectorAll('.main-nav a').forEach(function(link) {
    link.addEventListener("click", function(event) {
        let href = this.getAttribute("href");
        
        // Nur für Ankerlinks (#...)
        if (href.startsWith("#")) {
            event.preventDefault();
            let target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        }
    });
});


// === OPTIONAL: Aktiven Navigationslink hervorheben ===
// (Erkennt beim Scrollen, welcher Abschnitt sichtbar ist)
window.addEventListener("scroll", function() {
    let sections = document.querySelectorAll(".page-section");
    let navLinks = document.querySelectorAll(".main-nav a");
    
    let current = "";
    sections.forEach(function(section) {
        let top = section.offsetTop - 100;
        if (window.scrollY >= top) {
            current = "#" + section.getAttribute("id");
        }
    });
    
    navLinks.forEach(function(link) {
        link.classList.remove("active");
        if (link.getAttribute("href") === current) {
            link.classList.add("active");
        }
    });
});
