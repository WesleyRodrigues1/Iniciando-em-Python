# CALCULADORA VERSÃO 1.2
print('calculadora')
print('adição (+)')
print('subtração (-)')
print('multiplicação (*)')
print('divisão (/)')
op=input('qual operação deseja fazer? ')
if (op=='+') or (op=='-')  or (op == '/') or (op=='*'):
    y = int(input('digite um um numero: '))
    x = int(input('digite outro número: '))

while op != 's': #COLCOR O WHILE ANTES DA OPERAÇÃO ASSIM ELE VAI REPETIR AS MESMA (O S PARA ENCERRA O LOOP)

    if (op == '+'):
        soma= y+x
        print(f'o resulda da adição é {soma}')
    elif (op=='-'):
        soma= y-x
        print(f'o resulda da subtração é {soma}')
    elif (op=='*'):
        soma= y*x
        print(f'o resultado da multiplicação é {soma}')
    elif (op=='/'):
        soma= y/x
        print(f'o resultado da divisão é {soma}')
    else: #CASO EU APERTE QUALQUER TECLA QUE NÃO SEJA AS PREDEFINAS
        print('operação invalida')

    op = input('qual operação deseja fazer? ')
    if (op == '+') or (op == '-') or (op == '/') or (op == '*'):
        y = int(input('digite um um numero: '))
        x = int(input('digite outro número: '))


print('encerrando programa...')#quando digitar S encerra o programa.
