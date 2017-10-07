import xml.etree.ElementTree as ET

masscan_file = 'result.xml'
tree = ET.parse(masscan_file)
root = tree.getroot()

f = open('output.txt', 'w')

for data in root.iter('address'):
    ip = data.get('addr')
    for data in root.iter('port'):
        port = data.get('portid')
    f.write(ip + ':' + port + '\n')
f.close()