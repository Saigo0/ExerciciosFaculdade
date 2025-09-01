lista = [0] * 5
lista[0] = 1
lista[1] = 2
lista[2] = 2
lista[3] = 3
lista[4] = 4

verificados = [0] * 5

for i in range(5):
    cont = 0
    for j in range(5):
        if lista[i] != verificados[j]:
            verificados [j] = lista[i]
        if lista[i] == lista[j]:
            cont += 1
    if cont > 1:
        cont -= 1
        print("O número", lista[i], "é repetido", cont, "vezes")

