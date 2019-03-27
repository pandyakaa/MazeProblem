import sys
from collections import deque
from point import Point
from priorityQueue import PriorityQueue

# Fungsi inputMaze, dengan parameter sebuah file
# digunakan untuk memasukkan matriks sebagai representasi dari maze
# dari file eksternal dengan nama filename
# Sekaligus mencari titik awal masuk dan keluar, disimpan dalam startb, startk, finishb dan finishk
def inputMaze(filename) :
    arr = []

    f = open("{}.txt".format(filename),"r")
    for line in f :
        arr.append([int(c) for c in line.strip()])
    baris = len(arr)
    kolom = len(arr[0])
    f.close()

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

    # Melakukan validasi apakah matriks bisa dimainkan atau tidak
    if ( startb != -1 and startk != -1 and finishb != -1 and finishk != -1 ) :
        valid = True
    else :
        valid = False

    return arr,startb,startk,finishb,finishk,valid

# Fungsi printSolution, dengan parameter sebuah matriks m
# digunakan untuk melakukan output sebuah maze yang sudah ada solved
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

# Fungsi copy, dengan parameter sebuah matriks m1
# digunakan untuk melakukan DEEP COPY pada sebuah matriks
# sehingga tidak perlu membaca dari file eksternal lagi
def copy(m1) :
    m2 = []
    for i in range(len(m1)) :
        temp = []
        for j in range(len(m1[0])) :
            temp.append(m1[i][j])
        m2.append(temp)

    return m2

# Fungsi isFeasible, dengan parameter sebuah matriks m, int x dan int y
# digunakan untuk melakukan validasi, apakah koordinat (x,y) valid atau tidak
# DEFINISI VALID : Lebih atau sama dengan 0 , dan kurang dari panjang atau kolom matriks
def isFeasible(m,x,y) :
    if ( m[x][y]==0 and x >= 0 and x < len(m) and y >= 0 and y < len(m[0]) ) :
        return True
    
    return False

# Fungsi BFS, dengan parameter maze maze, int x, int y, dan point fp
# merupakan salah satu dari dua fungsi utama dalam program ini
# Memanfaatkan sebuah type data DEQUE, dan melakukan proses Breadth-First Searching
# Jika memiliki solusi, akan me-return sebuah point p
def BFS(maze,x,y,fp) :
    de = deque()
    de.append(Point(x,y,None))

    while ( not(len(de) == 0) ) :
        p = de.popleft()

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

# Fungsi manhattanDist, dengan parameter point point_start dan point point_finish
# digunakan untuk mencari nilai h(n) pada algoritma A*
# Menggunakan manhattan distance karena hanya bisa bergerak ke empat arah
def manhattanDist(point_start,point_finish) :
    return (abs(point_start.x - point_finish.x) + abs(point_start.y - point_finish.y))

# Fungsi AStar, dengan parameter maze maze, int x, int y, dan point fpoint
# merupakan salah satu dari dua fungsi utama dalam program ini
# Memanfaatkan type data Priority Queue, yang telah dibuat kelas sendiri sebelumnya
# Akan melakukan pencarian dengan algoritma AStar dengan :
# f(n) = g(n) + h(n)
# dengan g(n) adalah jarak sebenarnya sebuah titik ke titik akhir
# dan h(n) adalah jarak heuristik dari sebuah titik ke titik akhir dengan memanfaatkan manhattanDist
def AStar(maze,x,y,fpoint) :
    startPoint = Point(x,y,None)
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

# Fungsi main, akan dipanggil saat program ini dijalankan
if __name__ == "__main__":

    # Melakukan input nama file dari pengguna, dan memanggil fungsi inputMaze untuk
    # memasukkannya ke dalam maze
    file = input("Masukkan nama file : ")
    maze, start_baris , start_kolom, finish_baris , finish_kolom , valid = inputMaze(file)
    maze2 = copy(maze)

    # Util yang diperlukan oleh fungsi-fungsi searching
    fp = Point(finish_baris,finish_kolom,None)

    if ( valid ) :
        # Melakukan pemanggilan fungsi-fungsi Searching
        p = BFS(maze,start_baris,start_kolom,fp)
        q = AStar(maze2,start_baris,start_kolom,fp)
        
        # Melakukan output dari algoritma DFS
        maze[start_baris][start_kolom] = 4
        while (p.getParent() != None ) :
            maze[p.x][p.y] = 4
            p = p.getParent()

        print("\n \t \t Solution with BFS : \n")
        printSolution(maze)

        # Melakukan output dari algoritma A*
        maze2[start_baris][start_kolom] = 4
        while (q.getParent() != None ) :
            maze2[q.x][q.y] = 4
            q = q.getParent()

        print("\n \t \t Solution with A-Star : \n")
        printSolution(maze2)

    else :
        print("NOT FOUND")