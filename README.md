# masscan-parser

Save masscan XML result to result.xml and run my script.

Usage example :
masscan -p80 192.168.0.0/16 -oX result.xml --rate=10000

After scan run my script ./parser.py, and you will see output.txt

Output : 
IP:PORT