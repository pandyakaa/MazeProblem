# Kelas Point

class Point :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def print(self) :
        print("({},{})".format(self.x,self.y))
        