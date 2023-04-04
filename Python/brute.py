import os

f = open('random.dic','r')
words = f.readlines()

count = 0

for word in words:
    count+=1
    if "Incorrect" not in os.open("./program " + word):
        os.system("./program " + word)
        break
    
    