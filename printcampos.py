import pandas as pd

def PrintCampo(op):
	print(f"""\nEm que campo da tabela você deseja {op} este valor? 

Idade ---------------------------------------- 1
Sexo ----------------------------------------- 2
Tipo de dor no peito ------------------------- 3
Pressão arterial em repouso ------------------ 4
Colesterol sérico em mg/dl ------------------- 5
Glicemia de jejum ---------------------------- 6
Resultados do eletrocardiograma em repouso --- 7
Máxima frequencia cardiaca alcançada --------- 8
Angina induzida por esforço ------------------ 9
Desnivel no intervalo ST --------------------- 10
Inclinação do pico do segmento ST ------------ 11
Número de pricipais vasos sanguineos --------- 12
Presença de talassemia ----------------------- 13
Presença de doença cardiaca ------------------ 14\n""")

def nomeCampo():
	#retorna uma lista com o nome dos campos da tabela
	lista = ['Idade', 'Sexo', 'Dor no peito', 'Pressão arterial em repouso',
			 'Colesterol sérico', 'Glicemia de jejum',
			 'Eletrocardiograma em repouso', 'Máx. freq. cardiaca',
			 'Angina ind. por esforço', 'Desniv. do intervalo ST',
			 'inclinação do seg. ST', 'num. de princ. vasos sang.',
			 'Presença de talassemia', 'Presença de doença cardiaca']
	
	return lista

def entradaDados():
	#retorna uma série com os dados digitados em formato float
	dicio = {'Idade': float(input("Idade: ")), 
	         'Sexo': float(input("Sexo: ")),
			 'Dor no peito' : float(input('Tipo de dor no peito: ')),
			 'Pressão arterial em repouso': float(input('Pressão arterial em repouso: ')),
			 'Colesterol sérico': float(input('Colesterol sérico: ')),
			 'Glicemia de jejum': float(input('Glicemia de jejum: ')),
			 'Eletrocardiograma em repouso': float(input('Resultados do eletrocardiograma: ')),
			 'Máx. freq. cardiaca': float(input('Máxima frequencia cardiaca: ')),
			 'Angina ind. por esforço': float(input('Angina induzida por esforço: ')),
			 'Desniv. do intervalo ST': float(input('Desnivel no intervalo ST: ')),
			 'inclinação do seg. ST': float(input('Inclinação do pico do segmento ST: ')),
			 'num. de princ. vasos sang.' : float(input('Número de pricipais vasos sanguineos: ')),
			 'Presença de talassemia': float(input('Presença de talassemia: ')),
			 'Presença de doença cardiaca': float(input('Presença de doença cardiaca: '))}
	serie = pd.Series(dicio)
	return serie

def dadosDicio():
	#retorna um dicionario com os dados digitados em formato float
	dicio = {'Idade': float(input("Idade: ")), 
	         'Sexo': float(input("Sexo: ")),
			 'Dor no peito' : float(input('Tipo de dor no peito: ')),
			 'Pressão arterial em repouso': float(input('Pressão arterial em repouso: ')),
			 'Colesterol sérico': float(input('Colesterol sérico: ')),
			 'Glicemia de jejum': float(input('Glicemia de jejum: ')),
			 'Eletrocardiograma em repouso': float(input('Resultados do eletrocardiograma: ')),
			 'Máx. freq. cardiaca': float(input('Máxima frequencia cardiaca: ')),
			 'Angina ind. por esforço': float(input('Angina induzida por esforço: ')),
			 'Desniv. do intervalo ST': float(input('Desnivel no intervalo ST: ')),
			 'inclinação do seg. ST': float(input('Inclinação do pico do segmento ST: ')),
			 'num. de princ. vasos sang.' : float(input('Número de pricipais vasos sanguineos: ')),
			 'Presença de talassemia': float(input('Presença de talassemia: ')),
			 'Presença de doença cardiaca': float(input('Presença de doença cardiaca: '))}
	return dicio