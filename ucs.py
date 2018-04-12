import  os, sys, copy
import time
import timeit
import numpy as np
from icecream import ic
import heapq


class Node:
    state = ()
    parent = None
    action = ""
    path_cost = 0
    def __lt__(self, other):
        return self.path_cost < other.path_cost

class Ids:
    def __init__(self):
        self.mapObj = {}
        self.estado_inicial = ()
        self.estado_final = ()
        self.visitados = set()
        self.movimento = ['LU', 'LD', 'RU', 'RD','L','R', 'U', 'D']
        self.result=[]

    def ehObjetivo(self, node):
        if node.state == self.estado_final:
            return True

    def acaoPermitida(self, action, node):
        #ic(node.state[1])
        if action == 'L' and node.state[1]-1 >= 0:
            return (node.state[0], node.state[1]-1, 1)
        elif action == 'R' and node.state[1]+1 <= self.mapObj["width"]-1:
            return (node.state[0], node.state[1]+1, 1)
        elif action == 'U' and node.state[0]-1 >= 0:
            return (node.state[0]-1, node.state[1], 1)
        elif action == 'D' and node.state[0]+1 <= self.mapObj["height"]-1:
            return (node.state[0]+1, node.state[1], 1)
        elif action == 'LU' and node.state[1]-1 >= 0 and node.state[0]-1 >= 0:
            return (node.state[0]-1, node.state[1]-1, 1.5)
        elif action == 'LD' and node.state[1]-1 >= 0 and node.state[0]+1 <= self.mapObj["height"]-1:
            return (node.state[0]+1, node.state[1]-1, 1.5)
        elif action == 'RU' and node.state[1]+1 <= self.mapObj["width"]-1 and node.state[0]-1 >= 0:
            return (node.state[0]-1, node.state[1]+1, 1.5)
        elif action == 'RD' and node.state[1]+1 <= self.mapObj["width"]-1 and node.state[0]+1 <= self.mapObj["height"]-1:
            return (node.state[0]+1,node.state[1]+1, 1.5)
        return False

    def ids_pilha(self, node, depth):
        heap = []
        heapq.heappush(heap,node)
        while len(heap)>0:
            ic(len(heap))
            node =heapq.heappop(heap)
            self.visitados.add(node.state)
            if (self.ehObjetivo(node)):
                return node
            for action in self.movimento:
                afterState = self.acaoPermitida(action, node)
                if afterState:
                    if self.mapObj['map'][afterState[0], afterState[1]]!=1:
                        if not ((afterState[0], afterState[1]) in self.visitados):
                            no = Node()
                            no.state = (afterState[0], afterState[1])
                            no.action = action
                            no.parent = node
                            no.path_cost= node.path_cost+afterState[2]
                            heapq.heappush(heap,no)
        return False
            #if(afterState):

    def produzCaminho(self, node):
        while node != None:
            self.result.append(node.state)
            node = node.parent

    def busca_ids(self):
        inicial = Node()
        inicial.state = self.estado_inicial
        inicial.parent = None
        inicial.action = ""
        inicial.path_cost = 0
        res = self.ids_pilha(inicial, 0)
        if res:
            self.produzCaminho(res)
            self.result.reverse()
            print(self.result)
            print("passos:", len(self.result))
        else:
            print("nao achou")

    def load_map(self, filename, estado_inicial, estado_final):
        assert os.path.exists(filename), 'Cannot find the level file: %s' %(filename)
        mapFile = open(filename, 'r')
        content = mapFile.readlines() + ['\r\n']
        mapFile.close()
        height = int(content[1][7:-1])
        width = int(content[2][6:-1])
        self.mapObj['height'] =int(height)
        self.mapObj['width'] = int(width)
        ic(self.mapObj['width'])
        map = np.zeros((height, width))
        mapString = content[4:]
        #ic(mapString)
        ic(height)
        ic(width)
        for i in range(height):
            for j in range(width):

                if mapString[i][j] == '@':
                    map[i,j] = 1

                #map[i,j] = mapString[i][j]
        self.mapObj['map'] = map
        if estado_inicial[0]<0 or estado_inicial[0]>=height or estado_inicial[1]>=width or map[estado_inicial[0], estado_inicial[1]] == 1:
            print('error! initial state is in a wall or beyond limits')
            exit()
        if estado_final[0]<0 or estado_final[0]>=height or estado_final[1]>=width or map[estado_final[0], estado_final[1]] == 1:
            print('error! final state is in a wall or beyond limits')
            exit()
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final


b = Ids()
filename = sys.argv[1]
estado_inicial = (int(sys.argv[2]), int(sys.argv[3]))
estado_final = (int(sys.argv[4]), int(sys.argv[5]))
ic(estado_final)
ic(estado_inicial)
print(sys.argv)
b.load_map(filename, estado_inicial, estado_final)
b.busca_ids()
