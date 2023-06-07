# CALCULADORA VERSÃO 2.0
print('calculadora')
print('adição (+)')
print('subtração (-)')
print('multiplicação (*)')
print('divisão (/)')

while True: #COLOCAR O WHILE ANTES DA OPERAÇÃO ASSIM ELE VAI REPETIR AS MESMA (O S PARA ENCERRA O LOOP)
    op = input('qual operação deseja fazer? ')
    if (op == '+') or (op == '-') or (op == '/') or (op == '*'):
        y = int(input('digite um um numero: '))
        x = int(input('digite outro número: '))

    if (op == '+'):
        soma= y+x
        print(f'o resulda da adição é {soma}')
        continue #serve pra volta la pra cimar
    elif (op=='-'):
        soma= y-x
        print(f'o resulda da subtração é {soma}')
        continue#serve pra volta la pra cimar
    elif (op=='*'):
        soma= y*x
        print(f'o resultado da multiplicação é {soma}')
        continue#serve pra volta la pra cimar
    elif (op=='/'):
        soma= y/x
        print(f'o resultado da divisão é {soma}')
        continue#serve pra volta la pra cimar

    elif (op=='s'): #caso eu aperte a a tecla S o Programa encerra
        break#serve pra quebra o Loop

    else: #CASO EU APERTE QUALQUER TECLA QUE NÃO SEJA AS PREDEFINAS
        print('operação invalida')

print('encerrando programa...')#quando digitar S encerra o programa.