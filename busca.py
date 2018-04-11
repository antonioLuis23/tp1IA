import  os, sys, copy
import time
import timeit
import numpy as np
from icecream import ic
class Busca:
    def __init__(self, filename):
        self.mapObj = {}
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
        ic(map)

filename = "maps/map1.map"
b = Busca(filename)
