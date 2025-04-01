valor = int(input())
horas = 0
minutos = 0
segundos = 0
if valor >= 3600:
    while valor >= 3600:
        valor = valor - 3600
        horas += 1
if valor >= 60:
    while valor >= 60:
        valor = valor - 60
        minutos += 1
if valor >0 and valor < 60:
    segundos = valor
print (f'{horas}:{minutos}:{segundos}')