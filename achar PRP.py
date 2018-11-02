import re
import os

def leark():
    arq = open('polilex.txt','r',)
    lk=[]
    arq = arq.read()
    arq = arq.split('$.')
    for linha in arq:
        a = linha.splitlines()
        lk.append(a)
    return lk


lkk = leark()
listaN=[]
for i in lkk:
    for el in i:
        if '@X' in el and ' PRP ' in el:
           # print (i)
            listaN.append('\n'.join(i))

listaN='\n$.'.join(listaN)
print(listaN)

arq = open('polilexPRP@X.txt','w',)
arq.write(listaN)
arq.close()

