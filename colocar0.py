
def leark():
    arq = open('testePRP@X-seta.txt','r',)
    lk=[]
    arq = arq.read()
    arq = arq.split('$.')
    for linha in arq:
        a = linha.splitlines()
        lk.append(a)
    return lk

lk=leark()
print(lk)
X=[]
lk2=[]
for i in lk:
    for el in range(len(i)):
        if '@X' in i[el]:
            X.append(el+1)
            i[el] = i[el] + '0'
        if '@Y' in i[el]:
            lk2.append(el+1)
            i[el] = i[el] + 'he'
        else:
            if '@X' and '@Y' in i:
                i[el]= i[el]+'hi'
    lk2.append(i)
print(lk2)
'''
lk4=[]
for i in lk2:
    lk3=' '.join(lk2)
    lk4.append(lk3)
print(lk4)
'''
#lk4='\n$.'.join(lk2)

arq = open('testeP@X0.txt','w',)
arq.write(lk2)
arq.close()


