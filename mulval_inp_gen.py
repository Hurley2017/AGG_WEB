import re
import sys
import os
from copy import copy 
from pprint import pprint as p

if len(sys.argv) == 2: 
    TARGET = sys.argv[1]
else:
    print("Usage: python mulval_inp_gen.py <TARGET>")
    print('Specify target.')
    exit(1)        

matchCVE = re.compile(r'\bCVE[\d-]+')

MASTER_MAP = {}

f = open('DebugOut/nmap_all.txt','r')
DATA = f.read()
f.close()

DATA = DATA.split('Nmap scan report for')

for Content in DATA[1:]:
    IP = Content.split('\n')[0].split(' ')[-1].strip('(').strip(')')
    Port_Service = {}   
    Content = Content.split('\n')
    FilteresContent = []
    gotStart = False
    for line in Content:
        if line.startswith('Host is up'):
            gotStart = True
        if not gotStart:
            continue
        if not line.startswith('<'):
            FilteresContent.append(line)
    Series = []
    for line in FilteresContent:
        if '/tcp' in line and not line.startswith('|'):
            prt = int(line.split('/tcp')[0])
            service = line.split('open')[1].strip().split(' ')[0].strip()
            application = line.split(service)[-1].strip().split(' ')[0]
            Series.append(prt)
            Series.append(service + '_:_'+application)           
        if '/udp' in line and not line.startswith('|'):
            Series.append(int(line.split('/tcp')[0]))
            Series.append(line.split('open')[1].strip().split(' ')[0])
        Series.append(''.join(matchCVE.findall(line))[0:])   
    print(Series)     
    FilteredSeries = []
    for item in Series:
        if item == '':
            continue 
        if type(item) == str and 'CVE' in item:
            if len(item.split('-')) > 3:
                for CVE in item.split('CVE'):
                    if CVE == '':
                        continue
                    FilteredSeries.append('CVE'+CVE)
            else:
                FilteredSeries.append(item)        
        else:
            FilteredSeries.append(item) 
    print(FilteredSeries)           
    # VULINFO = open('vul_info1.txt', 'w')
    # for item in FilteredSeries:
    #     VULINFO.write(str(item)+'\n')   
    # VULINFO.close()                 
    PointStatus = [None, None]
    for item in FilteredSeries:
        if type(item) == int:
            PointStatus[0] = copy(item)
            Port_Service[item] = {}
        if type(item) == str:
            if not item.startswith('CVE'):
                PointStatus[1] = copy(item)
                Port_Service[PointStatus[0]][PointStatus[1]] = []
            else:
                Port_Service[PointStatus[0]][PointStatus[1]].append(item)
                

    for key in Port_Service:
        for key2 in Port_Service[key]:
            if len(Port_Service[key][key2]) != 0:
                Port_Service[key][key2] = list(set(Port_Service[key][key2]))                       
    MASTER_MAP[IP] = copy(Port_Service)
p(MASTER_MAP)

mulval_input = f"attackerLocated(internet).\nattackGoal(execCode(server_{"_".join(TARGET.split('.'))},_)).\n\n"

for IP in MASTER_MAP:
    server_id = f"server_{IP.replace('.', '_')}"
    for Port in MASTER_MAP[IP]:
        for SAPP in MASTER_MAP[IP][Port]:
            service = SAPP.split('_:_')[0]
            application = SAPP.split('_:_')[1]
            transport = 'tcp'
            mulval_input += f"hacl(internet, {server_id}, '{transport}', {Port}).\n"
            for CVE in MASTER_MAP[IP][Port][SAPP]:
                mulval_input += (f"vulExists({server_id}, '{CVE}', '{service}').\n"
                                 f"vulProperty('{CVE}', remoteExploit, privEscalation).\n")
            mulval_input += f"networkServiceInfo({server_id}, '{service}', '{transport}', {Port}, '{application}').\n\n"

# print(mulval_input)

MUL_ATK = open('DebugOut/attack.P', 'w')
MUL_ATK.write(mulval_input)
MUL_ATK.close()

