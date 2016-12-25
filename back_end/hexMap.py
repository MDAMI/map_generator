import random
import sys
import math

class hexMap(object):
    terrainName = {1: "plain", 2: "scrub", 3: "forest", 4: "rough", 5: "desert",
                6: "hills", 7: "mountains", 8: "marsh", 9: "pond",
                10: "depression"}

    terrainID = {"plain": 1, "scrub": 2, "forest": 3, "rough": 4, "desert": 5,
                "hills": 6, "mountains": 7, "marsh": 8, "pond": 9,
                "depression": 10}

    chances = [ [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                [3, 11, 13, 14, 15, 16, 17, 18, 19, 20],
                [1, 4, 14, 15, 0, 16, 17, 18, 19, 20],
                [2, 4, 5, 8, 10, 15, 17, 18, 19, 20],
                [3, 5, 0, 8, 14, 15, 17, 18, 19, 20],
                [1, 3, 5, 7, 8, 14, 16, 17, 19, 20],
                [1, 2, 3, 5, 6, 10, 18, 0, 19, 20],
                [2, 4, 6, 7, 0, 8, 0, 15, 19, 20],
                [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
                [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]]

    def __init__(self, width, height):
        self.mapArray = [["none" for x in range(width)] for y in range(height)]

    def assign(self, row, col, prev):
        rand = random.randint(1,20)
        index = 0
        x = False
        while x == False:
            if self.chances[prev-1][index] < rand:
                index += 1;
            else:
                x = True
        self.mapArray[row][col] = self.terrainName.get(index+1)

    def fillMap(self):
        filled = False
        row = math.floor(len(self.mapArray)/2);
        col = math.floor(len(self.mapArray[0])/2);
        self.mapArray[row][col] = self.terrainName.get(random.randint(1,8))
        while filled == False:
            neighbors = self.findEmptyNeighbors(row, col);
            if len(neighbors) != 0:
                coords = neighbors[random.randint(0,len(neighbors)-1)]
                prev = self.terrainID.get(self.mapArray[row][col])
                self.assign(coords[0], coords[1], prev)
                row = coords[0]
                col = coords[1]
            else:
                findingEmpty = True;
                row = 0;
                col = 0;
                while findingEmpty:
                    if self.mapArray[row][col] == 'none':
                        findingEmpty = False
                        self.mapArray[row][col] = self.terrainName.get(random.randint(1,8))
                    elif col == (len(self.mapArray[0])-1) and row == (len(self.mapArray)-1):
                        filled = True;
                        findingEmpty = False;
                    elif col == (len(self.mapArray[0])-1):
                        col = 0
                        row += 1
                    else:
                        col += 1

    def findNeighbors(self, row, col):
        nb = []
        if col != 0:
            nb.append((row, col-1))
        if col != len(self.mapArray[0])-1:
            nb.append((row, col+1))
        if row != 0:
            nb.append((row-1, col))
            if row % 2 == 0:
                if col != len(self.mapArray[0])-1:
                    nb.append((row-1, col+1))
            else:
                if col != 0:
                    nb.append((row-1, col-1))
        if row != len(self.mapArray)-1:
            nb.append((row+1, col))
            if row % 2 == 0:
                if col != len(self.mapArray[0])-1:
                    nb.append((row+1, col+1))
            else:
                if col != 0:
                    nb.append((row+1, col-1))
        return nb

    def findEmptyNeighbors(self, row, col):
        nb = self.findNeighbors(row, col)
        return [x for x in nb if self.mapArray[x[0]][x[1]] == "none"]

    def printMap(self):
        for arr in self.mapArray:
            for name in arr:
                sys.stdout.write(name + ", ")
            sys.stdout.write("\n")
        sys.stdout.flush();

    def mapString(self):
        mapStr = ''
        for arr in self.mapArray:
            for name in arr:
                mapStr += (name + ", ")
            mapStr += "\n"
        return mapStr
