import turtle

#screen initialization
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Solver")
wn.setup(700, 700)

#input maze from external file
#return array of maze, row, and column
def inputMaze(filename) :
    arr = []
    f = open("{}.txt".format(filename),"r")
    for line in f :
        arr.append([int(c) for c in line.strip()])
    baris = len(arr)
    kolom = len(arr[0])

    f.close()
    return arr,baris,kolom

#Wall block class
class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

#Solution block class
class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        #loses square in initialization
        self.color("white")
        self.penup()
        self.speed(-1)

#Text class
class Tex(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        FONT = ('Arial', 40, 'normal')
        self.write("Test",align="left", font = FONT)
        self.penup()
        self.speed(0)

#draw maze, 0 as walls, 2 as goals
def drawMaze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            i = -288 + (x * 24)
            j = 288 - (y * 24)

            if level[y][x] == 1:
                Wall.goto(i, j)
                Wall.stamp()
            if level[y][x] == 2:
                goal.goto(i,j)
                goal.color("green")
    return (-288 + (len(level[0]) * 24), 288 - (len(level) * 24))

#find Solution using BFS
def BFS(maze,x,y) :
    if (maze[x][y] == 2) :
        return True
    elif (maze[x][y] == 0 ) :
        maze[x][y] = 3
        if(x < len(maze) -1 ) :
            if BFS(maze,x+1,y) :
                return True
        if(x > 0) :
            if BFS(maze,x-1,y) :
                return True
        if ( y < len(maze[x])-1 ) :
            if BFS(maze,x,y+1) :
                return True
        if ( y > 0) :
            if BFS(maze,x,y-1) :
                return True

Wall = Wall()
goal = Goal()
level, row, column = inputMaze("input")
k, l = drawMaze(level)

if(BFS(level, 0, 1)):
    text = turtle.Turtle()
    text.shapesize(0.01)
    text.penup()
    text.goto(k, l)
    text.color("green")
    text.write("FOUND", font=("Arial", 48, "bold"))

    #tex.stamp()


wn.mainloop()
