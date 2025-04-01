A, B, C = input().split()
A= float(A)
B= float(B)
C= float(C)
if A == 0:
    print ('Impossivel calcular')
else:
    delta = (B**2) - ((4*A) * C)
    if delta > 0:
        x = ((-B + (delta**0.5)) / (2*A))
        y = ((-B - (delta**0.5)) / (2*A))
        print (f'R1 = {x:.5f}')
        print (f'R2 = {y:.5f}')
    elif delta == 0:
        x = ((-B + (delta**0.5)) / (2*A))
        y = ((-B - (delta**0.5)) / (2*A))
        print (f'R1 = {x:.5f}')
        print (f'R2 = {y:.5f}')
    else:
        print ('Impossivel calcular')