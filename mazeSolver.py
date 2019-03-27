import sys
from collections import deque
from point import Point
from priorityQueue import PriorityQueue

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

def printMaze(m) :
    for i in m :
        for j in i :
            if ( j == 1 ) :
                print("# ", end ='')
            else :
                print("  ", end = '')
        print()

def printSolution(m) :
    for i in m :
        for j in i :
            if (j == 1 ) : 
                print("# ",end = '')
            elif (j == 3 or j == 2) :
                print(" ",end = '')
            elif ( j == 4 ) :
                print("X ", end = '')
            else :
                print("  ", end = '')
        print()

def isFeasible(m,x,y) :
    if ( (m[x][y]==0 or m[x][y]==2)  and x >= 0 and x < len(m) and y >= 0 and y < len(m[0]) ) :
        return True
    
    return False

def BFS(maze,x,y,de) :
    de.append(Point(x,y,None))

    while ( not(len(de) == 0) ) :
        p = de.popleft()

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

def manhattanDist(point_start,point_finish) :
    return (abs(point_start.x - point_finish.x) + abs(point_start.y - point_finish.y))

def AStar(maze,x1,y1,fpoint) :
    startPoint = Point(x1,y1,None)
    startPoint.f = startPoint.g = startPoint.h = 0
    
    openList = PriorityQueue()

    openList.insert(startPoint)

    while ( not(openList.isEmpty()) ) :

        current_node = openList.delete()
        maze[current_node.x][current_node.y] = 3
        
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

if __name__ == "__main__":

    file = input("Masukkan nama file : ")
    maze, start_baris , start_kolom, finish_baris , finish_kolom = inputMaze(file)
    maze2, start_baris , start_kolom, finish_baris , finish_kolom = inputMaze(file)

    # Memberikan finish angka 2 sehingga lebih mudah dicari
    maze[finish_baris][finish_kolom] = 2
    
    fp = Point(finish_baris,finish_kolom,None)
    de = deque()

    p = BFS(maze,start_baris,start_kolom,de)
    q = AStar(maze2,start_baris,start_kolom,fp)

    if ( p != None ) :
        maze[start_baris][start_kolom] = 4
        while (p.getParent() != None ) :
            maze[p.x][p.y] = 4
            p = p.getParent()

        print("Solution with BFS :")
        printSolution(maze)

        maze2[start_baris][start_kolom] = 4
        while (q.getParent() != None ) :
            maze2[q.x][q.y] = 4
            q = q.getParent()

        print("\nSolution with A-Star :")
        printSolution(maze2)
    else :
        print("NOT FOUND")
    

