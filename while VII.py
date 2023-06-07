nome = ''
while not nome: #não importa oq eu escre aqui sempre vai dar falso por conta do "not", pq ele ta negando
    nome=input('Digite seu nome')
valor=int(input('Digite um numero qualquer: '))
if valor:
    print('Voce digitou um valor diferente de zero')
else:
    print('vc digitou zero')