from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pandas as pd
import math

class Vertex:
    def __init__(self, cidade):
        self.cidade = cidade
        self.visitado = False  #Mostra se o vértice foi visitado nas funções searchMinDistance e dijkstra
        self.anterior = None  #Usado nas funções dijkstra e showPath
        self.arestas = {}  #Dicionario que contem as conexões como chave e a distância como valor
        self.distanciaTotal = math.inf #infinito - usado nas funções dijkstra e searchMinDistance

    def __str__(self):
        #Repesentação str do vértice (vértice -> [conexões])
        tru = False
        string = self.cidade + ' -> '  #Adiciona a cidade do vertice na string

        for i in self.arestas.keys():  #Adiciona as chaves do dicionario arestas na string
            if tru is True:
                string += ', ' + i
            else:
                string += i
                tru = True

        return string

class Graph:
    def __init__(self):
        self.vertices = []  #Lista de vértices contidos no grafo
    
    def __str__(self):
        graph_string = ""
        for vertice in self.vertices:
            graph_string += vertice.__str__()
            graph_string += "\n"
        return graph_string


    def search(self, cidade):
        #Retorna o vértice procurado
        #Se o vertice não estiver no grafo retorna None
        for vertex in self.vertices:
            if cidade == vertex.cidade:
                return vertex
        return None

    def printGraph(self):
        #Imprime todos os vértices do grafo
        print('Cidade -> [Conexões]')
        for vertex in self.vertices:
            if len(vertex.arestas):
                print(vertex)
        print()

def searchMinDistance(vertices):  #retorna o vértice com menor distância
    
    maior = -1  #valor arbitrário utilizado na primeira comparação do for
    aux = None 

    for vertex in vertices:
        if vertex.distanciaTotal > maior and vertex.visitado == False and vertex.distanciaTotal != math.inf:
            maior = vertex.distanciaTotal
            aux = vertex
    return aux


def showPath(graph, origem, destino):
    #Imprime o caminho da origem ao destino
    string = ''
    
    #Verifica se o vértice destino está no grafo
    vertex = graph.search(destino)
    if vertex is None:
        string = 'O vértice de destino não está no grafo'
        return string
        
    if vertex.anterior is None:  #Verifica se existe um caminho entre origem e destino
        string = ('Não existe caminho entre [' + str(origem) +'] e [' + str(destino) +']')

    else:  #Se houver caminho
        string = ('A distância de [' + str(origem) +'] até [' + str(destino) + '] é de:'+ str(vertex.distanciaTotal) + 'Km\n')
        
        string += 'Caminho da origem até o destino:\n'

        #Coloca na lista caminho o percurso entre origem e destino
        caminho = [vertex.cidade]
        while vertex.anterior != None:
            caminho.append(vertex.anterior)
            vertex = graph.search(vertex.anterior)

        #Imprime o percurso
        tru = False
        for i in caminho[::-1]:
            if tru is True:
                string += (' -> ' + str(i))
                #print(' -> ', i, end='')
            else:
                string += str(i)
                #print(i, end='')
                tru = True
        string += '\n'
        #print()  #\n
        
    return string


def createVertex(conexoes):  #cria um vértice para caso não exista
    searchVertex = graph.search(conexoes)  #verifica o vértice que sera adicionado já está no grafo
    if searchVertex == None:  #se não está no grafo, é adicionado como um novo vértice
        vertex = Vertex(conexoes)
        graph.vertices.append(vertex)


graph = Graph()

dados = pd.read_csv('audomcitypairs-201912.csv', encoding='UTF-8')

##########################################################################
#################       Inicio da classe da janela       #################
##########################################################################

