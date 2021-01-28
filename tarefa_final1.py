from tkinter import *
from tkinter.scrolledtext import *
from tkinter import messagebox
import pandas as pd
from appGrafo import GrafoWindow

class labelEntry(Frame):
	def __init__(self, meumaster):
		super().__init__(meumaster)
		self.meumaster = meumaster
		self.widgets()

	def widgets(self):
		#Cria labels com os nomes dos índices e uma entry para cada label
		self.idade_label = Label(self,
							text='Idade:').grid(row=2, column=0)
		self.idade_entry = Entry(self)
		self.idade_entry.grid(row=2, column=1)
		
		self.sexo_label = Label(self,
							text='Sexo:').grid(row=3, column=0)
		self.sexo_entry = Entry(self)
		self.sexo_entry.grid(row=3, column=1)
		
		self.tipoDor_label = Label(self,
							text='Tipo de dor no peito:').grid(row=4, column=0)
		self.tipoDor_entry = Entry(self)
		self.tipoDor_entry.grid(row=4, column=1)

		self.pressao_label = Label(self,
							text='Pressão arterial em repouso:').grid(row=5, column=0)
		self.pressao_entry = Entry(self)
		self.pressao_entry.grid(row=5, column=1)

		self.colesterol_label = Label(self,
							text='Colesterol sérico:').grid(row=6, column=0)
		self.colesterol_entry = Entry(self)
		self.colesterol_entry.grid(row=6, column=1)

		self.glicemia_label = Label(self,
							text='Glicemia de jejum:').grid(row=7, column=0)
		self.glicemia_entry = Entry(self)
		self.glicemia_entry.grid(row=7, column=1)

		self.eletro_label = Label(self,
							text='Resultados do eletrocardiograma em repouso:').grid(row=8, column=0)
		self.eletro_entry = Entry(self)
		self.eletro_entry.grid(row=8, column=1)

		self.freq_label = Label(self,
							text='Máxima frequencia cardiaca alcançada:').grid(row=9, column=0)
		self.freq_entry = Entry(self)
		self.freq_entry.grid(row=9, column=1)

		self.angina_label = Label(self,
							text='Angina induzida por esforço:').grid(row=10, column=0)
		self.angina_entry = Entry(self)
		self.angina_entry.grid(row=10, column=1)

		self.desnivelST_label = Label(self,
							text='Desnivel no intervalo ST:').grid(row=11, column=0)
		self.desnivelST_entry = Entry(self)
		self.desnivelST_entry.grid(row=11, column=1)

		self.inclinacaoST_label = Label(self,
							text='Inclinação do pico de segmento ST:').grid(row=12, column=0)
		self.inclinacaoST_entry = Entry(self)
		self.inclinacaoST_entry.grid(row=12, column=1)

		self.numVasos_label = Label(self,
							text='Número de principais vasos sanguineos:').grid(row=13, column=0)
		self.numVasos_entry = Entry(self)
		self.numVasos_entry.grid(row=13, column=1)

		self.talassemia_label = Label(self,
							text='Presença de talassemia:').grid(row=14, column=0)
		self.talassemia_entry = Entry(self)
		self.talassemia_entry.grid(row=14, column=1)

		self.doencaCardi_label = Label(self,
							text='Presença de doença cardiaca:').grid(row=15, column=0)
		self.doencaCardi_entry = Entry(self)
		self.doencaCardi_entry.grid(row=15, column=1)	

	def dicionario(self):
		#retorna um dicionario com os dados que estão nas entrys
		self.dicio = {'Idade': float(self.idade_entry.get()), 
	    	     	  'Sexo': float(self.sexo_entry.get()),
				   	  'Dor no peito' : float(self.tipoDor_entry.get()),
				 	  'Pressão arterial em repouso': float(self.pressao_entry.get()),
				 	  'Colesterol sérico': float(self.colesterol_entry.get()),
				 	  'Glicemia de jejum': float(self.glicemia_entry.get()),
				 	  'Eletrocardiograma em repouso': float(self.eletro_entry.get()),
				 	  'Máx. freq. cardiaca': float(self.freq_entry.get()),
				 	  'Angina ind. por esforço': float(self.angina_entry.get()),
				 	  'Desniv. do intervalo ST': float(self.desnivelST_entry.get()),
				 	  'inclinação do seg. ST': float(self.inclinacaoST_entry.get()),
				 	  'num. de princ. vasos sang.' : float(self.numVasos_entry.get()),
				 	  'Presença de talassemia': float(self.talassemia_entry.get()),
				 	  'Presença de doença cardiaca': float(self.doencaCardi_entry.get())}
		return self.dicio

