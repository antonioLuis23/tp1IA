import  os, sys, copy
import time
import timeit
import numpy as np
from icecream import ic


class Node:
    state = ()
    parent = None
    action = ""
    path_cost = 0

class Ids:
    def __init__(self):
        self.mapObj = {}
        self.estado_inicial = ()
        self.estado_final = ()
        self.movimento = ['L','R', 'U', 'D', 'LU', 'LD', 'RU', 'RD']

    def ehObjetivo(self, node):
        if node.state == self.estado_final:
            return True

    def acaoPermitida(self, action, node):
        ic(node.state[1])
        if action == 'L' and node.state[1]-1 >= 0:
            return (node.state[0], node.state[1]-1, 1)
        elif action == 'R' and node.state[1]+1 <= self.mapObj["width"]-1:
            return (node.state[0], node.state[1]-1, 1)
        elif action == 'U' and node.state[0]-1 >= 0:
            return (node.state[0]-1, node.state[1], 1)
        elif action == 'D' and node.state[0]+1 >= self.mapObj["height"]-1:
            return (node.state[0]+1, node.state[1])
        elif action == 'LU' and node.state[1]-1 >= 0 and node.state[0]-1 >= 0:
            return (node.state[0]-1, node.state[1]-1, 1.5)
        elif action == 'LD' and node.state[1]-1 >= 0 and node.state[0]+1 >= self.mapObj["height"]-1:
            return (node.state[0]+1, node.state[1]-1, 1.5)
        elif action == 'RU' and node.state[1]+1 <= self.mapObj["width"]-1 and node.state[0]-1 >= 0:
            return (node.state[0]-1, node.state[1]+1, 1.5)
        elif action == 'RD' and node.state[1]+1 <= self.mapObj["width"]-1 and node.state[0]+1 >= self.mapObj["height"]-1:
            return (node.state[0]+1,node.state[1]+1, 1.5)
        return False

    def ids_recursivo(self, node):
        if (self.ehObjetivo(node)):
            return True
        for action in self.movimento:

            ic(action)
            afterState = self.acaoPermitida(action, node)
            if afterState and self.mapObj['map'][afterState[0], afterState[1]]!=1:
                no = Node()
                on.state = (afterState[0], afterState[1])
                on.state = node
                no.action = action
                no.path_cost= node.path_cost+afterState[2]
                self.id_recursivo(no)

            #if(afterState):


    def busca_ids(self):
        inicial = Node()
        inicial.state = self.estado_inicial
        inicial.parent = None
        inicial.action = ""
        inicial.path_cost = 0
        self.ids_recursivo(inicial)


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
