n = int(input())

for i in range(0,n):
    palabra = input()
    largo = len(palabra)
    if largo <= 10:
        print(palabra)
        continue

    abreviado = f"{palabra[0]}{largo-2}{palabra[-1]}"
    print(abreviado)
    