class radioB(Frame):
	#usado nas funções removerItem e pesquisar (arvore)
	def __init__(self, meumaster):
		super().__init__(meumaster)
		self.meumaster = meumaster
		self.option = IntVar()
		self.radiobuttons()

	def radiobuttons(self):
		#Cria radiobuttons com os nome dos índices
		idd = Radiobutton(self, text='Idade', variable= self.option, value=1)
		idd.grid(row=2, column=1)

		idd.select()

		sexo = Radiobutton(self, text='Sexo', variable=self.option, value=2)
		sexo.grid(row=3,column=1)

		tipoDor = Radiobutton(self, text='Tipo de dor no peito', variable=self.option, value=3)
		tipoDor.grid(row=4,column=1)

		pressao = Radiobutton(self, text='Pressão arterial em repouso', variable=self.option, value=4)
		pressao.grid(row=5,column=1)

		colesterol = Radiobutton(self, text='Colesterol sérico', variable=self.option, value=5)
		colesterol.grid(row=6,column=1)

		glicemia = Radiobutton(self, text='Glicemia de jejum', variable=self.option, value=6)
		glicemia.grid(row=7,column=1)

		eletro = Radiobutton(self, text='Resultado do eletrocardiograma', variable=self.option, value=7)
		eletro.grid(row=8,column=1)

		freq = Radiobutton(self, text='Máxima frequencia cardiaca', variable=self.option, value=8)
		freq.grid(row=9,column=1)

		angina = Radiobutton(self, text='Angina induzida por esforço', variable=self.option, value=9)
		angina.grid(row=10,column=1)

		desnivelST = Radiobutton(self, text='Desnivel do intervalo ST', variable=self.option, value=10)
		desnivelST.grid(row=11,column=1)

		inclinacaoST = Radiobutton(self, text='Inclinacao do segmento ST', variable=self.option, value=11)
		inclinacaoST.grid(row=12,column=1)

		numVasos = Radiobutton(self, text='Num. de princ. vasos sang.', variable=self.option, value=12)
		numVasos.grid(row=13,column=1)

		talassemia = Radiobutton(self, text='Presença de talassemia', variable=self.option, value=13)
		talassemia.grid(row=14,column=1)

		doencaCardi = Radiobutton(self, text='Presença de doenca cardiaca', variable=self.option, value=14)
		doencaCardi.grid(row=15,column=1)

	def optionSelected(self):
		#retorna a opção selecionada
		return self.option.get()

def clearScreen(frame):
	#Limpa a tela sem tirar o menu
	for i in frame.winfo_children():  #Destroi todos os widgets, com exceção do menu
			if 'menu' in str(i):
				pass
			else:
				i.destroy()

def popup(mensagem):
	#cria uma messagebox sem título que mostra a mensagem passada no parâmetro da função
	messagebox.showinfo(message=mensagem)

