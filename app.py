from flask import Flask
import random
import sys
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

class hexMap(object):
    terrainID = {1: "plain", 2: "scrub", 3: "forest", 4: "rough", 5: "desert", 6: "hills", 7: "mountains", 8: "marsh", 9: "pond", 10: "depression"}
    chances = [ [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                [3, 11, 13, 14, 15, 16, 17, 18, 19, 20],
                [1, 4, 14, 15, 0, 16, 17, 18, 19, 20],
                [2, 4, 5, 8, 10, 15, 17, 18, 19, 20],
                [3, 5, 0, 8, 14, 15, 17, 18, 19, 20],
                [1, 3, 5, 7, 8, 14, 16, 17, 19, 20],
                [1, 2, 3, 5, 6, 10, 18, 0, 19, 20],
                [2, 4, 6, 7, 0, 8, 0, 15, 19, 20]]

    def __init__(self, width, height):
        self.mapArray = [["none" for x in range(width)] for y in range(height)]

    def assign(self, row, col, prev):
        rand = random.randint(1,20)
        print rand
        print self.chances[prev-1]
        index = 0
        x = False
        while x == False:
            if self.chances[prev-1][index] < rand:
                index += 1;
            else:
                x = True
        self.mapArray[row][col] = self.terrainID.get(index+1)

    def fillMap(self):
        filled = False
        row = len(self.mapArray)/2;
        col = len(self.mapArray[0])/2;
        while filled == False:
            neighbors = findEmptyNeighbors();
            #TODO Finish this

    def findNeighbors(self, row, col):
        nb = []
        if col != 0:
            nb.append((row, col-1))
        if col != len(self.mapArray)-1:
            nb.append((row, col+1))
        if row != 0:
            nb.append((row-1, col))
            if row % 2 == 0:
                if col != len(self.mapArray)-1:
                    nb.append((row-1, col+1))
            else:
                if col != 0:
                    nb.append((row-1, col-1))
        if row != len(self.mapArray)-1:
            nb.append((row+1, col))
            if row % 2 == 0:
                if col != len(self.mapArray)-1:
                    nb.append((row+1, col+1))
            else:
                if col != 0:
                    nb.append((row+1, col-1))
        return nb

        def findEmptyNiegbors(self, row, col):
            nb = self.findNeighbors(row, col)
            return [x for x in nb if self.mapArray[x[0]][x[1]] == "none"]

    def printMap(self):
        for arr in self.mapArray:
            for name in arr:
                sys.stdout.write(name + ", ")
            sys.stdout.write("\n")
        sys.stdout.flush();
