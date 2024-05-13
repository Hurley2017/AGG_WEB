import os
import sys
import time
from pprint import pprint as p  

K = 1

CVSS_Scores = []

Attack_File = open('attack.P', 'r')
Content = Attack_File.read()
Attack_File.close()

Content = Content.split('\n\n')
Servers = [C.strip('\n') for C in Content if C.startswith('hacl')]

Attack_Header = Content[0]

P_Map = {}
for Server in Servers:
    Lines = Server.split('\n')
    Pairs = []
    for Line in Lines:
        if not Line.startswith('hacl') or not Line.startswith('networkServiceInfo'):
            Pairs.append(Line)
    for Pair in Pairs:
        if Pair.startswith('vulExists'):
            CVE = Pair.split(' ')[1].strip(",").strip("'")
        elif Pair.startswith('vulProperty'):
            CVE = Pair.split(' ')[0].replace('vulProperty', '').strip(',').strip('(').strip("'")
        else:
            continue    
        if CVE not in P_Map:
            P_Map[CVE] = [Pair]
        else:
            P_Map[CVE].append(Pair)  

Nmap_File = open('nmap_all.txt', 'r')
Nmap_Data = Nmap_File.read().split('\n')    
Nmap_File.close()
for CVE in P_Map:
    for Line in Nmap_Data:
        if CVE in Line:
            Line = Line.strip('|').strip(' ').split('\t')[2]
            P_Map[CVE].append(Line)
            CVSS_Scores.append(float(Line))
            break
CVSS_Scores = sorted(CVSS_Scores, reverse=True)
CVSS_Scores = CVSS_Scores[:K]
Curated_Map = {}
Count = 0
for CVE in P_Map:
    if float(P_Map[CVE][2]) in CVSS_Scores:
        Curated_Map[CVE] = P_Map[CVE]
        Count += 1
    if Count == K:
        break

p(Curated_Map)

New_Data = []

for Server in Servers:
    Serv_Data = []
    Lines = Server.split('\n')
    Serv_Data.append(Lines[0]) 
    Lines = Lines[1:] 
    for CVE in Curated_Map:
        for Line in Lines:
            if CVE in Line:
                Serv_Data.append(Line)
            else:
                continue   
    Serv_Data.append(Lines[-1])         
    New_Data.append("\n".join(Serv_Data))

AttackP = Attack_Header + "\n\n" + "\n\n".join(New_Data)
AttackOut = open('Tattack.P', 'w')
AttackOut.write(AttackP)
AttackOut.close()