def lista():  #fazer uma função para os botões?
	def printList():  #ok^^
		#Exibe a lista na tela
		clearScreen(novaJanela)  #Limpa a tela

		#Cria um scrolledText e o coloca na tela
		listaText = ScrolledText(novaJanela, wrap=WORD, width=40, height=17)
		listaText.grid(row=0, column=0)

		#Insere o conteúdo da lista no scrolledText
		listaText.insert('insert', 'Itens da lista:\n\n')
		listaText.insert('insert', str(trf1.lista))

	def clearLabelFrame(texto):  #ok^^
		#Limpa a tela e coloca um label com o texto do parâmetro e um objeto labelEntry na tela
		#Usada nas funções de inserir, editar item e remover item

		clearScreen(novaJanela)  #Limpa a tela
		label = Label(novaJanela, text=texto)  #Cria um label com a string passada como parametro
		label.grid(row=0, columnspan=2, sticky='we')  #Coloca o label na tela

		frame = labelEntry(novaJanela)  #cria um objeto com os labels e entrys que correspondem aos indices dos itens
		frame.grid()  #Coloca o objeto na tela
		return frame

	def inserirComeco():  #ok^^
		#Insere itens no começo da lista
		def putOnList(frame):  #Inserção na lista
			newItem = trf1.Pessoa(frame.dicionario())  #Cria um objeto do tipo pessoa com os dados das entrys
			trf1.lista.insert(0, newItem)  #Coloca o novo item no começo da lista
			popup('Item inserido na lista.')

		#Limpa a tela e coloca os labels e entrys nela
		frame = clearLabelFrame('Digite os dados que você deseja inserir na lista:')

		#--------botẽs--------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: putOnList(frame))
		confirmar.grid(row=1, column=1, sticky = 's') #sticky coloca o botão em baixo

		voltar = Button(novaJanela,
						text='Voltar',
						command=lambda: printList())  #Limpa a tela e coloca a lista atualizada nela
		voltar.grid(row=1, column=1, sticky = 'n')  #sticky coloca o botão em cima
		#---------------------

	def inserirFinal():  #ok^^
		#Insere itens no final da lista

		def putOnList(frame):  #Inserção na lista
			newItem = trf1.Pessoa(frame.dicionario())  #Cria um objeto do tipo pessoa com os dados das entrys
			trf1.lista.append(newItem)  #Adiciona o novo item no final da lista 
			popup('Item inserido na lista.')

		#Limpa a tela e coloca os labels e entrys nela
		frame = clearLabelFrame('Digite os dados que você deseja inserir na lista:')

		#--------botẽs--------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: putOnList(frame))
		confirmar.grid(row=1, column=1, sticky = 's')  #sticky coloca o botão em baixo

		voltar = Button(novaJanela,
						text='Voltar',
						command=lambda: printList()) #Limpa a tela e coloca a lista atualizada nela
		voltar.grid(row=1, column=1, sticky = 'n')  #sticky coloca o botão em cima
		#---------------------

	def inserirMeio():  #ok^^?
		#Insere itens na posição desejada

		def putOnList(frame):  #Inserção na lista
			newItem = trf1.Pessoa(frame.dicionario())  #Cria um objeto do tipo pessoa com os dados das entrys 
			posicao = int(posi.get()) - 1  #Posição em que o item será iserido

			trf1.lista.insert(posicao, newItem)  #Insere newItem na posição posicao
			popup('Item inserido na lista.')

		#Limpa a tela e coloca os labels e entrys nela
		frame = clearLabelFrame('Digite os dados que você deseja inserir na lista:')

		#Frame com label e entry pra essa parte ficar alinhada na tela
		framePosicao = Frame(novaJanela)
		#Não consegui alinhar o label com a entry.-.
		label1 = Label(framePosicao,
					   text='Posição em que o novo item será inserido:\n').grid(row=0, column=0)
		posi = Entry(framePosicao)  #entry para a posição que o item será inserido na lista
		posi.grid(row=0, column=1)

		framePosicao.grid(row=3, column=0)  #Coloca o frame na tela

		#--------botẽs--------
		voltar = Button(novaJanela,
						text='Voltar',
						command=lambda: printList())  #Limpa a tela e coloca a lista atualizada nela
		voltar.grid(row=4, column=0, sticky='w')  #sticky coloca o botão à esquerda

		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: putOnList(frame))
		confirmar.grid(row=4, column=0, sticky='e')  #sticky coloca o botão à direita
		#---------------------

	def editItem():  #ok^^
		#Edita um item específico, caso hajam dois iguais edita o que tem menor índice

		def acharIndice(frame):  #Acha o índice do item que será editado
			def substituicao(frame, posicao):  #Edição
				newItem=trf1.Pessoa(frame.dicionario())  #cria um objeto pessoa com os dados do novo item
				trf1.lista[posicao] = newItem  #substitui os valores na lista
				popup('Item editado.')

			oldItem = trf1.Pessoa(frame.dicionario())  #Cria um objeto pessoa com os dados do item que será editado
			posicao = trf1.lista.index(oldItem)  #acha o índice do item que será editado

			#Limpa a tela e coloca os labels e entrys nela
			frame1=clearLabelFrame('O que você deseja colocar no lugar deste item?')

			#--------botẽs--------
			confirmar = Button(novaJanela,
							   text='Confirmar',
							   command=lambda: substituicao(frame1, posicao))
			confirmar.grid(row=1, column=1, sticky = 's')

			voltar = Button(novaJanela,
							text='Voltar',
							command=lambda: printList())  #Limpa a tela e coloca a lista atualizada nela
			voltar.grid(row=1, column=1, sticky = 'n')

		#Limpa a tela e coloca os labels e entrys nela
		frame = clearLabelFrame('Qual item você deseja editar?')
		#--------botẽs--------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: acharIndice(frame))
		confirmar.grid(row=1, column=1, sticky = 's')

		voltar = Button(novaJanela,
						text='Voltar',
						command=lambda: printList())  #Limpa a tela e coloca a lista atualizada nela
		voltar.grid(row=1, column=1, sticky = 'n')
		#---------------------

	def editPosition():  #(funciona) VER A POSIÇÃO DOS BOTÕES
		#Edita o item na posição digitada
		def editarPosicao(frame):  #edição 
			posicao = int(entry.get()) - 1  #posição do item
			trf1.lista[posicao] = trf1.Pessoa(frame.dicionario())  #substitui o valor na posição
			popup('Item editado')

		clearScreen(novaJanela)  #Limpa a tela

		label = Label(novaJanela, text='Digite a posição do item que você deseja editar.')
		label.grid()
		entry = Entry(novaJanela)
		entry.grid()

		label1 = Label(novaJanela, text='O que você deseja colocar nesta posição?')
		label1.grid(row=3, columnspan=2, sticky='we')

		#Coloca os labels e entrys na tela
		frame = labelEntry(novaJanela)
		frame.grid()

		#--------botẽs--------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: editarPosicao(frame))
		confirmar.grid(row=4, column=1, sticky = 's')

		voltar = Button(novaJanela,
						text='Voltar',
						command=lambda: printList())  #Limpa a tela e coloca a lista atualizada nela
		voltar.grid(row=4, column=1, sticky = 'n')
		#---------------------

	def removerItem():  #ok^^
		#Remove um item específico da lista

		def removeI(frame):  #Remoção
			trf1.lista.removeItem(trf1.Pessoa(frame.dicionario()))  #Remove o item desejado
			popup('Item removido')

		#Limpa a tela e coloca os labels e entrys nela
		frame = clearLabelFrame('Que item você deseja remover?')

		#--------botẽs--------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: removeI(frame))
		confirmar.grid(row=1, column=1, sticky = 's')

		voltar = Button(novaJanela,
						text='Voltar',
						command=lambda: printList())  #Limpa a tela e coloca a lista atualizada nela
		voltar.grid(row=1, column=1, sticky = 'n')
		#---------------------

	def removerPosicao():#(funciona) VER A POSIÇÃO DOS BOTÕES
		#Remove o item da posição digitada

		def removeP(posicao):  #Remoção
			trf1.lista.removeIndice(posicao-1)  #Remove o item no índice posicao-1
			popup('Item removido.')

		clearScreen(novaJanela)  #Limpa a tela

		label = Label(novaJanela, text='Digite a posição do item que você deseja remover.')
		label.grid()
		entry = Entry(novaJanela)
		entry.grid()

		confirmar = Button(novaJanela, text='confirmar', command= lambda:removeP(int(entry.get())))
		confirmar.grid()

		voltar = Button(novaJanela, text='Voltar', command=lambda:printList())  #Limpa a tela e coloca a lista atualizada nela
		voltar.grid()

	import tarefa1 as trf1
	novaJanela = Toplevel()  #Cria uma nova janela
	novaJanela.title('Lista encadeada')

	#--------menu--------
	menu = Menu(novaJanela)

	menuInserir = Menu(menu, tearoff=0)
	menuInserir.add_command(label='Inserir no começo', command=lambda:inserirComeco())
	menuInserir.add_command(label='Inserir numa posiçao específica', command=lambda:inserirMeio())
	menuInserir.add_command(label='Inserir no final', command=lambda:inserirFinal())

	menu.add_cascade(label='Inserir', menu=menuInserir)

	menuEditar = Menu(menu, tearoff=0)
	menuEditar.add_command(label='Editar item específico', command=lambda:editItem())
	menuEditar.add_command(label='Editar item numa posiçao específica', command=lambda:editPosition())

	menu.add_cascade(label='Editar', menu=menuEditar)

	menuRemover = Menu(menu, tearoff=0)
	menuRemover.add_command(label='Remover item específico', command=lambda:removerItem())
	menuRemover.add_command(label='Remover item numa posiçao específica', command=lambda:removerPosicao())

	menu.add_cascade(label='Remover', menu=menuRemover)

	novaJanela.config(menu=menu)
	#--------------------

	printList()#Mostra a lista
	#--------Fim da função lista--------

