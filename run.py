import os, sys
os.system('clear')
try:
    __import__("run").login_kamu()
except Exception as e:
    exit(str(e))
