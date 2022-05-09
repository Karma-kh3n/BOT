P = '\x1b[1;97m'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(M))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "KARMA" == fc:
		__import__("KARMA").checkin()
	else:
		__import__(".....").checkin()
