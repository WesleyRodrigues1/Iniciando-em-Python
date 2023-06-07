# Solicita o preço do produto e o percentual de desconto ao usuário
preco_produto = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcula o valor do desconto
valor_desconto = (percentual_desconto / 100) * preco_produto

# Calcula o preço final do produto
preco_final = preco_produto - valor_desconto

# Exibe o valor do desconto e o preço final do produto
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
#o ":.2f" serve para dicidi o numero de casa decimas que vão aparecer
print(f"Preço final do produto: R$ {preco_final:.2f}")
