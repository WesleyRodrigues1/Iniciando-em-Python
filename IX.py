pr=int(input('qual o valor da comprar: '))
print('selecione o metodo de pagamento')
print('1-Pagamento à vista – conceder desconto de 5%;')
print('2-Pagamento em 3x – o valor não sofre alterações;')
print('3-Pagamento em 5x – acréscimo de 2%;')
print('4-Pagamento em 10x – acréscimo 8%;')
s1=int(input('selecione uma das opçoes acima: '))
if s1==1:
    desconto=(pr*5)/100
    print(f'pagamento a vista, recebeu R${desconto} de desconto')
    print(f"preço final é de R${pr-desconto}")
elif (s1==2):
    print(f'pagamento parcelado em 3x, o valor não sofre alterações')
    print(f'preço final é de R${pr} ')
elif (s1==3):
    juros=(pr*2)/100
    print(f'o valor da comprar final será de R${pr+juros}')
    print(f'será parcelado em 5x de R${(juros+pr)/5}')
elif(s1==4):
    juros= (pr*8)/100
    print('o valor final da compra será de R$', pr+juros)
    print(f'será parcelado em 10x de R${(pr+juros)/10}')
else:
    print('Opção inválida!')


