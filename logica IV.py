print('olá seja bem vindo a loja do gostoso!!!')
print("pressione 1 mança")
print('pressione 2 leranja')
print('pressione 3 banana')
print("pressione 4 deseja bom dia")

produto=int(input('digite o número do produto que vc queira: '))
qtd=int(input("quantas unidades? "))
if (produto==1):
    pagar= qtd*2.3
    print(f'você comprou {qtd} mança, total a pagar {pagar}')

elif (produto==2):
    pagar=qtd*3.6
    print(f'você comprou {qtd} laranja, total a pagar {pagar}')
elif (produto==3):
    pagar = qtd * 1.85
    print(f'você comprou {qtd} banana, total a pagar {pagar:.2f}')
elif (produto==4):
    print('Olá bom dia, gostoso, seu lindo!!!')
else:
    print('produto inexistente')
