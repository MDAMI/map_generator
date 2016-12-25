from hexMap import hexMap
import random

mapObj = hexMap(12,6)
mapObj.assign(2,2,10)
mapObj.fillMap()
mapObj.printMap()
