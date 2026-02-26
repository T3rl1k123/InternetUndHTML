# DS 02 – IP-Adressen und Routing

> **Themenfeld E.1 – Internetprotokolle** · Doppelstunde 2 von 5

---

## Lernziele dieser Stunde

- Du kannst den Aufbau einer IPv4-Adresse erklären.
- Du verstehst die Bedeutung der Subnetzmaske.
- Du kannst den Netzwerk- und Hostanteil einer IP-Adresse bestimmen.
- Du verstehst, wie ein Router verschiedene Netzwerke verbindet.
- Du kannst in Filius ein Netzwerk mit Router aufbauen.

---

## 1. IPv4-Adressen

Jedes Gerät in einem Netzwerk braucht eine eindeutige **IP-Adresse** (Internet Protocol Address), damit es Daten senden und empfangen kann – vergleichbar mit einer Postanschrift.

### Aufbau einer IPv4-Adresse

Eine IPv4-Adresse besteht aus **4 Bytes** (= 32 Bit), geschrieben als vier Zahlen, getrennt durch Punkte:

```
192.168.1.10
```

Jede Zahl liegt im Bereich **0 – 255** (da ein Byte 8 Bit hat: 2⁸ = 256 mögliche Werte).

### Binärdarstellung

Computer arbeiten intern mit Binärzahlen. Die IP-Adresse `192.168.1.10` sieht binär so aus:

```
192     . 168     . 1       . 10
11000000. 10101000. 00000001. 00001010
```

> **Python-Tipp:** Du kannst IP-Adressen in Python umrechnen:
> ```python
> # Dezimal → Binär
> ip = "192.168.1.10"
> for teil in ip.split("."):
>     print(f"{int(teil):>3} = {int(teil):08b}")
> ```

---

## 2. Subnetzmaske

Die **Subnetzmaske** bestimmt, welcher Teil der IP-Adresse das **Netzwerk** identifiziert und welcher Teil den **Host** (das einzelne Gerät).

### Beispiel: Subnetzmaske `255.255.255.0`

```
IP-Adresse:    192.168.  1. 10
Subnetzmaske:  255.255.255.  0
               ─────────────  ──
               Netzwerkanteil  Hostanteil
```

- **Netzwerkanteil** (`192.168.1`): Identifiziert das Netzwerk
- **Hostanteil** (`.10`): Identifiziert das Gerät im Netzwerk

### Regel: Wer ist im selben Netzwerk?

Zwei Geräte sind im **selben Netzwerk**, wenn ihr **Netzwerkanteil** übereinstimmt.

| Gerät | IP-Adresse | Netzwerkanteil | Selbes Netz? |
|-------|-----------|----------------|-------------|
| PC1 | 192.168.1.10 | 192.168.1 | ✅ |
| PC2 | 192.168.1.20 | 192.168.1 | ✅ |
| PC3 | 192.168.**2**.10 | 192.168.**2** | ❌ Anderes Netz! |

### Gängige Subnetzmasken

| Subnetzmaske | Kurzschreibweise | Netzwerkanteil | Max. Hosts |
|-------------|-----------------|----------------|-----------|
| `255.0.0.0` | /8 | 1. Byte | 16.777.214 |
| `255.255.0.0` | /16 | 2 Bytes | 65.534 |
| `255.255.255.0` | /24 | 3 Bytes | 254 |

> Die Kurzschreibweise `/24` bedeutet: Die ersten 24 Bit der Adresse sind der Netzwerkanteil.

### Besondere IP-Adressen

| Adresse | Bedeutung |
|---------|-----------|
| `x.x.x.0` | Netzwerkadresse (z. B. `192.168.1.0`) |
| `x.x.x.255` | Broadcast-Adresse (Nachricht an alle im Netz) |
| `127.0.0.1` | Localhost (der eigene Rechner) |
| `0.0.0.0` | „Alle Netzwerke" / nicht konfiguriert |

---

## 3. Routing – Netzwerke verbinden

Wenn zwei Geräte in **verschiedenen** Netzwerken sind, brauchen sie einen **Router**, der die Datenpakete zwischen den Netzen weiterleitet.

### Wie funktioniert Routing?

```
Netzwerk A (192.168.1.0/24)          Netzwerk B (192.168.2.0/24)
                                   
  PC1 ──┐                               ┌── PC3
        Switch ── Router ── Switch ──┤
  PC2 ──┘                               └── PC4
```

1. PC1 (`192.168.1.1`) will eine Nachricht an PC3 (`192.168.2.1`) senden
2. PC1 erkennt: PC3 ist **nicht** im eigenen Netzwerk
3. PC1 schickt das Paket an den **Standard-Gateway** (= den Router)
4. Der Router kennt beide Netzwerke und leitet das Paket an PC3 weiter

### Standard-Gateway

Jeder PC muss wissen, wohin er Pakete schicken soll, die **nicht** für das eigene Netzwerk bestimmt sind. Diese Adresse heißt **Standard-Gateway** – das ist die IP-Adresse des Routers im eigenen Netz.

```
PC1-Konfiguration:
  IP-Adresse:      192.168.1.1
  Subnetzmaske:    255.255.255.0
  Standard-Gateway: 192.168.1.254    ← Adresse des Routers in Netz A
```

### Der Router hat mehrere IP-Adressen

Ein Router hat für **jedes angeschlossene Netzwerk** eine eigene IP-Adresse (eine pro Schnittstelle):

```
Router:
  Schnittstelle 1: 192.168.1.254  (im Netzwerk A)
  Schnittstelle 2: 192.168.2.254  (im Netzwerk B)
```

---

## 🔨 Erarbeitungsaufgabe: Zwei Netzwerke mit Router verbinden

