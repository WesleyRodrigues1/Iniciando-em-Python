print("bem vindo a loja do Wesley Rodrigues Gama")

# Solicita o valor do produto e a quantidade de unidades
Preco_produto=float(input('Qual o valor do Produto: '))
quantidade_produto=int(input('Quantas Unidades: '))

# Calcula o valor sem desconto
sem_desconto=(Preco_produto*quantidade_produto)

# Verifica a quantidade de unidades e define o desconto correspondente
if (quantidade_produto<=9):
   desconto= 0
   porcentagem= '0%'
elif (quantidade_produto>=10 and quantidade_produto<=99):
    desconto= 0.05
    porcentagem = '5%'

elif (quantidade_produto>=100 and quantidade_produto<=999):
    desconto= 0.10
    porcentagem = '10%'

else:
    (quantidade_produto>=1000)
    desconto= 0.15
    porcentagem = '15%'
# Exibe o valor sem desconto
print(f'valor sem o desconto R${sem_desconto:.2f}')
# Exibe o valor com desconto
print(f'valor com desconto R${sem_desconto - (desconto * sem_desconto):.2f}, (desconto de {porcentagem})')