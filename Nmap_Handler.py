import os
import sys
import time

Scan_Result = []

Vulners = r'"C:\Program Files (x86)\Nmap\scripts\vulners.nse"'

CIDR = '192.168.1.1/24'
os.system("nmap -sP 192.168.1.1/24 -oN DebugOut/Nmap_scan.txt")
File = open("DebugOut/nmap_scan.txt", "r")
Data = File.read()
File.close()
Data = Data.split("\n")[1:]
Data = [D.split(' ')[-1] for D in Data if ".".join(CIDR.split(".")[:-1]) in D]
for Ip in Data:
    print(Ip)
    Scan_Result.append(os.popen(f"nmap -sV --script={Vulners} {Ip}").read())

Scan_Result = "\n".join(Scan_Result)

File = open("DebugOut/nmap_all.txt", "w")
File.write(Scan_Result)
File.close()

os.system("python3 mulval_inp_gen.py 172.28.29.180")
os.system("python3 Truncate_AttackP.py")