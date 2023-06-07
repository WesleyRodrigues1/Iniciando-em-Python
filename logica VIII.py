print('calculadora')
print('adição (+)')
print('subtração (-)')
print('multiplicação (*)')
print('divisão (/)')
op=input('qual operação deseja fazer? ')
if (op=='+') or (op=='-')  or (op == '/') or (op=='*'):
    y=int(input('digite um um nuemero: '))
    x=int(input('digite outro número: '))
if (op == '+'):
    soma= y+x+
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
else:
    print('operação invalida')
