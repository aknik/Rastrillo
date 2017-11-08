# -*- coding: utf-8 -*-
# apt install python-ecdsa python-numpy libwww-perl
from bcoin import *
amount = 0
outfile = open("b.txt","a") # open file for appending
n=1
status_code = 0
while True:
	bytes = aleat(256)
	pk = int (bytes,16) #^ int("99A2170A6A172889A8CA10E04E11AF25272F07A836BE37F9B5BCDCE42B4FB60C", 16) 
	privkey = (str(hex(pk)))[2:-1]
	privkey = privkey.rjust(64, "0").upper()
	pubkey = pubb(pk)  
	url = "https://api.blocktrail.com/v1/btc/address/"+addy(pk)+"?api_key=4d82c5bf7bd351d2b526f9a2a4f63369176c6ae3"
	agent = '"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"'
	headers = {	'User-Agent': agent,'Accept-Encoding': 'gzip','accept-language': 'es-ES','Connection': 'Keep-Alive',}
	while (status_code != 200):
		r = requests.get(url)
		status_code = r.status_code
		if status_code == 429 : sleep(10) 
		if status_code == 404 : status_code = 200
		if status_code == 500: break
		try:
		    amount = float((r.json()['balance']))
		except:
		    print status_code
		else:
		    print n, amount , status_code, " b"
		    n += 1
	status_code = 0
	if amount > 0 : 
		reply(str(pk))
		reply(str(url))
		outfile.write(str(amount/100000000) +","+ addy(pk) +","+ numtowif(pk) +"\n")

outfile.close()

