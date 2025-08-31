lista = [0] * 5
lista[0] = 1
lista[1] = 2
lista[2] = 2
lista[3] = 3
lista[4] = 4

cont = [0] * 5
valores = [0] * 5

for i in range (5):
    for j in range(5):
        if lista[i] == lista[j]:
            valores[i] = lista[i]
            cont[i] += 1

for i in range (5):
    if cont[i] == 1:
        cont[i] = 0
        valores[i] = 0

cont2 = 0

for i in range (5):
    if cont[i] == 0:
        cont2 += 1

lista2 = [0] * (5 - cont2)

for i in range (len(lista2)):
    for j in range(5):
        if valores[j] != 0:
            lista2[i] = valores[j]

for i in range (len(lista2)):
    for j in range(len(lista2)):
        if lista2[i] == lista2[j]:



print("Valores que se repetem: ", lista2)
print("Vezes que se repetem: ", cont)