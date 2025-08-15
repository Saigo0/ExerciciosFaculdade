from xmlrpc.client import MAXINT

city1cod = int(input("Insira o código da cidade 1: "))
city1vehicles = int(input("Insira quantos veículos a cidade 1 tem: "))
city1crashes = int(input("Insira o número de acidentes de trânsito com vítimas na cidade 1: "))

city2cod = int(input("Insira o código da cidade 2: "))
city2vehicles = int(input("Insira quantos veículos a cidade 2 tem: "))
city2crashes = int(input("Insira o número de acidentes de trânsito com vítimas na cidade 2: "))

city3cod = int(input("Insira o código da cidade 3: "))
city3vehicles = int(input("Insira quantos veículos a cidade 3 tem: "))
city3crashes = int(input("Insira o número de acidentes de trânsito com vítimas na cidade 3: "))

city4cod = int(input("Insira o código da cidade 4: "))
city4vehicles = int(input("Insira quantos veículos a cidade 4 tem: "))
city4crashes = int(input("Insira o número de acidentes de trânsito com vítimas na cidade 4: "))

city5cod = int(input("Insira o código da cidade 5: "))
city5vehicles = int(input("Insira quantos veículos a cidade 5 tem: "))
city5crashes = int(input("Insira o número de acidentes de trânsito com vítimas na cidade 5: "))

maiorIndice = 0
maiorIndiceCod = ""
menorIndice = MAXINT
menorIndiceCod = ""

for i in range (1, 6):
    
