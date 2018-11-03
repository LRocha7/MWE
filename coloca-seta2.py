
def leark():
    arq = open('polilexPRP@X.txt','r',)
    lk=[]
    arq = arq.read()
    arq = arq.split('$.')
    for linha in arq:
        a = linha.splitlines()
        lk.append(a)
    return lk

lk=leark()

#print(lk)

lk2=[]

for elem in lk:
    i=0
    for q in elem:
        lk2.append(q + " {}>>".format(i))
        i+=1

#print(lk2)

lk2='\n'.join(lk2)
print(lk2)

arq = open('polilexPRP@X-seta.txt','w',)
arq.write(lk2)
arq.close()              

    