> Siehe auch: [Filius-Anleitung: Routing](filius-anleitungen/02-routing.md)

### Aufbau

Erstelle in Filius folgendes Netzwerk:

```
Netzwerk A: 192.168.1.0/24        Netzwerk B: 192.168.2.0/24

  PC-A1 (192.168.1.1) ───┐          ┌─── PC-B1 (192.168.2.1)
                        Switch-A ── Router ── Switch-B
  PC-A2 (192.168.1.2) ───┘          └─── PC-B2 (192.168.2.2)
```

### Schritt-für-Schritt

1. **Platziere 2 Switches** und **4 PCs** (je 2 pro Switch)

2. **Platziere einen Router** zwischen den Switches und verbinde ihn mit beiden Switches

3. **Konfiguriere den Router** (Doppelklick):
   - Schnittstelle 1: IP `192.168.1.254`, Maske `255.255.255.0`
   - Schnittstelle 2: IP `192.168.2.254`, Maske `255.255.255.0`

4. **Konfiguriere die PCs in Netz A:**
   - PC-A1: IP `192.168.1.1`, Maske `255.255.255.0`, Gateway `192.168.1.254`
   - PC-A2: IP `192.168.1.2`, Maske `255.255.255.0`, Gateway `192.168.1.254`

5. **Konfiguriere die PCs in Netz B:**
   - PC-B1: IP `192.168.2.1`, Maske `255.255.255.0`, Gateway `192.168.2.254`
   - PC-B2: IP `192.168.2.2`, Maske `255.255.255.0`, Gateway `192.168.2.254`

6. **Teste die Verbindung** im Aktionsmodus:
   - Öffne die Befehlszeile auf PC-A1
   - `ping 192.168.1.2` → Funktioniert (gleiches Netz)
   - `ping 192.168.2.1` → Funktioniert (über Router)

---

## 📝 Übungsaufgaben

### Aufgabe 1: Netzwerkanteil bestimmen
Bestimme für folgende IP-Adressen den Netzwerk- und Hostanteil (Subnetzmaske: `255.255.255.0`):

| IP-Adresse | Netzwerkanteil | Hostanteil |
|-----------|----------------|-----------|
| `10.0.0.5` | ? | ? |
| `172.16.3.100` | ? | ? |
| `192.168.10.1` | ? | ? |

<details>
<summary>Lösung anzeigen</summary>

| IP-Adresse | Netzwerkanteil | Hostanteil |
|-----------|----------------|-----------|
| `10.0.0.5` | `10.0.0` | `.5` |
| `172.16.3.100` | `172.16.3` | `.100` |
| `192.168.10.1` | `192.168.10` | `.1` |
</details>

### Aufgabe 2: Im selben Netzwerk?
Welche der folgenden Geräte können direkt (ohne Router) miteinander kommunizieren?  
Subnetzmaske ist überall `255.255.255.0`.

| Gerät | IP-Adresse |
|-------|-----------|
| A | `192.168.1.10` |
| B | `192.168.1.20` |
| C | `192.168.2.10` |
| D | `192.168.1.30` |
| E | `10.0.0.1` |

<details>
<summary>Lösung anzeigen</summary>

- **A, B, D** sind im selben Netzwerk `192.168.1.0/24` → können direkt kommunizieren
- **C** ist im Netzwerk `192.168.2.0/24` → braucht einen Router
- **E** ist im Netzwerk `10.0.0.0/24` → braucht einen Router
</details>

### Aufgabe 3: Drei Netzwerke (⭐ Herausforderung)
Erweitere dein Filius-Netzwerk um ein **drittes Netzwerk C** (`192.168.3.0/24`):

1. Füge einen zweiten Router oder eine dritte Schnittstelle am bestehenden Router hinzu
2. Erstelle 2 PCs im neuen Netzwerk
3. Konfiguriere alles richtig (IP, Maske, Gateway)
4. Teste: Kann PC-A1 einen PC in Netzwerk C erreichen?

### Aufgabe 4: Python – IP-Adresse analysieren
Schreibe ein Python-Programm, das:
1. Eine IP-Adresse und eine Subnetzmaske als Eingabe nimmt
2. Die Binärdarstellung beider Adressen ausgibt
3. Den Netzwerkanteil berechnet und ausgibt

```python
# Starthilfe:
ip = input("IP-Adresse: ")      # z.B. "192.168.1.10"
maske = input("Subnetzmaske: ")  # z.B. "255.255.255.0"

ip_teile = ip.split(".")
maske_teile = maske.split(".")

# Tipp: Netzwerkanteil = IP AND Maske (bitweise)
# In Python: int(ip_teil) & int(maske_teil)
```

<details>
<summary>Lösung anzeigen</summary>

```python
ip = input("IP-Adresse: ")
maske = input("Subnetzmaske: ")

ip_teile = ip.split(".")
maske_teile = maske.split(".")

print("\nBinärdarstellung:")
print(f"  IP:    {'.'.join(f'{int(t):08b}' for t in ip_teile)}")
print(f"  Maske: {'.'.join(f'{int(t):08b}' for t in maske_teile)}")

netzwerk = []
for i in range(4):
    netzwerk.append(str(int(ip_teile[i]) & int(maske_teile[i])))

print(f"\nNetzwerkanteil: {'.'.join(netzwerk)}")
```
</details>

---

## 🔗 Weiterführende Links

- [inf-schule.de – IP-Adressen](https://www.inf-schule.de/rechnernetze/filius/erkundung_adressierung)
- [Wikipedia – IPv4](https://de.wikipedia.org/wiki/IPv4)

---

[← Zurück: DS 01](01-Rechnernetze.md) · [Weiter → DS 03: DNS](03-DNS.md)
