#CODED BY KARMA DAVID
#UPDATED 9 JUNE 2022


import platform
import os
os.system('git pull')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("bot").checkin()
elif 'aarch' in arc:
	__import__("bot").checkin()
else:
	exit(f' Unknow device machine {arc}')
