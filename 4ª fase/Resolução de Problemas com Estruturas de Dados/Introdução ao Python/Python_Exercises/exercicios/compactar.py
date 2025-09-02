lista = [0] * 15

for i in range(len(lista)):
    lista[i] = i

nCompact = int(input("Digite quantos elementos da lista desejas compactar: "))

for i in range(nCompact):
    lista[(i + 1) * (-1)] = 0

print(lista)