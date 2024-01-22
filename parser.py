#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) < 2:
    print("\033[1;31m" + "Argument missing:\n" + "\033[0m"
          "Please specify the path to the masscan XML file.\n"
          "\033[1m" + "Usage: " + "\033[0;4m" + "python3 parser.py <path_to_xml_file>" + "\033[0m")
    sys.exit(1)

try:
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
    
    for data in root.iter('host'):
        ip = data.find('address').get('addr')
        for ports in data.iter('port'):
            port = ports.get('portid')
        print(ip + ':' + port)

except ET.ParseError as e:
    print("\033[0;31m" + "XML parsing error:\n" + str(e) + "\033[0m")
except FileNotFoundError as e:
    print("\033[0;31m" + "File not found. Please check the file path:\n" + str(e) + "\033[0m")
