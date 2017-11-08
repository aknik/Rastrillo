# -*- coding: utf-8 -*-
# apt install python-ecdsa python-numpy libwww-perl
from bcoin import *
amount = 0
acumulado = float(0)
outfile = open("a.txt","a") # open file for appending
n=1
status_code = 0
while True:
	bytes = aleat(256)
	pk = int (bytes,16) #^ int("99A2170A6A172889A8CA10E04E11AF25272F07A836BE37F9B5BCDCE42B4FB60C", 16) 
	privkey = (str(hex(pk)))[2:-1]
	privkey = privkey.rjust(64, "0").upper()
	pubkey = pubb(pk)  
	url = "https://blockchain.info/es/q/addressbalance/" + addy(pk)
	while (status_code != 200):

		r = requests.get(url)
		status_code = r.status_code
		if status_code == 429: sleep(10)
		if status_code == 500: break
		sleep(1)
		try:
		    amount = get_num(r.text)
		except: 
		    print  status_code
		else:
		    print n , amount, status_code, " a"
		    n += 1
		# sys.stdout.write('%s\r' % str(n))
		# sys.stdout.flush()
	status_code = 0
	if amount > 0 : 
		reply(str(pk))
		outfile.write(str(amount/100000000) +","+ addy(pk) +","+ numtowif(pk) +"\n")

outfile.close()

