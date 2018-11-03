import re

def leark():
    arq = open('polilexN@X-setahihe.txt','r',encoding="latin-1")
    lk=[]
    arq = arq.read()
    lk = arq.split('$. 0>>') #SEPARA EM MWEs
    for x,item in enumerate(lk):
		lk[x] = lk[x].splitlines() #SEPARA CADA PALAVRA DENTRO DA MWE

	return lk

lk=leark()

for a,mwe in enumerate(lk): #LOOP ENTRE MWEs
	for b,palavra in enumerate(mwe): #LOOP ENTRE PALAVRAS DENTRO DAS MWEs
		encontrou = False
		if '@>' in palavra:
			classe = palavra.split('@>')[1].split(' ')[0] #QUALQUER CLASSE GRAM. QUE VENHA DEPOIS DE '@>', NÃO SÓ ' N ', E O ESPAÇO
			if classe == 'P': classe = 'PRP'
			for c,parabaixo in enumerate(mwe):
				if ' ' + classe + ' ' in parabaixo and c>b: #O NÚMERO DA LINHA QUE CONTÉM ' N ' É MAIOR QUE O NÚMERO DA LINHA QUE CONTÉM ' @> '
					encontrou = True
					tokenquequero = parabaixo.split('>>')[0][-1]
					lk[a][b] = lk[a][b] + tokenquequero #LK[A] = MWE, LK[A][B] = PALAVRA/LINHA
					break
			if not encontrou:
				print('not encontrou')
				classe = 'PROP'
				for c,parabaixo in enumerate(mwe):
					if ' ' + classe + ' ' in parabaixo and c>b: #O NÚMERO DA LINHA QUE CONTÉM ' N ' É MAIOR QUE O NÚMERO DA LINHA QUE CONTÉM ' @> '
						tokenquequero = parabaixo.split('>>')[0][-1]
						lk[a][b] = lk[a][b] + tokenquequero #LK[A] = MWE, LK[A][B] = PALAVRA/LINHA
						break

#AGORA PARA CIMA
for a,mwe in enumerate(lk): #LOOP ENTRE MWEs
	for b,palavra in enumerate(mwe): #LOOP ENTRE PALAVRAS DENTRO DAS MWEs
		regex = re.search('@(.*)<',palavra)
		if regex:
			classe = regex[1] #QUALQUER CLASSE GRAM. QUE VENHA DEPOIS DE '@>', NÃO SÓ ' N ', E O ESPAÇO
			if classe == 'P': classe = 'PRP'
			for c,paracima in enumerate(mwe):
				if ' ' + classe + ' ' in paracima and c<b: #O NÚMERO DA LINHA QUE CONTÉM ' N ' É MAIOR QUE O NÚMERO DA LINHA QUE CONTÉM ' @> '
					tokenquequero = paracima.split('>>')[0][-1]
					lk[a][b] = lk[a][b] + tokenquequero #LK[A] = MWE, LK[A][B] = PALAVRA/LINHA					
					break


#PRINTAR NO FORMATO STR //não consegui printar a lista de forma legível
novotexto = str()
for mwe in lk:
	novotexto = novotexto + '$. 0>>'
	for linha in mwe:
		novotexto = novotexto + linha + '\n'

print(novotexto)
'''
arq = open('@X@N-feito.txt','w',)
arq.write(novotexto)
arq.close()
'''

'''
casos com verbos serão tratados caso a caso na mão.
fazer uma linha (aquele programa anterior) para que os casos de @X que
colocaria 0, sejam hi
em casos de @Y fazer uma linha para colocar he
para dar uma geral procurar por '>>\n'
'''