class GrafoWindow:
    def __init__(self):
        self.janelaGrafo = Tk()# Cria janela principal
        self.janelaGrafo.geometry('450x620')
        self.janelaGrafo.title('Grafo')

        # Cria três frames
        self.frame_1 = Frame(self.janelaGrafo)
        self.frame_2 = Frame(self.janelaGrafo)
        self.frame_3 = Frame(self.janelaGrafo)
        self.frame_4 = Frame(self.janelaGrafo)
        self.frame_5 = Frame(self.janelaGrafo)
        self.frame_6 = Frame(self.janelaGrafo)
        self.frame_7 = Frame(self.janelaGrafo)

        # cria um label e uma entry
        self.label1 = Label(self.frame_1, text='Digite o número de vértices que deseja adicionar')
        self.entrada = Entry(self.frame_1, width = 10)

        # coloca label1 e entrada no frame_1
        self.label1.pack(side='left')
        self.entrada.pack(side='left')

        # Criando os botões
        self.botao_confirmar = Button(self.frame_2, text='Confirmar', command= self.numeroVertices)
        self.botao_sair = Button(self.frame_2, text='Sair', command= self.janelaGrafo.destroy)

        # Coloca os botões no frame_2
        self.botao_confirmar.pack(side='left')
        self.botao_sair.pack(side='left')

        self.grafoText = ScrolledText(self.frame_3, wrap=WORD, width=40, height=17)
        self.grafoText.pack(side='left')

        self.label2 = Label(self.frame_4, text='Vértice de origem:')
        self.orig = Entry(self.frame_4, width = 10)
        self.label2.pack(side='left')
        self.orig.pack(side='left')

        self.label3 = Label(self.frame_5, text='Vértice de destino:')
        self.dest = Entry(self.frame_5, width = 10)
        self.label3.pack(side='left')
        self.dest.pack(side='left')

        self.botao_buscar = Button(self.frame_6, text='Buscar', command= self.dijkstra)
        self.botao_buscar.pack(side='left')

        self.resultadoBusca = ScrolledText(self.frame_7, wrap=WORD, width=40, height=10)
        self.resultadoBusca.pack(side='left')
        

        # Empacotando os frames na janela
        self.frame_1.pack()
        self.frame_2.pack()
        self.frame_3.pack()
        self.frame_4.pack()
        self.frame_5.pack()
        self.frame_6.pack()
        self.frame_7.pack()


        self.janelaGrafo.mainloop()


    def numeroVertices(self):
        option = int(self.entrada.get())
        i = 0
        while i < option:
            # data[0] = Cidade / data[1] = Conexão / data[6] = distância entre cidade e conexão
            data = dados.iloc[i]  #adiciona linha a linha na ordem em que está no arquivo
            
            searchVertex = graph.search(data[0])  #Procura o vértice data[0] no grafo

            if searchVertex != None:  #se o vértice já está no grafo, só sua conexão é adicionada
                searchVertex.arestas[data[1]] = data[6]
                createVertex(data[1])
            else:  #se não estiver cria um novo vértice
                vertex = Vertex(data[0])
                vertex.arestas[data[1]] = data[6]
                graph.vertices.append(vertex)  #Adiciona ao grafo
                createVertex(data[1])

            i += 1

        #self.grafoText["text"] = str(graph)
        self.grafoText.insert(END ,str(graph))

#----------------------FIM numeroVertices-------------------------------------


    def dijkstra(self):  #calcula a menor distância do vértice de origem à qualquer outro vértice do grafo (se houver um caminho entre eles)
        #graph
        origem = str(self.orig.get())
        destino = str(self.dest.get())
        #-----Essa parte faz origem.distanciaTotal valer zero-----
        origemVertex = graph.search(origem)

        if origemVertex == None:
            self.resultadoBusca.insert(END , 'O vértice de origem não está no grafo.')
            #return print('O vértice de origem não está no grafo.')

        else:  #Se o vértice origem está no grafo:
            origemVertex.distanciaTotal = 0
        #---------------------------------------------------------

        i = 0
        while i < len(graph.vertices):  
        #sempre irá pegar o vértice de origem na primeira iteração 
        #pois, nesta iteração, ele é o único tem distanciaTotal != math.inf
            
            currentVertex = searchMinDistance(graph.vertices) #Vértice em que a busca ocorre
            
            if currentVertex is None:
                break

            currentVertex.visitado = True  #Marca o vértice como visitado

            for conectVertex in currentVertex.arestas.keys():  
            #Verifica a distância entre o vértice atual e suas conexões
            #se o valor for menor o vértice anterior e a distância são atualizados

                vertex = graph.search(conectVertex)  #Cada vertice conectado ao currentVertex
                    
                if vertex.distanciaTotal > currentVertex.distanciaTotal + currentVertex.arestas[vertex.cidade]:
                    vertex.distanciaTotal = currentVertex.distanciaTotal + currentVertex.arestas[vertex.cidade]
                    vertex.anterior = currentVertex.cidade

                i += 1

        self.resultadoBusca.insert(END , showPath(graph, origem, destino))
        #showPath(graph, origem, destino)