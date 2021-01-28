
class Node:
	#Nós da lista
	def __init__(self,item):
		self.item = item
		self.proximo = None

	def __str__(self):
		return str(self.item)

class LinkedList:

	def __init__(self):
		#Cria uma lista vazia
		self.cabeca = None
		self._tamanho = 0

	def append(self, valor):
		#Adiciona o item valor no final da lista
		if self.cabeca:
			auxiliar = self.cabeca
			
			while auxiliar.proximo:  #Percorre a lista até o último nó
				auxiliar = auxiliar.proximo

			auxiliar.proximo = Node(valor)

		else:  #Primeira inserção
			self.cabeca = Node(valor)

		self._tamanho += 1

	def __len__ (self):
		#len(lista) retorna o tamanho da lista encadeada
		return self._tamanho

	def _acharNode(self, indice):
		#Retorna o nó que tem indice como índice
		auxiliar = self.cabeca

		for i in range(indice):  #Percorre a lista até a posição indice
			if auxiliar:
				 auxiliar = auxiliar.proximo
			else: #Levanta um erro se a posição indice não existe na lista
				raise IndexError ('List index out of range')

		return auxiliar

	def __getitem__(self, indice):
	# asdf = lista[4]
		auxiliar = self._acharNode(indice)
		if auxiliar: #Se existe essa posição na lista
			return auxiliar.item
		
		raise IndexError('List index out of range')

	def __setitem__(self, indice, valor):
	# lista[4] = 26
		auxiliar = self._acharNode(indice)

		if auxiliar:  #Se existe essa posição na lista
			auxiliar.item = valor
		else:
			raise IndexError('List index out of range')

	def index(self, valor):
		#Retorna o índice de valor na lista
		auxiliar = self.cabeca
		i = 0
		while auxiliar: #Percorre a lista até achar a posição de valor
			if auxiliar.item == valor:
				return i
			auxiliar = auxiliar.proximo
			i += 1
		#Se o item valor não está na lista levanta um erro
		raise ValueError(f'{valor} is not in list')

	def insert(self, indice, valor):
		#Insere o item valor no índice indice da lista

		newNode = Node(valor)
		if indice == 0:  #Inserção na cabeça da lista
			newNode.proximo = self.cabeca
			self.cabeca = newNode
		else:  #Inserção na cauda da lista
			auxiliar = self._acharNode(indice-1)
			newNode.proximo = auxiliar.proximo
			auxiliar.proximo = newNode
		self._tamanho += 1

	def removeItem(self, valor):
		#Remove o item valor da lista

		if self.cabeca == None:  #Se a lista estiver vazia
			raise ValueError(f'{valor} is not in list')

		elif self.cabeca.item == valor:  #Se o item está na cabeça da lista
			self.cabeca = self.cabeca.proximo
			self._tamanho -= 1
			return True

		else:  #Se o item está na cauda
			antecesor = self.cabeca
			auxiliar = self.cabeca.proximo

			while auxiliar:
				if auxiliar.item == valor:
					antecesor.proximo = auxiliar.proximo
					auxiliar.proximo = None
					self._tamanho -= 1
					return True
				antecesor = auxiliar
				auxiliar = auxiliar.proximo

			#Se o item valor não está na lista levanta um erro
			raise ValueError(f'{valor} is not in list')
	
	def removeIndice(self, indice):
		#Remove o índice indice da lista
		if self.cabeca == None:  #Lista vazia
			raise IndexError('Empty list')

		elif indice > (self._tamanho-1):  #Indice > número de elementos da lista
			raise IndexError ('List index out of range')

		elif indice == 0:  #Remover a cabeça da lista
			self.cabeca = self.cabeca.proximo
			self._tamanho -= 1
			return True

		else:  #Remover índice na cauda da lista
			antecessor = self._acharNode(indice-1) #Nó antecessor
			auxiliar = antecessor.proximo  #Nó que será removido
			antecessor.proximo = auxiliar.proximo
			auxiliar.proximo = None
			self._tamanho -= 1
		
	def __str__(self):
		r = ''
		auxiliar = self.cabeca
		while auxiliar:
			r += str(auxiliar.item) + '\n\n'
			auxiliar = auxiliar.proximo
		return r

if __name__ == '__main__':
	lista = LinkedList()
	lista.append(9)
	lista.append(8)
	lista.append(7)
	lista.append(6)
	lista.append(5)
	lista.append(4)
	lista.append(3)
	lista.append(2)
	lista.append(1)
	lista.append(0)
	lista.insert(5,24)
	lista[1] = 36

	a = lista[7]
	print(f'a = {a}')

	print(len(lista))

	print(lista)

	lista.removeIndice(9)

	lista.removeItem(0)

	print(len(lista))

	print(lista)