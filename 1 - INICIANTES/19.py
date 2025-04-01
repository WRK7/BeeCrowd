valor = int(input())
cedulas = [100,50,20,10,5,2,1]
print(valor)
for x in cedulas:
    print(f'{valor //x} nota(s) de R$ {x},00')
    valor %= x