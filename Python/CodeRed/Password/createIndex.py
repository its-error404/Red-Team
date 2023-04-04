import sys,time,struct,hashlib,argparse,threading,platform

from os import _exit,getcwd, path

try:
    from algorithms import algorithms

except ImportError:
    sys.stderr.write("Missing file Algorithms.py")
    _exit(2)
    
if platform.system().lower() in ['linux','darwin']:
    W = "\033[0m"
    R = "\033[31m"
    P = "\033[35m"
    C = "\033[36m"
    O = "\033[33m"
    bold = "\033[1m"
    clear = chr(27) + '[2K\r'

else:
    bold = W = R = P = C = O = ""
    clear = '\n'
    
INFO = bold + C + "[*] " + W
WARN = bold + R + "[!] " + W
MONEY = bold + O + "[$] " + W
PROMPT = bold + P + "[?] " + W

def create_index(fword,fout,algorithm,flock):
    position = fword.tell()
    line = fword.readline()
    while line:
        word = line.strip()
    
    


    
