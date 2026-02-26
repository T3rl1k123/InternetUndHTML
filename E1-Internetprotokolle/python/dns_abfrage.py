# DNS-Abfrage in Python
# Fragt die IP-Adresse zu einem Domainnamen ab.

import socket

print("=== DNS-Abfrage-Tool ===\n")

while True:
    domain = input("Domain eingeben (oder 'quit'): ").strip()
    
    if domain.lower() == "quit":
        break
    
    if not domain:
        print("Bitte eine Domain eingeben!\n")
        continue
    
    try:
        ip = socket.gethostbyname(domain)
        print(f"  {domain} → {ip}\n")
    except socket.gaierror:
        print(f"  Fehler: '{domain}' konnte nicht aufgelöst werden.\n")

print("Programm beendet.")
