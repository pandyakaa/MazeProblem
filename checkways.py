def inputMaze(filename) :
    arr = []
    f = open("{}.txt".format(filename),"r")
    for line in f :
        arr.append([int(c) for c in line.strip()])
    baris = len(arr)
    kolom = len(arr[0])

    f.close()
    return arr,baris,kolom

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
    maze, baris , kolom = inputMaze(file)

    # Finish ada pada angka 2
    for i in maze :
        print(i)
    print()
    printMaze(maze)
    print()
    if (BFS(maze,0,1)) :
        printSolution(maze)
    else :
        print("NOT FOUND")