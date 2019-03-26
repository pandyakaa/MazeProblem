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

# Solusi menggunakan Algoritma BFS
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

if __name__ == "__main__":
    file = input("Masukkan nama file : ")
    maze, start_baris , start_kolom, finish_baris , finish_kolom = inputMaze(file)

    # Memberikan finish angka 2 sehingga lebih mudah dicari
    maze[finish_baris][finish_kolom] = 2
    
    printMaze(maze)
    print()
    if (BFS(maze,start_baris,start_kolom)) :
        printSolution(maze)
    else :
        print("NOT FOUND")