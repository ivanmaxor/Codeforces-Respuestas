n = int(input())

for i in range(0, n):

    numeros = list(map(int, input().split()))
    numeros.sort()

    menor = numeros[0]
    mediano = numeros[1]
    mayor = numeros[2]

    rango = mayor - menor

    print(min(rango, mediano))