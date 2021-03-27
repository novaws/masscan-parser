#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()

for data in root.iter('address'):
    ip = data.get('addr')
    for data in root.iter('port'):
        port = data.get('portid')
    print(ip + ':' + port)