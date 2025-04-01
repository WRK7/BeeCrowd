valor = int(input())
ano = 0
mes = 0
dias = 0
if valor >= 365:
    while valor >= 365:
        ano +=1
        valor = valor - 365
if valor >= 30:
    while valor >= 30:
        mes +=1
        valor = valor - 30
if valor > 0 and valor < 30:
    dias = valor
    valor = valor - valor
print (f'{ano} ano(s)')
print (f'{mes} mes(es)')
print (f'{dias} dia(s)')