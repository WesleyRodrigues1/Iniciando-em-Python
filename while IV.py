# VALIDANDO ENTRADA
x=int(input('Digite um Valor maior do que zero: '))

while x<=0:
    x = int(input('Digite um Valor maior do que zero: '))
    print('incorreto tente novamente')

print(f'vc acertou parabens vc digitou o numero {x} !!')