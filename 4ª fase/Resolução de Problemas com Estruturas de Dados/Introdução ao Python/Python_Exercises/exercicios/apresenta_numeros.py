I = int(input("Insira o valor de I: "))
A = int(input("Insira o valor de A: "))
B = int(input("Insira o valor de B: "))
C = int(input("Insira o valor de C: "))

if I == 1:
    if C > B and B > A:
        print(A,B,C)
    elif B > C and C > A:
        print(A,C,B)
    elif A > B and C > A:
        print(B, A, C)
    elif A > B and C > B and A > B:
        print(B,C,A)
    elif B > C and A > C and B > A:
        print(C,A,B)
    else:
        print(C,B,A)

if I == 2:
    if A > B and B > C:
        print(A,B,C)
    elif B > C and C > A:
        print(A,C,B)
    elif B > C and C > A:
        print(B,C,A)
    elif A > C and B > A:
        print(B,A,C)
    elif C > B and B > A:
        print(C,B,A)
    else:
        print(C,A,B)

if I == 3:
    if B > C and C > A and B > A:
        print(A,B,C)
    elif C > B and C > A and B > A:
        print(A,C,B)
    elif C > B and C > A and A > B:
        print(B,C,A)
    elif A > B and A > C and C > B:
        print(B,A,C)
    elif B > C and A > C and B > A:
        print(C,B,A)
    else:
        print(C,A,B)

print("Fim do programa!")


