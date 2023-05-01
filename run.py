import os, sys
os.system('clear')
try:
    __import__("BOT").karma()
except Exception as e:
    exit(str(e))