def fila():  #ok^^
	def show(mostrar):
		#checkbutton do menu
		#mostra a fila inteira

		clearScreen(novaJanela)  #Limpa a tela

		if mostrar.get():  #checkbutton selecionado
			#Cria um scrolledtext
			filaInteira = ScrolledText(novaJanela, wrap=WORD, width=40, height=17)

			#Insere os itens da fila no scrolledtext
			filaInteira.insert('insert', 'Todos itens da fila:\n\n')
			filaInteira.insert('insert', str(trf3.fila))

			filaInteira.grid(row=0, column=1)  #Coloca o scrolledtext na tela

		else:  #checkbutton não selecionado
			peekFila()  #Limpa a tela e mostra o primeiro item da fila

	def peekFila():  #OK^^
		#Mostra o primeiro item da fila
		clearScreen(novaJanela)  #Limpa a tela  

		#Cria um scrolledtext e o coloca na tela
		asdf = ScrolledText(novaJanela, wrap=WORD, width=40, height=17)
		asdf.grid(row=0, column=0)

		#Insere o primeiro item da fila no scrolledtext
		asdf.insert('insert', 'Primeiro item da fila:\n\n')
		asdf.insert('insert', str(trf3.fila.peek()))

	def put1():  #ok^^
		#Adiciona um itens no final da fila

		def putOnQueue(frame):  #Inserção
			#Cria um objeto do tipo pessoa com o novo item
			newItem = frame.dicionario()
			newItem = trf3.Pessoa(newItem)

			trf3.fila.put(newItem)  #Insere newItem no final da fila

			popup('Item inserido na fila.')

		clearScreen(novaJanela)  #Limpa a tela

		label = Label(novaJanela,
					  text='Digite os dados que você deseja inserir na fila:').grid(row=1, columnspan=2, sticky='we')
		
		#Coloca os labels que correspondem aos indices dos itens e entrys na tela
		frame = labelEntry(novaJanela)
		frame.grid()

		#--------Botões--------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: putOnQueue(frame))
		confirmar.grid(row=2, column=1, sticky = 's')

		voltar = Button(novaJanela,
						text='Voltar',
						command=lambda: peekFila())  #Limpa a tela e mostra o primeiro item da fila
		voltar.grid(row=2, column=1, sticky = 'n')
		#----------------------
		
	def get1():  #OK^^
		#Remove o primeiro item da fila
		trf3.fila.get()

		#atualiza a tela
		if mostrar.get():  #Se mostrar a fila inteira estiver selecionado
			show(mostrar)  #Limpa a tela e mostra a fila inteira
		else:
			peekFila()  #Limpa a tela e mostra o primeiro item da fila

		popup('Item removido da fila.')

	import tarefa3_2 as trf3

	novaJanela = Toplevel()  #Cria uma nova janela
	novaJanela.title('Fila')

	#--------menu--------
	menu = Menu(novaJanela)

	menuAction = Menu(menu, tearoff=0)
	menuAction.add_command(label='Inserir item', command = lambda: put1())
	menuAction.add_command(label='Remover o primeiro da fila', command = lambda: get1())
	menu.add_cascade(label='Ações', menu=menuAction)

	mostrar = IntVar()
	menu.add_checkbutton(label='Mostrar fila inteira', offvalue=0, onvalue=1, variable=mostrar, command= lambda: show(mostrar))

	novaJanela.config(menu=menu)
	#--------------------

	peekFila()  #Limpa a tela e mostra o primeiro item da fila

	#--------Fim da função fila--------
	
