#for i in range (0,21,2):
#    print(i)

#for i in range (21,0,-2):
     #print(i)

n=int(input("intodice un numero para la altura del triangulo: "))
for i in range(1,n+1,2):
    for j in range(i,0,-2):
        print(j, end=" ")
    print(" ")    