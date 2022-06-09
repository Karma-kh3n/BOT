#CODED BY KARMA DAVID
#UPDATED 9 JUNE 2022


import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nBAD INTERNET CONNECTION\n'%(M))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("IG").checkin()
	else:
		__import__("IG").checkin()
