# Filius-Anleitung: Routing – Zwei Netzwerke verbinden

> Zu [DS 02 – IP-Adressen und Routing](../02-IP-Adressen-und-Routing.md)

---

## Ziel

Zwei separate Netzwerke mit einem Router verbinden, sodass PCs aus Netz A mit PCs aus Netz B kommunizieren können.

## Netzplan

```
Netzwerk A: 192.168.1.0/24              Netzwerk B: 192.168.2.0/24

  PC-A1 (192.168.1.1) ──┐                ┌── PC-B1 (192.168.2.1)
                       Switch-A ── Router ── Switch-B
  PC-A2 (192.168.1.2) ──┘                └── PC-B2 (192.168.2.2)

Router:
  Schnittstelle 1: 192.168.1.254 (Netz A)
  Schnittstelle 2: 192.168.2.254 (Netz B)
```

## Schritt 1: Geräte platzieren

1. Im **Entwurfsmodus**: Platziere:
   - 2 Switches (Switch-A links, Switch-B rechts)
   - 1 Router (in der Mitte)
   - 2 PCs links (PC-A1, PC-A2), verbunden mit Switch-A
   - 2 PCs rechts (PC-B1, PC-B2), verbunden mit Switch-B

2. Verbinde Switch-A mit dem Router (Kabel)
3. Verbinde Switch-B mit dem Router (Kabel)

## Schritt 2: Router konfigurieren

1. **Doppelklicke** auf den Router
2. Du siehst mehrere Schnittstellen (Anschlüsse)
3. Konfiguriere:
   - **Schnittstelle zum Switch-A:** IP `192.168.1.254`, Maske `255.255.255.0`
   - **Schnittstelle zum Switch-B:** IP `192.168.2.254`, Maske `255.255.255.0`

> **Tipp:** Achte darauf, welcher Anschluss mit welchem Switch verbunden ist!

## Schritt 3: PCs in Netzwerk A konfigurieren

Doppelklicke auf jeden PC und trage ein:

| PC | IP-Adresse | Subnetzmaske | Gateway |
|----|-----------|-------------|---------|
| PC-A1 | `192.168.1.1` | `255.255.255.0` | `192.168.1.254` |
| PC-A2 | `192.168.1.2` | `255.255.255.0` | `192.168.1.254` |

> **Wichtig:** Der Gateway ist die IP-Adresse des Routers im eigenen Netzwerk!

## Schritt 4: PCs in Netzwerk B konfigurieren

| PC | IP-Adresse | Subnetzmaske | Gateway |
|----|-----------|-------------|---------|
| PC-B1 | `192.168.2.1` | `255.255.255.0` | `192.168.2.254` |
| PC-B2 | `192.168.2.2` | `255.255.255.0` | `192.168.2.254` |

## Schritt 5: Testen

1. Wechsle in den **Aktionsmodus** (▶️)
2. Installiere die **Befehlszeile** auf PC-A1
3. Teste:
   - `ping 192.168.1.2` → PC-A2 im eigenen Netz ✅
   - `ping 192.168.2.1` → PC-B1 im anderen Netz ✅ (über Router)
   - `ping 192.168.2.2` → PC-B2 im anderen Netz ✅ (über Router)

## Häufige Fehler

| Problem | Mögliche Ursache |
|---------|-----------------|
| Ping im eigenen Netz geht, aber nicht ins andere | Gateway ist nicht eingetragen oder falsch |
| Gar kein Ping möglich | IP-Adressen oder Subnetzmasken stimmen nicht |
| Router antwortet nicht | Router-Schnittstellen nicht richtig konfiguriert |

---

[Zurück zur Übersicht](../02-IP-Adressen-und-Routing.md)
