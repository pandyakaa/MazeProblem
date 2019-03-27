import sys
from collections import deque
from point import Point
from colorama import Fore, Back, Style
import turtle

wallColor = "black"
goalColor = "green"
bfsColor = "blue"
solColor = "red"

#screen initialization
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Solver")
wn.setup()
wn.screensize(2000, 2000)


#input maze
def inputMaze(filename) :
    arr = []
    f = open("{}.txt".format(filename),"r")
    for line in f :
        arr.append([int(c) for c in line.strip()])
    baris = len(arr)
    kolom = len(arr[0])

    startb = -1
    startk = -1
    finishb = -1
    finishk = -1

    # Melakukan pencarian titik mulai dan akhir (case : kiri dan kanan)
    for i in range(baris) :
        if (arr[i][0] == 0) :
            startb = i
            startk = 0

        if (arr[i][kolom-1] == 0) :
             finishb = i
             finishk = kolom-1

    # Melakukan pencarian titik mulai dan akhir (case : atas dan bawah)
    for i in range(kolom) :
        if (arr[0][i] == 0) :
            startb = 0
            startk = i

        if (arr[baris-1][i] == 0) :
            finishb = baris-1
            finishk = i

    f.close()
    return arr,startb,startk,finishb,finishk


#Wall block class
class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color(wallColor)
        self.penup()
        self.speed(-1)

#goal block class
class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        #loses square in initialization
        self.color("white")
        self.penup()
        self.speed(-1)

#Solution block class
class Sol(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        #loses square in initialization
        self.color("white")
        self.penup()
        self.speed(-1)

#BFS block class
class Bfs(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        #loses square in initialization
        self.color("white")
        self.penup()
        self.speed(-1)

#draw maze 1 as walls
def drawMaze(array):
    for y in range(len(array)):
        for x in range(len(array[y])):
            i = -288 + (x * 24)
            j = 288 - (y * 24)

            if array[y][x] == 1:
                Wall.goto(i, j)
                Wall.stamp()
            if array[y][x] == 2:
                goal.goto(i,j)
                goal.color(goalColor)


    return (-288 + (len(array[0]) * 24), 288 - (len(array) * 24))


#check for walls
def isFeasible(m,x,y) :
    if ( (m[x][y]==0 or m[x][y]==2) ) :
        return True

    return False

#Breadth first search
def BFS(maze,x,y,de) :
    de.append(Point(x,y,None))

    while ( not(len(de) == 0) ) :
        p = de.popleft()
        i = -288 + (p.y * 24)
        j = 288 - (p.x * 24)

        if (maze[p.x][p.y] == 2) :
            return p

        if(isFeasible(maze,p.x-1,p.y)) :
            maze[p.x][p.y] = 3
            nextP = Point(p.x-1,p.y,p)
            de.append(nextP)
        elif (maze[p.x][p.y] == 0) :
            maze[p.x][p.y] = 3

        if (isFeasible(maze,p.x+1,p.y)) :
            maze[p.x][p.y] = 3
            nextP = Point(p.x+1,p.y,p)
            de.append(nextP)
        elif (maze[p.x][p.y] == 0) :
            maze[p.x][p.y] = 3

        if(isFeasible(maze,p.x,p.y+1)) :
            maze[p.x][p.y] = 3
            nextP = Point(p.x,p.y+1,p)
            de.append(nextP)
        elif (maze[p.x][p.y+1] == 0) :
            maze[p.x][p.y] = 3

        if(isFeasible(maze,p.x,p.y-1)) :
            maze[p.x][p.y] = 3
            nextP = Point(p.x,p.y-1,p)
            de.append(nextP)
        elif (maze[p.x][p.y-1] == 0) :
            maze[p.x][p.y] = 3
        Bfs.goto(i,j)
        Bfs.color(bfsColor)
        Bfs.stamp()

#main
if __name__ == "__main__":
    file = input("Masukkan nama file : ")
    maze, startrow, startcolumn, finishrow, finishcolumn = inputMaze(file)
    maze[finishrow][finishcolumn] = 2

    Wall = Wall()
    goal = Goal()
    Sol = Sol()
    Bfs = Bfs()
    drawMaze(maze)

    de = deque()
    p  =None
    p = BFS(maze, startrow, startcolumn, de)

    if (p != None) :
        print("Found")


        while (p.getParent() != None ) :
            maze[p.x][p.y] = 4

            i = -288 + (p.y * 24)
            j = 288 - (p.x * 24)
            Sol.goto(i,j)
            Sol.color(solColor)
            Sol.stamp()

            p = p.getParent()

        maze[startrow][startcolumn] = 4
        i = -288 + (startcolumn * 24)
        j = 288 - (startrow * 24)
        Sol.goto(i,j)
        Sol.color(solColor)
        Sol.stamp()

    else :
        print("Not Found")



    wn.mainloop()
