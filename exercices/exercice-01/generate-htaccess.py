#!/usr/bin/env python3

# List des adresses IP du client 
IPS = [
    "192.168.1.10",
    "172.100.2.11",
    "10.0.1.9.10",
    "192.168.1.10",
    "172.100.2.11",
    "10.0.1.9.10"
]

# Ici c'est l'entête de notre fichier htaccess
output = [
    "Order Allow,Deny"
]

# chemin relative vers notre fichier htaccess
file_output = "exercices/exercice-01/htaccess.txt"

for ip in IPS:
    # print(ip)
    output.append(f"Allow from {ip}")

output.append("Deny from all")

# on écrit le tout dans notre fichier 
with open(file_output, "w") as fp:
    for out in output:
        fp.write(f"{out}\n")

