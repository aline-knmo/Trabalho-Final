from stack import Stack
import pandas as pd
from printcampos import dadosDicio  #Usada na função inserir

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

#Pilha que armazenará os dados
pilha = Stack()

#Coloca as informações na pilha
for i in range(100):
	pessoa = Pessoa(dados.iloc[i])
	pilha.push(pessoa)

if __name__ == '__main__':
	while True:
		print("""Menu:

Inserir ------------- I
Vizualizar pilha ---- V
Vizualizar topo ----- T
Remover item -------- R
Sair----------------- S""")
		opera = input().lower()[0]
		if opera == 's':
			break

		elif opera == 'i':
			print('Digite os dados que você deseja adicionar.\n')
			item = dadosDicio()
			pessoa = Pessoa(item)
			pilha.push(pessoa)
			print(f'Item \n\n{pessoa}\n\n inserido.\n')

		elif opera == 'v':
			print(pilha)

		elif opera == 't':
			print(pilha.peek())

		elif opera == 'r':
			itemTopo = pilha.pop()
			print(f'Item \n\n{itemTopo}\n\n removido.\n')

		else:
			print('Opção inválida.')
