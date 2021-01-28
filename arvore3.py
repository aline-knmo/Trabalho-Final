class Node:
	"""Nós da árvore binária"""
	def __init__(self,item):
		self.item = item
		self.esquerda = None
		self.direita = None

	def __str__ (self):
		#print(Node) imprime o valor de item
		return str(self.item)


class ArvoreBinaria:
	def __init__(self, item = None):
		#Cria uma árvore
		if item:  #Se algum item for passado a raíz da árvore é o item
			novo = Node(item)
			self.raiz = novo
		else:  #Se nenhum item for passado a raíz é None
			self.raiz = None

	def EMordem (self, arv=None, lista=None):
		#Percorre a árvore em ordem (in order)
		if arv is None:
			#Se o primeiro nó da travessia não for especificado
			#a travessia começa pela raiz.
			arv = self.raiz

		if arv.esquerda:  #Se tem filho à esquerda
			#chama a função recurcivamente com o filho como parametro
			self.EMordem(arv.esquerda, lista)
		
		if lista is not None:
			lista.append(str(arv) + '\n\n')
		elif lista is None:
			print (arv, '\n')
		
		if arv.direita:  #Se tem filho à direita
			#chama a função recurcivamente com o filho como parametro
			self.EMordem(arv.direita, lista)

	def inserir(self, item, campo=1):
		"""Insere o valor item, ordenado pelo índice campo, na árvore."""

		parente = None
		auxiliar = self.raiz
		while auxiliar:  #Acha o nó pai do item que será inserido
			parente = auxiliar
			if float(item[campo]) < float(auxiliar.item[campo]):
				auxiliar = auxiliar.esquerda
			else:
				auxiliar = auxiliar.direita

		#Insersão do item na árvore
		if parente is None:  #Árvore vazia
			self.raiz = Node(item)
		elif float(item[campo]) < float(parente.item[campo]):
			parente.esquerda = Node(item) 
		else:
			parente.direita = Node(item)

	def pesquisa(self, valor, campo=1, no='raiz', lista = None):
		#Procura todos os itens que tem valor no campo campo.
		#Se uma lista for especificada os itens são armazenados nela,
		#caso contrario os itens são imprimidos na tela

		if no == 'raiz':  #Se nenhuma subarvore for especificada a pesquisa começa da raíz
			no = self.raiz

		if no is None:  
			return no

		#Travessia em ordem.
		if no.esquerda:  #Se tem filho à esquerda
			#chama a função recurcivamente com o filho como parametro
			self.pesquisa(valor, campo, no.esquerda, lista)

		if no.item[campo] == valor:
			if lista is not None:
				lista.append(no.item)
			else:
				print (no, '\n')

		if no.direita:  #Se tem filho à direita
			#chama a função recurcivamente com o filho como parametro
			self.pesquisa(valor, campo, no.direita, lista)

	def min(self, node='raiz'):
		#Retorna o item do nó mais à esquerda (com menor valor) da árvore
		
		if node == 'raiz':  #Se nenhuma subarvore for especificada começa da raíz
			node = self.raiz
		while node.esquerda:  #Enquanto houverem filhos à esquerda
			node = node.esquerda
		return node.item  

	def remover_item(self, valor, campo=1 , node='raiz'):
		#funfa não -> não remove a raíz quando a raíz só tem um filho ou quando a árvore só tem a raíz
		#Remove um nó especifico da árvore

		if node == 'raiz':  #Se nenhuma subarvore for especificada começa da raíz
			node = self.raiz

		#Quando chega numa folha e o item não é encontrado
		#ou quando a árvore está vazia
		#a função é chamada com node=None
		if node is None:
			return node

		if valor == node.item:  #Remoção do nó
			if node.esquerda is None:  #Se o nó tem filho à direita ou é uma folha
				#Se o nó for uma folha node.direita é None
				return node.direita
			elif node.direita is None:  #Se o nó tem filho à esquerda
				return node.esquerda
			else:  #Se o nó tem dois filhos
				troca = self.min(node.direita)  #Nó da subárvore à direita que tem o menor valor
				node.item = troca  #O nó passa ter o menor valor de sua subárvore à direita

				#Remove o nó troca da subárvore a direita
				node.direita = self.remover_item(troca, campo, node.direita)
		
		#Acha o nó que será removido
		if float(valor[campo]) < float(node.item[campo]):
			node.esquerda = self.remover_item(valor, campo, node.esquerda)
		else:
			node.direita = self.remover_item(valor, campo, node.direita)

		return node