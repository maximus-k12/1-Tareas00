def suma(n):
    divisores = [ d for d in range(1,n//2+1) if n % d == 0 ]
    return sum(divisores)
    
def numero_amigo(i):
    j = suma(i)
    if i<j and i==suma(j):
        print(i, j)

limit = int(input("Introduzca un numero: "))

for i in range(2, limit):
    numero_amigo(i)