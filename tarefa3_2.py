from fila import Fila
from printcampos import dadosDicio  #Usada na função inserir
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

	def __repr__(self):
		return str(self.dados)

	def __str__(self):  #Permite usar a função print() com objetos do tipo pessoa
		return self.__repr__()

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

#Lê 100 linha aleatorias (e sem repetições) do arquivo 
dados = pd.read_csv('heart.csv').sample(100)
dados.rename(columns={'age':'Idade', 'sex':'Sexo','cp':'Dor no peito',
					  'trestbps':'Pressão arterial em repouso',
					  'chol':'Colesterol sérico', 'fbs':'Glicemia de jejum',
					  'restecg':'Eletrocardiograma em repouso',
					  'thalach':'Máx. freq. cardiaca','exang':'Angina ind. por esforço',
					  'oldpeak':'Desniv. do intervalo ST', 'slope':'inclinação do seg. ST',
					  'ca':'num. de princ. vasos sang.', 'thal':'Presença de talassemia',
					  'target':'Presença de doença cardiaca'}, inplace=True)

#Fila que armazenará os dados
fila = Fila()

for i in range(0,100):
	#Coloca as 100 linha aleatorias na fila
	pessoa = Pessoa(dados.iloc[i])
	fila.put(pessoa)

if __name__ == '__main__':
	while True:
		print("""Menu:

	Inserir item ----------------- I
	Vizualizar fila -------------- V
	Vizualizar primeiro item ----- P
	Ver o tamanho da fila -------- T
	Remover primeiro item -------- R
	Sair do programa ------------- S""")

		opera = input().upper()[0]
		
		if opera == 'S':  #Sair do programa
			break

		elif opera == 'I':  #Inserir item no final da fila
			print('Digite os dados que você deseja adicionar:\n')
			item = dadosDicio()  #Coloca os dados digitados num dicionário
			pessoa = Pessoa(item)  #Cria um objeto do tipo pessoa com os dados

			fila.put(pessoa)  #Coloca pessoa no final da lista
			print(f"Valor:\n\n{pessoa}\n\ninserido.\n")

		elif opera == 'V':  #Ver fila inteira
			print(fila)

		elif opera == 'P':  #Ver a cabeça da fila
			print(f'O primeiro elemento da fila é:\n{fila.peek()}\n')

		elif opera == 'R':  #Remover a cabeça da fila
			itemTopo = fila.get()
			print(f'Item:\n\n{itemTopo}\n\nremovido.\n')

		elif opera == 'T':  #Ver tamanho da fila
			print(f'A fila tem {len(fila)} itens.')

		else:
			print('Opção inválida.')
