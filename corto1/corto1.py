def collatz(n):          #funcion que determina la seccuencia de collatz de un numero 
    sec = [n]            #lista que guarda la seccuencia
    while n!=1:           #se ejecuta hasta que el ultimo terino de la seccuiencia sea 1
        if n%2==0:        
            n=n//2          #si n es par el siguiente numero de la secuencia sera n/2
        else:
            n=(3*n)+1       #si n es impar el siguiente numero de la secuencia sera 3*n+1
        sec.append(n)       #guarda los sig n en la lista
    return sec              #retorna la lista cuando ya se ha teminado de encontrar todos los teminos 

nf=728    #ultimos 3 digitos del carnet

file = 'collatz.txt'  #nombre del archivo donde se guardaran los datos
sfile = open(file, 'w')  #abir el archivo

for i in range(2, nf+1):                           #encuentra la seccuencia de collatz para todos los numeros entre 2 - 728
    sfile.write(str(collatz(i))+'\n')              #escribe la secuencia de collatz del numero i en el archivo collatz.txt 

sfile.close()          #cerrar archivo

