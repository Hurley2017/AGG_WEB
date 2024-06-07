import os
Vulners = r'"C:\Program Files (x86)\Nmap\scripts\vulners.nse"'
Data = ['44.228.249.3']
Scan_Result = []
for Ip in Data:
    print(Ip)
    Scan_Result.append(os.popen(f"nmap -sV --script={Vulners} {Ip} --resolve-all").read())

Scan_Result = "\n".join(Scan_Result)

File = open("DebugOut/nmap_all_deep.txt", "w")
File.write(Scan_Result)
File.close()