def inputMaze(filename) :
    arr = []
    f = open("{}.txt".format(filename),"r")
    for line in f :
        arr.append([int(c) for c in line.strip()])
    panjang = len(arr[0])
    lebar = len(arr)

    f.close()
    return arr,panjang,lebar

def printMaze(m) :
    for i in m :
        for j in i :
            if ( j == 1 ) :
                print("# ", end ='')
            else :
                print("  ",end = '')
        print()

def printSolution(m) :
    for i in m :
        for j in i :
            if (j == 0 ) : 
                print(" ",end = '')
            else :
                print("# ",end = '')
        print()

def isSafe(m,x,y) :
    if ( x >= 0 and x < len(m[0]) and ( y >= 0 and y < len(m)) and m[x][y] == 0 ) :
        return True
    else :
        return False

def solveUtil(m,x,y,sol) :
    if ( x == len(m[0]) - 1 and y == len(m) - 1 ) :
        sol[x][y] = 0
        return True
    
    if isSafe(m,x,y) == True :
        sol[x][y] = 0

        if solveUtil(m,x+1,y,sol) == True :
            return True
        
        if solveUtil(m,x,y+1,sol) == True :
            return True
        
        sol[x][y] = 1
        return False

def solveMaze(m) :

    sol = [ [ 1 for j in range(len(m[0])) ] for i in range(len(m)) ] 
      
    if solveUtil(m, 0, 0, sol) == False: 
        print("Solution doesn't exist"); 
        return False
      
    printSolution(sol) 
    return True

if __name__ == "__main__":
    file = input("Masukkan nama file : ")
    maze, size_x , size_y = inputMaze(file)

    printMaze(maze)
    print()
    printSolution(maze)
    print()
    solveMaze(maze)
    

    

        
        