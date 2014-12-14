import urllib
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
u = urllib.urlopen(url) 
data = u.read()
answer = data[24:]

for i in range(1,999):
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+answer
	u = urllib.urlopen(url)
	data = u.read()
	answer = data[24:]
	print answer

