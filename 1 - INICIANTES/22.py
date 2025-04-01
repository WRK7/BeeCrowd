valor = float(input())
centavos = int(round(valor * 100))
cedulas = [10000,5000,2000,1000,500,200]
print('NOTAS:')
for x in cedulas:
    print(f'{centavos //x} nota(s) de R$ {x//100}.00')
    centavos %= x
moedas = [100,50,25,10,5,1]
print('MOEDAS:')
for i in moedas:
    print(f'{centavos //i} moeda(s) de R$ {i/100:.2f}')
    centavos %= i