def pilha():  #ok^^(Falta fazer a parte de mostrar a fila inteira)
#					Fazer do mesmo jeito que a de fila.
	def push1(): #ok^^
		#Adiciona um item no topo da pilha

		def putOnStack(frame):  #Inserção
			#Cria um objeto do tipo pessoa com os dados do novo item
			newItem = frame.dicionario()
			newItem = trf2.Pessoa(newItem)

			trf2.pilha.push(newItem)  #Adicioana o novo item no topo da pilha
			popup('Item inserido na pilha.')

		clearScreen(novaJanela)  #Limpa a tela

		label = Label(novaJanela,
					  text='Digite os dados que você deseja inserir na pilha:').grid(row=1, columnspan=2, sticky='we')
		
		#Coloca os labels que correspondem aos indices dos itens e entrys na tela
		frame = labelEntry(novaJanela)
		frame.grid()

		#-------botões-------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: putOnStack(frame))
		confirmar.grid(row=2, column=1, sticky = 's')

		voltar = Button(novaJanela,
						text='Voltar',
						command=lambda: peekPilha())  #Limpa a tela e mostra o primeiro item da fila
		voltar.grid(row=2, column=1, sticky = 'n')
		#--------------------

	def pop1(): #OK^^
		#Remove o primeiro item da pilha
		trf2.pilha.pop()  #Remoção
		
		#lembrar de modificar essa parte 
		#se for feita a função de mostrar a fila inteira
		#usar a função get1 de fila como exemplo
		peekPilha()  #limpa a tela e mostra o topo da pilha
		popup('Item removido.')

	def peekPilha():  #ok^^
		#Limpa a tela e mostra o primeiro item da pilha

		clearScreen(novaJanela)  #Limpa a tela

		#Cria um scrolledtext e o coloca na tela
		asdf = ScrolledText(novaJanela, wrap=WORD, width=40, height=17)
		asdf.grid(row=0, column=0)

		#Insere o primeiro item da pilha no scrolledtext
		asdf.insert('insert', 'Primeiro item da pilha:\n\n')
		asdf.insert('insert', str(trf2.pilha.peek()))

	import tarefa2 as trf2

	novaJanela = Toplevel()  #Cria uma nova janela
	novaJanela.title('Pilha')

	#--------menu--------
	menu = Menu(novaJanela)

	menuAction = Menu(menu, tearoff=0)
	menuAction.add_command(label='Inserir item', command = lambda: push1())
	menuAction.add_command(label='Remover item', command = lambda: pop1())

	menu.add_cascade(label='Ações', menu=menuAction)

	novaJanela.config(menu=menu)
	#--------------------

	peekPilha()  #mostra o primeiro item

	#--------Fim da função pilha--------

