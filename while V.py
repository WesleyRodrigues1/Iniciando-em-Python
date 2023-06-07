print('escre uma mensagem que irei repetir pra vc')
print('para encerra escreva sair')
while True: #true serve para executa sem uma condição especificar
    texto= input('digite a frase: ')
    print(texto)
    #breal serve para encerra o laço do programa
    if texto ==  'sair':
        break
print('vc digitou sair, encerrando programa')

