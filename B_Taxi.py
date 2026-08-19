n_grupos = int(input())
grupos = list(map(int, input().split()))

uno = grupos.count(1)
dos = grupos.count(2)
tres = grupos.count(3)
cuatro = grupos.count(4)

taxis = cuatro

conjuntos_tres_uno = min(uno, tres)
taxis += conjuntos_tres_uno
tres -= conjuntos_tres_uno
uno -= conjuntos_tres_uno

taxis += tres
taxis += dos // 2

if dos % 2 == 1:
    taxis += 1
    uno -= min(uno, 2)

taxis += -(-uno // 4)

print(taxis)
