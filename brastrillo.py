# -*- coding: utf-8 -*-
# apt install python-ecdsa python-numpy libwww-perl
from bcoin import *
amount = 0
acumulado = float(0)
outfile = open("pillado.txt","a") # open file for appending
n=0
status_code = 0

while True:
	#bytes = fourmi(256)  #"" Returns a list of n random bits.  from FourmiLab """
	#bytes = aleat(256)    #"" Returns a list of n random bits.  from dev/random  """
	n = n + 1
	# Seleccion de la fuente de numeros aleatorios http://www.random.org o http://www.fourmilab.ch
	#bytes = randomorg()
	#bytes = fourmi(1)import re
	#bytes = fourmi2()
	#bytes = paleat (256/8)
	bytes = aleat(256)
	#bytes = bytes + bytes + bytes + bytes  
	# bytes de prueba
	#bytes = "0x000003A28AF16B7620C6AA0E3544C6B668259D40DDBDA9E29F3E2EC35E015194"
	#print validwif('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTJ')
	#print validwif('5HueCGU8rMjxEXxiPuD5BDku4MkFqeZyd4dZ1jvhTVqvbTLvyTK')
	#pk = int(hashlib.sha256('something small and easy to remember but not easy to guess').hexdigest(),16)
	#pk = 0X43D526519BB23D81EA7870AC864EE10F50BE691687AFA1A48FD0C99A2BC88EE5
	# Realizamos XOR con el valor obtenido via web con 32 bytes elegidos por nosotros. Paranoicos ;-)
	pk = int (bytes,16) #^ int("99A2170A6A172889A8CA10E04E11AF25272F07A836BE37F9B5BCDCE42B4FB60C", 16) 

	if validwif(numtowif(pk)):    

		privkey = (str(hex(pk)))[2:-1]
		privkey = privkey.rjust(64, "0").upper()
		#pk =(int(hashlib.sha256(file('hiddeninplainsight.jpg','rb+').read()).hexdigest(),16))
		#1FfmbHfnpaZjKFvyi1okTjJJusN455paPH
		pubkey = pubb(pk)  
		url = "https://www.blockonomics.co/api/balance" 
		# url = "https://www.blockonomics.co/api/balance " + "1FfmbHfnpaZjKFvyi1okTjJJusN455paPH" 
		agent = '"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"'
		headers = {
		'User-Agent': agent,
		'Accept-Encoding': 'gzip',
		'accept-language': 'es-ES',
		'Connection': 'Keep-Alive',
		}

		while (status_code != 200):

			r = requests.post(url, headers = headers,json={"addr": addy(pk)})
			status_code = r.status_code
			amount = (r.json()['response'][0]['confirmed'])
			print r.json()['response'][0]['addr'], amount , status_code
			
			if status_code == 429: sleep(10)
			if status_code == 500: status_code = 200
            
		status_code = 0
		if amount > 0 : 
			reply(str(pk))
			outfile.write(str(amount/100000000) +","+ addy(pk) +","+ numtowif(pk) +"\n")
			outfile.close()

