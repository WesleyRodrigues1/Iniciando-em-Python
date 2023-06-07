total= 0
dinheiro= 0

while True:
    idade = (input('Qual é sua idade: '))
    if idade == 'sair':
            break
    idade= int(idade)
    total= total+1

    if idade<= 2:
        print(f'entrada gratuia para menores de {idade} anos ')
    elif 3<=idade<=11:
        ingreso=15
        print(f'o valor do ingressora será de R${ingreso}')
    elif idade>=12:
        ingreso = 30
        print(f'o valor do ingressora será de R${ingreso}')
    dinheiro= dinheiro + ingreso

media= dinheiro/total
print (f'total de pessoas {total}')
print (f'total arrecadado R${dinheiro}')
print (f'media arrecadada R${media}')




