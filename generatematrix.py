from random import randint

f = open("matriks.txt","w")

for i in range(5) :
    for j in range(5) :
        f.write(str(randint(0,1)))
    f.write("\n")
    
f.close()
    