def arvore():  #ok^^
	def show(option):
		#Mostra na tela a opção escolhida no radiobutton do menu

		if option.get() == 1:
			showIdade()

		elif option.get() == 2:
			showPressao()

		elif option.get() == 3:
			showFreq()

	def showIdade():  #ok^^
		#Mostra os itens ordenados pela idade
		clearScreen(novaJanela)  #Limpa a tela

		#Cria um scrolledText e o coloca na tela
		textIdade = ScrolledText(novaJanela, wrap=WORD, width=40, height=17)
		textIdade.grid(row=0, column=0)

		#Insere os itens da árvore ordenada pela idade no scrolledtext
		textIdade.insert('insert', 'Itens ordenados pela idade:\n\n')
		lista = []
		trf4.arvore.EMordem(lista = lista)
		for i in lista:
			textIdade.insert('insert', i)

	def showPressao():  #ok^^
		#Mostra os itens ordenados pela pressão
		clearScreen(novaJanela)  #Limpa a tela 

		#Cria um scrolledText e o coloca na tela
		textPressao = ScrolledText(novaJanela, wrap=WORD, width=40, height=17)
		textPressao.grid(row=0, column=0)

		#Insere os itens da árvore ordenada pela pressão no scrolledtext
		textPressao.insert('insert', 'Itens ordenados pela pressão arterial:\n\n')
		lista = []
		trf4.arvoreP.EMordem(lista = lista)
		for i in lista:
			textPressao.insert('insert', i)

	def showFreq():  #ok^^
		#Mostra os itens ordenados pela frequencia
		clearScreen(novaJanela)  #Limpa a tela

		#Cria um scrolledText e o coloca na tela
		textFreq = ScrolledText(novaJanela, wrap=WORD, width=40, height=17)
		textFreq.grid(row=0, column=0)

		#Insere os itens da árvore ordenada pela frequencia no scrolledtext
		textFreq.insert('insert', 'Itens ordenados pela frequencia cardiaca:\n\n')
		lista = []
		trf4.arvoreF.EMordem(lista = lista)
		for i in lista:
			textFreq.insert('insert', i) 

	def inserir1():  #ok^^
		#Insere itens nas três árvores

		def putOnTree(frame):  #inserção

			#Cria um objeto do tipo pessoa com o novo item 
			newItem = frame.dicionario()
			newItem = trf4.Pessoa(newItem)


			trf4.arvore.inserir(newItem, 1)  #Insere o item na árvore ordenada por idade
			trf4.arvoreP.inserir(newItem, 4)  #Insere o item na árvore ordenada por pressao
			trf4.arvoreF.inserir(newItem, 8)  #insere o item na arvore ordenada pro frequencia

			popup('Item inserido na árvore.')

		clearScreen(novaJanela)  #Limpa a tela

		label = Label(novaJanela,
					  text='Digite os dados que você deseja inserir na árvore:').grid(row=1, columnspan=2, sticky='we')
		
		#Coloca os labels que correspondem aos indices dos itens e entrys na tela
		frame = labelEntry(novaJanela)
		frame.grid()

		#--------Botões--------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: putOnTree(frame))
		confirmar.grid(row=2, column=1, sticky = 's')

		voltarB = Button(novaJanela,
						text='Voltar',
						command=lambda: show(option))  #Limpa a tela e mostra a árvore selecionada
		voltarB.grid(row=2, column=1, sticky = 'n')
		#----------------------

	def pesquisar1():  #ok^^
		#Mostra na tela todos os itens que tem o valor desejado num campo específico

		def pesquisa(frame):  #pesquisa
			valor = float(entryValor.get())  #Valor que será pesquisado
			opcao = frame.optionSelected()  #Índice em que o valor será procurado

			clearScreen(novaJanela)  #Limpa a tela
			
			#Cria um scrolledtext e o coloca na tela
			textPesquisa = ScrolledText(novaJanela, wrap=WORD, width=40, height=17)
			textPesquisa.grid(row=0, column=0)

			#Insere os valores da pesquisa no scrolledtext
			textPesquisa.insert('insert', f'Itens com valor {valor} no índice {opcao}:\n\n')
			lista = []
			trf4.arvore.pesquisa(valor, campo=opcao, lista=lista)
			for i in lista:
				textPesquisa.insert('insert', str(i) + '\n\n')

			#------botão------
			botao = Button(novaJanela, text='voltar', command=lambda:show(option))  #Limpa a tela e mostra a árvore selecionada
			botao.grid(row=0, column=1, sticky='n')
			#------------------

		clearScreen(novaJanela)  #Limpa a tela

		labelValor = Label(novaJanela, text='Valor:', font='bold')
		labelValor.grid(row=0, column=0)

		entryValor = Entry(novaJanela)
		entryValor.grid(row=1, column=0, sticky='n')

		labelIndices = Label(novaJanela, text='Indice em que a pesquisa será feita:\n', font='bold')
		labelIndices.grid(row=0, column=1)

		#Insere radiobutons com os índices dos itens na tela
		frame = radioB(novaJanela)
		frame.grid(row=1, column=1)

		#--------Botões--------
		voltarB = Button(novaJanela,
						   text='Voltar',
						   command=lambda: show(option))  #limpa a tela e mostra a árvore selecionada
		voltarB.grid(row=2, column=0, sticky = 'we')

		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: pesquisa(frame))
		confirmar.grid(row=2, columnspan=2, sticky = 'we')
		#----------------------

	def removerValor():  #ok^^
		#Remover itens com um valor no compa escolhido

		def removeValor(frame):  #Remoção
			valor = float(entryValor.get()) #Valor que será removido
			opcao = frame.optionSelected()  #Indice selecionado no radiobutton

			#Coloca os itens que serão removidos na lista
			lista = []
			trf4.arvore.pesquisa(valor, campo=opcao, lista=lista)

			#Remove os itens
			for i in lista:
				trf4.arvore.remover_item(i,1)  #Remove da árvore ordenada por idade
				trf4.arvoreP.remover_item(i,4)  #Remove da árvore ordenada por pressão
				trf4.arvoreF.remover_item(i,8)  #Remove da árvore ordenada por frequencia

			show(option)  #Limpa a tela e mostra a árvore selecionada
			popup('Itens removidos.')

		clearScreen(novaJanela)  #Limpa a tela

		labelValor = Label(novaJanela, text='Valor:', font='bold')
		labelValor.grid(row=0, column=0)

		entryValor = Entry(novaJanela)
		entryValor.grid(row=1, column=0, sticky='n')

		labelIndice = Label(novaJanela, text='Remover itens com este valor no índice:\n', font='bold')
		labelIndice.grid(row=0, column=1)

		#Insere radiobutons com os índices dos itens na tela
		frame = radioB(novaJanela)
		frame.grid(row=1, column=1)

		#--------Botões--------
		voltarB = Button(novaJanela,
						   text='Voltar',
						   command=lambda: show(option))  #Limpa a tela e mostra a árvore selecionada
		voltarB.grid(row=2, column=0, sticky = 'we')

		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: removeValor(frame))
		confirmar.grid(row=2, column=1, sticky = 'we')
		#----------------------

	def removerItem():  #ok^^
		#Remove um item específico

		def removeItem(frame):  #Remoção
			#Cria um objeto do tipo pessoa com os dados do item que será removido
			item = frame.dicionario()
			item = trf4.Pessoa(item)

			#Remove o item das árvores
			trf4.arvore.remover_item(item,1)  #Remove o item da árvore ordenada por idade
			trf4.arvoreF.remover_item(item,4)  #Remove o item da árvore ordenada por frequencia
			trf4.arvoreP.remover_item(item,8)  #Remove o item da árvore ordenada por pressão

			show(option)  #Limpa a tela e mostra a árvore selecionada
			popup('Item removido.')

		clearScreen(novaJanela)  #Limpa a tela
		label = Label(novaJanela,
					  text='Digite os dados do item que você deseja remover.').grid(row=1, columnspan=2, sticky='we')
		
		#Coloca os labels que correspondem aos indices dos itens e entrys na tela
		frame = labelEntry(novaJanela)
		frame.grid()

		#--------Botões--------
		confirmar = Button(novaJanela,
						   text='Confirmar',
						   command=lambda: removeItem(frame))
		confirmar.grid(row=2, column=1, sticky = 's')

		voltarB = Button(novaJanela,
						text='Voltar',
						command=lambda: show(option))  #Limpa a tela e mostra a árvore selecionada
		voltarB.grid(row=2, column=1, sticky = 'n')
		#----------------------

	import tarefa4_3 as trf4

	novaJanela = Toplevel()  #Cria uma nova janela
	novaJanela.title('Árvore binaria')

	#--------menu--------
	menu = Menu(novaJanela)

	menuAction = Menu(menu, tearoff=0)
	menuAction.add_command(label='Inserir', command = lambda: inserir1())
	menuAction.add_command(label='Pesquisar', command = lambda: pesquisar1())

	menu.add_cascade(label='Ações', menu=menuAction)

	menuRemover = Menu(menuAction, tearoff=0)
	menuRemover.add_command(label='item específico', command=lambda:removerItem())
	menuRemover.add_command(label='itens com determinado valor num campo', command=lambda:removerValor())

	menuAction.add_cascade(label='Remover', menu=menuRemover)

	menuVisualizar1 = Menu(menu, tearoff=0)

	option = IntVar()

	menuVisualizar1.add_radiobutton(label= 'Odenado por idade', variable= option, value=1, command=lambda: show(option))
	menuVisualizar1.add_radiobutton(label= 'Ordenado por pressão', variable= option, value=2, command=lambda: show(option))
	menuVisualizar1.add_radiobutton(label= 'Ordenado por frequencia', variable= option, value=3, command=lambda: show(option))
	menu.add_cascade(label='Visualizar', menu=menuVisualizar1)

	novaJanela.config(menu=menu)
	#--------------------

	option.set(1)
	show(option)  #Mostra a árvore ordenada por idade
	#------fim da função arvore------


