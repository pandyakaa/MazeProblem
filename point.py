# Kelas Point

class Point :
    def __init__(self,x,y,parent):
        self.x = x
        self.y = y
        self.parent = parent

        self.f = 0
        self.g = 0
        self.h = 0

    def print(self) :
        print("({},{})".format(self.x,self.y))
    
    def getParent(self) :
        return self.parent
    
    def isEqual(self, other):
        return (self.x == other.x and self.y == other.y)
        
        