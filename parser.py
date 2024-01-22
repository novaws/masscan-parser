#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

for data in root.iter('host'):
    ip = data.find('address').get('addr')
    for ports in data.iter('port'):
        port = ports.get('portid')
    print(ip + ':' + port)
