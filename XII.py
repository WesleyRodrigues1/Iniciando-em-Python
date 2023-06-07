kwh=float(input('qual a quantidade de Kwh: '))
print('tipo de estalação')
print('Digite r para residência \nDigite i para industria e \nDigite c para comercios')

estalacao=input('tipo de estalaçao:  ')

if (estalacao=='r'):
    if (kwh<=500):
        preco= 0.40
        q = 'residência'
    else:
        preco= 0.65
        q = 'residência'
elif (estalacao=='c'):
    if (kwh<=100):
        preco= 0.55
        q = 'comercial'
    else:
        preco= 0.60
        q = 'comercial'
elif (estalacao=='i'):
    if (kwh<=5000):
        preco= 0.55
        q = 'industria'
    else:
        preco= 0.60
        q = 'industria'
if (estalacao=='r' or estalacao=='i' or estalacao=='c'):
    print(f'seu imóvel é {q}, o preço da fatura R${preco * kwh:.2f}')

else:
    print('opção invalida!')





