# import xml.etree.ElementTree as ET

# def parse_nessus_file(file_path):
#     tree = ET.parse(file_path)
#     root = tree.getroot()

#     for report_item in root.findall(".//ReportItem"):
#         port = report_item.get('port')
#         if port != "0":
#             svc_name = report_item.get('svc_name')
#             protocol = report_item.get('protocol')

#             # Extracting CVEs if available, they might be in child elements
#             cves = []
#             for ref in report_item.findall(".//cve"):
#                 cves.append(ref.text)

#             # Formatting CVEs for output
#             cve_str = ", ".join(cves) if cves else "N/A"

#             # Print the findings
#             print(f"Port: {port}, Service Name: {svc_name}, Protocol: {protocol}, CVEs: {cve_str}\n")

# Replace 'file_path_here' with the actual file path
# parse_nessus_file("./data/webvuln.nessus")

import xml.etree.ElementTree as ET

def parse_nessus_file(file_path, output_file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Dictionary to hold data for each port
    port_data = {}

    for report_item in root.findall(".//ReportItem"):
        port = report_item.get('port')
        if port and port != "0":
            svc_name = report_item.get('svc_name')
            protocol = report_item.get('protocol')

            # Extracting CVEs, ensuring no duplication
            new_cves = {ref.text for ref in report_item.findall(".//cve")}

            # If the port is already in the dictionary, update the CVE list
            if port in port_data:
                port_data[port]['cves'].update(new_cves)
            else:
                # Otherwise, create a new entry
                port_data[port] = {
                    'svc_name': svc_name,
                    'protocol': protocol,
                    'cves': new_cves
                }

    # Write data to file
    with open(output_file_path, 'w') as f:
        for port, details in port_data.items():
            cve_str = ", ".join(details['cves']) if details['cves'] else "N/A"
            f.write(f"Port: {port}, Service Name: {details['svc_name']}, Protocol: {details['protocol']}, CVEs: {cve_str}\n\n")

# Replace 'file_path_here' and 'output_file_path_here' with actual paths
parse_nessus_file("./data/vul_s65xv7.nessus", "./data/output.txt")
