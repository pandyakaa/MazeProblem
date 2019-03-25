def isVisited(m,x,y) :
    if (m[x][y] == 1) :
        return True
    else :
        return False

def initMatriksVisited(m,size_x, size_y) :
    for i in range(size_x) :
        for j in range(size_y) :
            m[i][j] = 0

def isBuntu(x,y,m,mvisit) :
    if (m[x][y+1] == 1 and m[x][y]) :
        return True 

def BFS(start_x , start_y, finish_x, finish_y, arrvisited, arrhasil, m) :
    return 0
    
if __name__ == "__main__":
    arr = []
    f = open("matriks.txt","r")
    for line in f :
        arr.append([int(c) for c in line.strip()])
    
    
    

    

        
        