"""-------------------------------Principales numeros primos------------------------------------"""
""""-------------------Programa basado para un maximo de 15 numeros perfectos, en base 
a el numero primo de cada numero N--------------------------------------------------------------"""

primos_principales = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279] 
def Numeros_perfectos(n=10):
    return [(2**p - 1) * (2**(p - 1)) for p in primos_principales[:n]]
kms=int(input("Introduzca un numero: "))
print(Numeros_perfectos(n=kms))