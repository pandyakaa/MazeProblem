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

if __name__ == "__main__":
    file = input("Masukkan nama file : ")
    maze, size_x , size_y = inputMaze(file)
    printMaze(maze)
    

    

        
        