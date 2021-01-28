class Node:
	def __init__(self,item):
		self.item = item
		self.proximo = None

	def __str__(self):
		return str(self.item)

class Fila:
	def __init__(self):
		self.primeiro = None
		self.ultimo = None
		self._tamanho = 0

	def put(self, item):
	#Insere o valor item no final da fila
		novo = Node(item)

		if self.primeiro is None:  #Primeira inserção
			self.primeiro = novo

		if self.ultimo is None:  #Primeira inserção
			self.ultimo = novo
		else:
			self.ultimo.proximo = novo
			self.ultimo = novo

		self._tamanho += 1

	def get(self):
	#remove o primeiro valor da fila
		if len(self) > 0:  #Se a fila não está vazia  
			retorno = self.primeiro.item
			self.primeiro = self.primeiro.proximo
			self._tamanho -= 1
			return retorno
		raise IndexError ('Fila vazia.')  #Levanta um erro se a fila está vazia

		

	def peek(self):
	#retorna o primeiro valor da fila sem removê-lo
		if len(self) > 0:
			return self.primeiro.item
		raise IndexError ('Fila vazia.')  #Levanta um erro se a fila está vazia
		

	def __len__ (self):
		#len(fila) retorna o tamanho da fila
		return self._tamanho

	def __repr__ (self):
		if len(self) > 0:
			r = ''
			auxiliar = self.primeiro
			while auxiliar:
				r += str(auxiliar.item) + '\n\n'
				auxiliar = auxiliar.proximo
			return r

		raise IndexError ('Fila vazia.')

	def __str__(self):
		return self.__repr__()