#---------Programa principal--------
root = Tk()
root.title('Trabalho Final')

#---------colocar a janela no meio da tela---------
#dimenções da janela
largura = 300
altura = 180

#resolução do sistema
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()

#posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#definir a geometry
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
#--------------------------------------------------

label = Label(root,
			  text='Selecione uma estrutura:',
			  anchor='center',
			  font='Helvetica 14 bold').grid(columnspan=2, sticky='we')

botao1 = Button(root,
				text='Lista encadeada',
				height=2,
				width=15,
				pady=5,
				#fg='#130f40',
				background='#78909C',
				command = lambda: lista()).grid(row=1, column=0)
botao2 = Button(root,
				text='Pilha',
				height=2,
				width=15,
				pady=5,
				background='#78909C',
				command = lambda: pilha()).grid(row=1, column=1)
botao3 = Button(root,
				text='Fila',
				height=2,
				width=15,
				pady=5,
				background='#78909C',
				command = lambda: fila()).grid(row=2, column=1)
botao4 = Button(root,
				text='Árvore binaria',
				height=2,
				width=15,
				pady=5,
				background='#78909C',
				command = lambda: arvore()).grid(row=2, column=0)
botao4 = Button(root,
				text='Grafo',
				height=2,
				width=15,
				pady=5,
				background='#78909C',
				command = lambda: GrafoWindow()).grid(row=3, column=0)
botao4 = Button(root,
				text='Sair',
				height=2,
				width=15,
				pady=5,
				background='#78909C',
				command = lambda: root.destroy()).grid(row=3, column=1)

root.mainloop()