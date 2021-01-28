#Tarefa 5 - estrutura de dados (ple) 09/12/2020

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


def dijkstra(graph, origem, destino):  #calcula a menor distância do vértice de origem à qualquer outro vértice do grafo (se houver um caminho entre eles)
    #-----Essa parte faz origem.distanciaTotal valer zero-----
    origemVertex = graph.search(origem)

    if origemVertex == None:
        return print('O vértice de origem não está no grafo.')

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

    showPath(graph, origem, destino)


def showPath(graph, origem, destino):
    #Imprime o caminho da origem ao destino

    #Verifica se o vértice destino está no grafo
    vertex = graph.search(destino)
    if vertex is None:
        return print('O vértice de destino não está no grafo')

    if vertex.anterior is None:  #Verifica se existe um caminho entre origem e destino
        print('Não existe caminho entre [', origem, '] e [', destino, ']')

    else:  #Se houver caminho
        print('A distância de [', origem, '] até [', destino, '] é de:', vertex.distanciaTotal, 'Km')
        
        print('Caminho da origem até o destino:')

        #Coloca na lista caminho o percurso entre origem e destino
        caminho = [vertex.cidade]
        while vertex.anterior != None:
            caminho.append(vertex.anterior)
            vertex = graph.search(vertex.anterior)

        #Imprime o percurso
        tru = False
        for i in caminho[::-1]:
            if tru is True:
                print(' -> ', i, end='')
            else:
                print(i, end='')
                tru = True
        print()  #\n


def createVertex(conexoes):  #cria um vértice para caso não exista
    searchVertex = graph.search(conexoes)  #verifica o vértice que sera adicionado já está no grafo
    if searchVertex == None:  #se não está no grafo, é adicionado como um novo vértice
        vertex = Vertex(conexoes)
        graph.vertices.append(vertex)


graph = Graph()

dados = pd.read_csv('audomcitypairs-201912.csv', encoding='UTF-8')

option = int(input('Digite o número de vértices que deseja adicionar: '))

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

graph.printGraph()

origem = input('Digite o vértice de origem:').upper()
destino = input('Digite o vértice de destino:').upper()
print()  #\n

dijkstra(graph, origem, destino)