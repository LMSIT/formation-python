#!/usr/bin/env python3

IPS = [
    "192.168.1.10",
    "172.100.2.11"
]


output = [
    "Order Allow,Deny"
]

for ip in IPS:
    output.append(f"Allow from {ip}")

output.append("Deny from all")

with open("htaccess.txt", "w") as fp:
    for out in output:
        fp.write(f"{out}\n")
