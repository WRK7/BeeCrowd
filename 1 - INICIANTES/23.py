A, B, C, D = input().split()
A= int(A)
B= int(B)
C= int(C)
D= int(D)
if B > C and D > A:
    soma1 = C + D
    soma2 = A + B
    if soma1 > soma2 and C > 0 and D > 0 and A %2 == 0:
        print ('Valores aceitos')
    else:
        print ('Valores nao aceitos')
else:
    print ('Valores nao aceitos')