dias=int(input('quantos dias? '))
horas=int(input('quantas horas? '))
minuntos=int(input('quantos minuntos? '))
segundos=int(input('quantos segundos? '))
total = segundos + (minuntos * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)
resposta= f'O total de segundos calculado é de {total}'
print(resposta)