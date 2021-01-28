from arvore3 import ArvoreBinaria
import printcampos as pcamp
import pandas as pd

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
dados = pd.read_csv('heart.csv').sample(100)

#Renomeia os campos da tabela
dados.rename(columns={'age':'Idade', 'sex':'Sexo','cp':'Dor no peito',
					  'trestbps':'Pressão arterial em repouso',
					  'chol':'Colesterol sérico', 'fbs':'Glicemia de jejum',
					  'restecg':'Eletrocardiograma em repouso',
					  'thalach':'Máx. freq. cardiaca','exang':'Angina ind. por esforço',
					  'oldpeak':'Desniv. do intervalo ST', 'slope':'inclinação do seg. ST',
					  'ca':'num. de princ. vasos sang.', 'thal':'Presença de talassemia',
					  'target':'Presença de doença cardiaca'}, inplace=True)

#Árvores que armazenarão os dados
arvore = ArvoreBinaria()   #Ordenada pela idade
arvoreP = ArvoreBinaria()  #Ordenada pela pressão arterial
arvoreF = ArvoreBinaria()  #Ordenada pela frequencia cardiaca

#Inserção dos itens aleatorios nas árvores
for i in range(0,100):
	pessoa = Pessoa(dados.iloc[i])
	arvore.inserir(pessoa, 1)
	arvoreP.inserir(pessoa, 4)
	arvoreF.inserir(pessoa, 8)

if __name__ == '__main__':
	while True:
		print("""\n             Menu:

	Inserir item ----------------- I

	Vizualizar dados ordenados por:
	Idade ------------------------ VI
	Pressão arterial em repouso -- VP
	Máxima frequencia cardiaca --- VF

	Pesquisar -------------------- P

	Remover item ----------------- RI

	Remover valor ---------------- RV

	Sair do programa ------------- S""")

		opera = input().strip().upper()
		
		if opera[0] == 'S':  #Sair do programa
			break

		elif opera[0] == 'P':  #Mostra todos os itens com um determinado valor no campo desejado
			valor = float(input('Que valor você deseja procurar? ')) #Valor que será procurado
			
			pcamp.PrintCampo('pesquisar')
			campo = int(input())  #Campo da tabela em que o valor será procurado
			
			print(f'\nItens da tabela com o valor {valor} no campo {campo}:')
			arvore.pesquisa(valor, campo)

		elif opera[0] == 'I':  #Inserir
			print('Digite os dados que você deseja adicionar:\n')
			item = pcamp.dadosDicio()  #Coloca os dados num dicionario
			pessoa = Pessoa(item)      #Cria um objeto do tipo pessoa com os dados

			#Insere o novo item nas três árvores
			arvore.inserir(pessoa, 1)
			arvoreP.inserir(pessoa, 4)
			arvoreF.inserir(pessoa, 8)

			print(f"Valor\n\n{pessoa}\n\ninserido.\n")

		elif opera == 'VI':  #Vizualizar por idade
			print('\nDados com o índice idade em ordem crescente:\n')
			arvore.EMordem()

		elif opera == 'VP': #Vizualizar por pressão sanguinea
			print('\nDados com o índice pressão arterial em repouso em ordem crescente:\n')
			arvoreP.EMordem()

		elif opera == 'VF':  #Vizualizar por frequencia cardiaca
			print('\nDados com o índice máxima frequencia cardiaca em ordem crescente:\n')
			arvoreF.EMordem()

		elif opera == 'RI':  #remover um item específico
			print('Qual item você deseja remover?\n')
			
			item = pcamp.dadosDicio()  #Coloca os dados d item num dicionario
			pessoa = Pessoa(item)      #Cria um objeto do tipo pessoa com os dados

			#Remove o item nas três árvores
			arvore.remover_item(pessoa,1)
			arvoreF.remover_item(pessoa,4)
			arvoreP.remover_item(pessoa,8)

			print(f"Valor\n\n{pessoa}\n\nremovido.\n")

		elif opera == 'RV': #remover itens com um determinado valor no campo desejado
			valor = float(input('Que valor você deseja remover? '))  #Valor que será removido
			pcamp.PrintCampo('remover')
			campo = int(input())  #Campo em que o valor deve ser procurado 

			#Lista com os nós em que o campo campo vale valor
			lista = list()
			arvore.pesquisa(valor, campo, lista=lista)

			#Remoção dos nós contidos na lista da três árvores 
			for i in lista:
				arvore.remover_item(i,1)
				arvoreP.remover_item(i,4)
				arvoreF.remover_item(i,8)

			print(f'Itens com valor {valor} no campo {campo} removidos.')

		else:
			print('Opção inválida.')