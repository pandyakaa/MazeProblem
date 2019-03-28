import sys
from collections import deque
from point import Point
from colorama import Fore, Back, Style
from priorityQueue import PriorityQueue
import turtle
import time

#color definition
tileColor = "white"
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

    startr = -1
    startc = -1
    finishr = -1
    finishc = -1

    # Melakukan pencarian titik mulai dan akhir (case : kiri dan kanan)
    for i in range(baris) :
        if (arr[i][0] == 0) :
            startr = i
            startc = 0

        if (arr[i][kolom-1] == 0) :
             finishr = i
             finishc = kolom-1

    # Melakukan pencarian titik mulai dan akhir (case : atas dan bawah)
    for i in range(kolom) :
        if (arr[0][i] == 0) :
            startr = 0
            startc = i

        if (arr[baris-1][i] == 0) :
            finishr = baris-1
            finishc = i

    # Melakukan validasi apakah matriks bisa dimainkan atau tidak
    if ( startr != -1 and startc != -1 and finishr != -1 and finishc != -1 ) :
        valid = True
    else :
        valid = False

    f.close()
    return arr,startr,startc,finishr,finishc, valid

#deep copy for maze
def copy(m1) :
    m2 = []
    for i in range(len(m1)) :
        temp = []
        for j in range(len(m1[0])) :
            temp.append(m1[i][j])
        m2.append(temp)

    return m2

#Tile block class
class Tile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5)
        self.color(tileColor)
        self.penup()
        self.speed(0)


#Wall block class
class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color(wallColor)
        self.shapesize(0.5)
        self.penup()
        self.speed(0)

#goal block class
class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5)
        #loses square in initialization
        self.color("white")
        self.penup()
        self.speed(0)

#Solution block class
class Sol(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5)
        #loses square in initialization
        self.color("white")
        self.penup()
        self.speed(0)

#BFS block class
class Bfs(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shapesize(0.5)
        #loses square in initialization
        self.color("white")
        self.penup()
        self.speed(0)

#draw maze 1 as walls
def drawMaze(array):
    for y in range(len(array)):
        for x in range(len(array[y])):
            i = -288 + (x * 12)
            j = 288 - (y * 12)

            if array[y][x] == 0:
                Tile.goto(i,j)
                Tile.stamp()
            if array[y][x] == 1:
                Wall.goto(i, j)
                Wall.stamp()
            if array[y][x] == 2:
                goal.goto(i,j)
                goal.color(goalColor)


    return (-288 + (len(array[0]) * 12), 288 - (len(array) * 12))


#check for walls
def isFeasible(m,x,y) :
    if ( (m[x][y]==0 or m[x][y]==2) ) :
        return True

    return False

#Breadth first search
def BFS(maze,x,y,fp) :
    de = deque()
    de.append(Point(x,y,None))

    while ( not(len(de) == 0) ) :
        p = de.popleft()

        i = -288 + (p.y * 12)
        j = 288 - (p.x * 12)

        maze[p.x][p.y] = 3
        if (p.isEqual(fp)) :
            return p

        if(isFeasible(maze,p.x-1,p.y)) :
            nextP = Point(p.x-1,p.y,p)
            de.append(nextP)

        if (isFeasible(maze,p.x+1,p.y)) :
            nextP = Point(p.x+1,p.y,p)
            de.append(nextP)

        if(isFeasible(maze,p.x,p.y+1)) :
            nextP = Point(p.x,p.y+1,p)
            de.append(nextP)

        if(isFeasible(maze,p.x,p.y-1)) :
            nextP = Point(p.x,p.y-1,p)
            de.append(nextP)

        #color BFS
        Bfs.goto(i,j)
        Bfs.color(bfsColor)
        Bfs.stamp()

#Manhattan distance
def manhattanDist(point_start,point_finish) :
    return (abs(point_start.x - point_finish.x) + abs(point_start.y - point_finish.y))

#A*
def AStar(maze,x,y,fpoint) :
    startPoint = Point(x,y,None)
    startPoint.f = startPoint.g = startPoint.h = 0

    openList = PriorityQueue()

    openList.insert(startPoint)

    while ( not(openList.isEmpty()) ) :

        current_node = openList.delete()
        maze[current_node.x][current_node.y] = 3
        i = -288 + (current_node.y * 12)
        j = 288 - (current_node.x * 12)
        #color BFS
        Bfs.goto(i,j)
        Bfs.color(bfsColor)
        Bfs.stamp()


        if (current_node.isEqual(fpoint) ) :
            return current_node

        children = []
        for pos in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            curr_x = current_node.x + pos[0]
            curr_y = current_node.y + pos[1]

            if (not(isFeasible(maze,curr_x,curr_y))) :
                continue

            child = Point(curr_x,curr_y,current_node)
            children.append(child)

        for child in children :
            child.g = current_node.g + 1
            child.h = manhattanDist(child,fpoint)
            child.f = child.g + child.h

            openList.insert(child)

#main
if __name__ == "__main__":
    file = input("Masukkan nama file : ")
    maze, startrow, startcolumn, finishrow, finishcolumn, valid = inputMaze(file)
    maze2 = copy(maze)

    fp = Point(finishrow, finishcolumn, None)

    #Turtle object initialization
    Tile = Tile()
    Wall = Wall()
    goal = Goal()
    Sol = Sol()
    Bfs = Bfs()

    if (valid) :
        print("Found")
        #Draw Maze
        drawMaze(maze)

        #BFS execution
        p = BFS(maze, startrow, startcolumn,fp)
        #draw Solution
        while (p.getParent() != None ) :
            maze[p.x][p.y] = 4

            i = -288 + (p.y * 12)
            j = 288 - (p.x * 12)
            Sol.goto(i,j)
            Sol.color(solColor)
            Sol.stamp()

            p = p.getParent()

        maze[startrow][startcolumn] = 4
        i = -288 + (startcolumn * 12)
        j = 288 - (startrow * 12)
        Sol.goto(i,j)
        Sol.color(solColor)
        Sol.stamp()


        #Draw Maze
        drawMaze(maze2)
        #A* execution
        q = AStar(maze2,startrow,startcolumn,fp)
        #draw Solution
        while (q.getParent() != None ) :
            maze[q.x][q.y] = 4

            i = -288 + (q.y * 12)
            j = 288 - (q.x * 12)
            Sol.goto(i,j)
            Sol.color(solColor)
            Sol.stamp()

            q = q.getParent()

        maze2[startrow][startcolumn] = 4
        i = -288 + (startcolumn * 12)
        j = 288 - (startrow * 12)
        Sol.goto(i,j)
        Sol.color(solColor)
        Sol.stamp()

    else :
        print("Not Found")



    wn.mainloop()
