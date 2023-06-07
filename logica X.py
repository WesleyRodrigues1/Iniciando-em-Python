dano = int(input('Qual a quantidade de dano: '))
escudo = int(input('Qual o valor do escudo: '))

if dano >= 10 and escudo == 0:
    print('Você está morto!')
else:
    print('Nossa, você sobreviveu!')

print("Escolha uma direção:")
print('1 - Leste')
print('2 - Norte')
print('3 - Sul')
print('4 - Oeste')
opcao = int(input('Digite a direção que deseja seguir: '))
#tanto faz a opção, que scolher por conta do 'or', vai dar verdeiro

if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    print('Parabéns, você escapou!')
else:
    print(' opção errada, Se fodeu, não escapou e morreu kkkkkkkkk')
