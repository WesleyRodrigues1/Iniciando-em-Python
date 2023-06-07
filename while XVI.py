print('Bem-vindo à Lanchonete do Wesley Rodrigues ')
#lista do cardapio do restaurante
print('***************Cardápio***************')
print('| Código | Descricao              | Valor |')
print('| 100    | Cachorro Quente        | 9,00  |')
print('| 101    | Cachorro Quente Duplo  | 11,00 |')
print('| 102    | X-Egg                  | 12,00 |')
print('| 103    | X-Salada               | 13,00 |')
print('| 104    | X-Bacon                | 14,00 |')
print('| 105    | X-Tudo                 | 17,00 |')
print('| 200    | Refrigerante Lata      | 5,00  |')
print('| 201    | Chá Gelado             | 4,00  |')

preco = 0 # verificar total que o usuário gastou

while True: # Verifixar o Pedido do Código
    codigo = int(input('Digite o código do Produto: '))

    # Verifica se o código digitado é válido
    if codigo not in [100, 101, 102, 103, 104, 105, 200, 201]:
        print('Opção inválida')
        continue

    # Verifica o código e atualiza o preço
    if codigo == 100:
        print('Você pediu um Cachorro Quente no valor de R$ 9,00')
        preco += 9
    elif codigo == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de R$ 11,00')
        preco += 11
    elif codigo == 102:
        print('Você pediu um X-Egg no valor de R$ 12,00')
        preco += 12
    elif codigo == 103:
        print('Você pediu um X-Salada no valor de R$ 13,00')
        preco += 13
    elif codigo == 104:
        print('Você pediu um X-Bacon no valor de R$ 14,00')
        preco += 14
    elif codigo == 105:
        print('Você pediu um X-Tudo no valor de R$ 17,00')
        preco += 17
    elif codigo == 200:
        print('Você pediu um Refrigerante Lata no valor de R$ 5,00')
        preco += 5
    elif codigo == 201:
        print('Você pediu um Chá Gelado no valor de R$ 4,00')
        preco += 4

    #Verificar se o Usuario vai quere algo mais
    pedir = int(input('Deseja pedir mais alguma coisa?\n1 - Sim\n2 - Não: '))

    # Verifica se o usuário deseja fazer outro pedido
    if pedir == 1:
        continue

    else: # Se não fizer outro pedido  o codigo encerrar mostrando o total gasto
        print(f'O total a ser pago é de R$ {preco:.2f}')
        break
