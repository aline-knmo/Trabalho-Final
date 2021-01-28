from linkedList import LinkedList
import pandas as pd
from printcampos import dadosDicio

class Pessoa():
	def __init__(self, arg):
		self.idade = arg['Idade']
		self.sexo = arg['Sexo']
		self.dorPeito = arg['Dor no peito']
		self.pressaoArt = arg['Pressão arterial em repouso']
		self.colesterol = arg['Colesterol sérico']
		self.glicemiaJejum = arg['Glicemia de jejum']
		self.eletrocardiograma = arg['Eletrocardiograma em repouso']
		self.maxFreqCard = arg['Máx. freq. cardiaca']
		self.anginaIndEsforco = arg['Angina ind. por esforço']
		self.desnivelST = arg['Desniv. do intervalo ST']
		self.inclinacaoST = arg['inclinação do seg. ST']
		self.numPrincVasoSang = arg['num. de princ. vasos sang.']
		self.talassemia = arg['Presença de talassemia']
		self.doencaCardiaca = arg['Presença de doença cardiaca']

		self.dados = pd.Series(arg)  #usado para as funções __repr__ e __eq__
		self.dados.name = None

	def __str__(self):  #Permite usar a função print() com objetos do tipo pessoa
		return str(self.dados)

	def __eq__(self, outraPessoa):  #comparação de igualdade entre duas pessoas	
		return self.dados.equals(outraPessoa.dados)

	def __getitem__(self, indice):
		#pessoa[indice] retorna o valor da variável que corresponde ao indice desejado
		lista = [self.idade, self.sexo, self.dorPeito, self.pressaoArt,
				 self.colesterol, self.glicemiaJejum, self.eletrocardiograma,
				 self.maxFreqCard, self.anginaIndEsforco, self.desnivelST,
				 self.inclinacaoST, self.numPrincVasoSang, self.talassemia,
				 self.doencaCardiaca]

		return lista[indice-1]

	def __len__(self):
		return 14

#100 linhas aleatorias do arquivo
dados = pd.read_csv('heart.csv').sample(7)

#Renomeia os campos da tabela
dados.rename(columns={'age':'Idade', 'sex':'Sexo','cp':'Dor no peito',
					  'trestbps':'Pressão arterial em repouso',
					  'chol':'Colesterol sérico', 'fbs':'Glicemia de jejum',
					  'restecg':'Eletrocardiograma em repouso',
					  'thalach':'Máx. freq. cardiaca','exang':'Angina ind. por esforço',
					  'oldpeak':'Desniv. do intervalo ST', 'slope':'inclinação do seg. ST',
					  'ca':'num. de princ. vasos sang.', 'thal':'Presença de talassemia',
					  'target':'Presença de doença cardiaca'}, inplace=True)

#lista encadeada que armazenará os dados
lista = LinkedList()

#Coloca as informações na lista
for i in range(7):
	pessoa = Pessoa(dados.iloc[i])
	lista.append(pessoa)

if __name__ == '__main__':
	while True:
		print("""	Menu:

	Inserir ---------- I
	Editar ----------- E
	Vizualizar ------- V
	Remover item ----- R
	Sair-------------- S""")

		opera = input().lower()[0]

		if opera == 's':
			break

		elif opera == 'v':
			print(lista)

		elif opera == 'i': #ok^^
			print('Digite o item que você deseja adicionar.\n')
			#coloca os dados do item num dicionário
			item = dadosDicio()  #função no arquivo printcampos.py
			pessoa = Pessoa(item)
			
			opera = input('[ f ] inserir no final\n[ c ] inserir no começo\n[ p ] inserir numa posição específica\n').lower()[0]
			while opera not in 'cpf':
				opera = input('Opção inválida.\n').lower()[0]

			if opera == 'f': #final
				lista.append(pessoa)
			elif opera == 'c': #começo
				lista.insert(0, pessoa)
			elif opera == 'p': #posição específica
				indice = int(input('Em que posição deseja colocar o item? ')) - 1
				lista.insert(indice, pessoa)

			print(f'Item \n\n{pessoa}\n\n inserido.\n')

		elif opera == 'e':
			opera = input('Editar:\n[ i ] item\n[ p ] posição\n').lower()[0]
			while opera not in 'ip':
				opera = input('Opção inválida.\n').lower()[0]

			if opera == 'i':
				print('Qual item você deseja editar?\n')
				#coloca os dados do item num dicionário
				itemVelho = dadosDicio()  #função no arquivo printcampos.py
				pos = lista.index(Pessoa(itemVelho))  #acha o índice do itemVelho

				print(f'O que você deseja colocar no lugar deste item?\n')
				novoItem = dadosDicio()   #coloca os dados do novo item num dicionário
				
				lista[pos] = Pessoa(novoItem)  #substitui o valor do itemVelho pelo valor do novoItem

			elif opera == 'p':
				pos = int(input('Qual posição você deseja editar:\n')) -1

				print(f'O que você deseja colocar na posição {pos+1}?\n')
				#coloca os dados do item num dicionário
				novoItem = dadosDicio()  #função no arquivo printcampos.py

				lista[pos] = Pessoa(novoItem)  #substitui o valor na posição pos

		elif opera == 'r':
			opera = input('Remover:\n[ i ] item\n[ p ] posição\n').lower()[0]
			while opera not in 'ip':
				opera = input('Opção inválida.\n').lower()[0]

			if opera == 'i':
				print('Qual item você deseja remover?\n')
				#coloca os dados do item num dicionário
				item = dadosDicio()  #função no arquivo printcampos.py

				lista.removeItem(Pessoa(item))  #Remove o item desejado

			elif opera == 'p':
				pos = int(input('Qual posição você deseja remover:\n')) -1

				lista.removeIndice(pos)  #remove o item no índice pos
				
		else:
			print('Opção inválida.')