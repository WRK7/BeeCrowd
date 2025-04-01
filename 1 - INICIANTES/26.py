escolha, escolha2 = input().split()
escolha= int(escolha)
escolha2 = int(escolha2)
a=4
b=4.50
c=5
d=2
e=1.50
if escolha == 1:
    resultado = escolha2 * a
    print (f'Total: R$ {resultado}.00')
elif escolha == 2:
    resultado = escolha2 * b
    print (f'Total: R$ {resultado}0')
elif escolha == 3:
    resultado = escolha2 * c
    print (f'Total: R$ {resultado}.00')
elif escolha == 4:
    resultado = escolha2 * d
    print (f'Total: R$ {resultado}.00')
elif escolha == 5:
    resultado = escolha2 * e
    print (f'Total: R$ {resultado}0')
else:
    print ('Valor invalido')