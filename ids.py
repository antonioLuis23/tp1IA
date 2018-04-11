import  os, sys, copy
import time
import timeit
import numpy as np
from icecream import ic
class Ids:
    def __init__(self):
        self.mapObj = {}
        self.estado_inicial = ()
        self.estado_final = ()
        self.movimento = ['L','R', 'U', 'D', 'LU', 'LD', 'RU', 'RD']

    def busca_ids(self):

    def load_map(self, filename, estado_inicial, estado_final):
        assert os.path.exists(filename), 'Cannot find the level file: %s' %(filename)
        mapFile = open(filename, 'r')
        content = mapFile.readlines() + ['\r\n']
        mapFile.close()
        height = int(content[1][7:-1])
        width = int(content[2][6:-1])
        self.mapObj['height'] =height
        self.mapObj['width'] = width
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
        self.estado_inicial= estado_inicial
        self.estado_final = estado_final


b = Ids()
filename = sys.argv[1]
estado_inicial = (sys.argv[2], sys.argv[3])
estado_final = (sys.argv[4], sys.argv[5])
ic(estado_final)
ic(estado_inicial)
print(sys.argv)
b.load_map(filename, estado_inicial, estado_final)
b.busca_ids()
