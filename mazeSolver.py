import sys
from collections import deque
from point import Point

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
            else :
                print("  ", end = '')
        print()

def isFeasible(m,x,y) :
    if ( (m[x][y]==0 or m[x][y]==2) ) :
        return True
    
    return False

def BFS(maze,x,y,de) :
    de.append(Point(x,y))

    while ( not(len(de) == 0) ) :
        p = de.pop()

        if (maze[p.x][p.y] == 2) :
            return True
        
        if(isFeasible(maze,p.x-1,p.y)) :
            maze[p.x][p.y] = 3
            nextP = Point(p.x-1,p.y) 
            de.append(nextP)
        elif (maze[p.x][p.y] == 0) :
            maze[p.x][p.y] = 3

        if (isFeasible(maze,p.x+1,p.y)) :
            maze[p.x][p.y] = 3
            nextP = Point(p.x+1,p.y)
            de.append(nextP)
        elif (maze[p.x][p.y] == 0) :
            maze[p.x][p.y] = 3
        
        if(isFeasible(maze,p.x,p.y+1)) :
            maze[p.x][p.y] = 3
            nextP = Point(p.x,p.y+1) 
            de.append(nextP) 
        elif (maze[p.x][p.y+1] == 0) :
            maze[p.x][p.y] = 3

        if(isFeasible(maze,p.x,p.y-1)) :
            maze[p.x][p.y] = 3
            nextP = Point(p.x,p.y-1) 
            de.append(nextP) 
        elif (maze[p.x][p.y-1] == 0) :
            maze[p.x][p.y] = 3
    
    return False


if __name__ == "__main__":
    file = input("Masukkan nama file : ")
    maze, start_baris , start_kolom, finish_baris , finish_kolom = inputMaze(file)

    # Memberikan finish angka 2 sehingga lebih mudah dicari
    maze[finish_baris][finish_kolom] = 2

    de = ([])
    printMaze(maze)
    print()
    if (BFS(maze,start_baris,start_kolom,de)) :
        for i in maze :
            print(i)
    else :
        print("NOT FOUND") 