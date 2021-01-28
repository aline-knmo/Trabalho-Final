class Node:
	def __init__(self,item):
		self.item = item
		self.proximo = None
		
	def __str__(self):
		return str(self.item)

class Stack:
	def __init__(self):
		self.top = None
		self._tamanho = 0

	def push(self, item):
		novo = Node(item)
		novo.proximo = self.top
		self._tamanho += 1
		self.top = novo

	def pop(self):
		if self._tamanho == 0:
			raise IndexError('Pilha vazia.')
		else: 
			item = self.top.item
			self.top = self.top.proximo
			self._tamanho -= 1
			return item

	def peek(self):
		if self._tamanho > 0:
			return self.top.item
		raise IndexError('Pilha vazia.')

	def __len__ (self):
		return self._tamanho

	def __repr__ (self):
		r = ''
		auxiliar = self.top
		while auxiliar:
			r += str(auxiliar.item) + '\n'
			auxiliar = auxiliar.proximo
		return r

	#Permite usar a função print() para exibir a pilha
	def __str__(self):
		return self.__repr__()
