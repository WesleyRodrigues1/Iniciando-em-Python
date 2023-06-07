import km as km

km=int(input('quantos km o carro vai percorre? '))
dias =int(input('quanto dias o carro vai ser alugado? '))
# dias custa 60 por dia, 0,15 km rodado;
s1= km * 0.15 + dias * 60
print(f'dias: {dias} e km: {km}')
print(f'valor a ser pago será de R${s1}')