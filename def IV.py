def dimensoesObjeto():
    while True: #garante o Loop até as condições, forem satisfeitas
        try:
            comprimento = int(input('Digite o comprimento do objeto (em cm): '))  # Solicita o comprimento do objeto em centímetros
            largura = int(input('Digite a largura do objeto (em cm): '))  # Solicita a largura do objeto em centímetros
            altura = int(input('Digite a altura do objeto (em cm): ')) # Solicita a altura do objeto em centímetros

            volume = altura * comprimento * largura # Calcula o volume do objeto

            if volume < 1000:
                preco = 10 # Define o preço como 10 para objetos com volume inferior a 1000 cm³
            elif 1000 <= volume < 10000:
                preco = 20 # Define o preço como 20 para objetos com volume entre 1000 e 9999 cm³
            elif 10000 <= volume < 30000:
                preco = 30 # Define o preço como 30 para objetos com volume entre 10000 e 29999 cm³
            elif 30000 <= volume < 100000:
                preco = 50 # Define o preço como 50 para objetos com volume entre 30000 e 99999 cm³
            else:
                print(f'O volume do objeto é {volume} cm³')
                print('Não aceitamos objetos com dimensões tão grandes')
                print('Por favor, entre com as dimensões desejadas novamente')
                continue

            print(f"O volume do objeto é: {volume} cm³")
            return preco

        except ValueError:
            print("Você digitou alguma dimensão do objeto com valor não númerico.")
            print('Por favor, entre com as dimensões desejadas novamente')

def pesoObjeto():
    while True: #garante o Loop até as condições, forem satisfeitas
        try:
            peso = float(input('Digite o peso do objeto (em kg): ')) # Solicita o peso do objeto em quilogramas
            if peso <= 0.1:
                multiplicador = 1 # Define o multiplicador como 1 para objetos com peso menor ou igual a 0.1 kg
            elif 0.1 <= peso < 1:
                multiplicador = 1.5 # Define o multiplicador como 1.5 para objetos com peso entre 0.1 e 0.99 kg
            elif 1 <= peso < 10:
                multiplicador = 2 # Define o multiplicador como 2 para objetos com peso entre 1 e 9.99 kg
            elif 10 <= peso < 30:
                multiplicador = 3 # Define o multiplicador como 3 para objetos com peso entre 10 e 29.99 kg
            else: # se o peso ultrapassar o limite
                print('Não aceitamos objetos tão pesados')
                print('Por favor, entre com o peso desejado novamente')
                continue

            return multiplicador

        except ValueError: # se o usuario digitar uma teclar invalidar
            print("Você digitou peso do objeto com valor não numerico.")
            print('Por favor, entre com o peso desejado novamente')

def rotaObjeto():
    while True: #garante o Loop até as condições, forem satisfeitas
        try: #lista das rotas
            print('Selecione a rota:')
            print('BS - De Belém até São Paulo')
            print('SR - De São Paulo até Rio de Janeiro')
            print('BR - De Brasília até Rio de Janeiro')
            print('RB - De Rio de Janeiro até Brasília')
            rota = input('>> ') # Solicita a rota selecionada

            if rota == "BS":
                pg = 1 # Define o fator de pagamento como 1 para a rota "BS"
            elif rota == "SR":
                pg = 1.2 # Define o fator de pagamento como 1 para a rota "SR"
            elif rota == "BR":
                pg = 1.5 # Define o fator de pagamento como 1.5 para a rota "BR"
            elif rota == "RB":
                pg = 1.5 # Define o fator de pagamento como 1.5 para a rota "RB"
            else: # se o usuario digitar uma rota que não esteja na lista
                print('Você digitou uma rota que não existe')
                continue

            return pg

        except ValueError:
            print("Você digitou um valor inválido.")

print('Bem Vindo A Companhia de Lojistica Wesley rodrigues Gama S.A')
# Mfunção para obter as dimensões do objeto
preco_dimensoes = dimensoesObjeto()

# função para obter o peso do objeto
multiplicador_peso = pesoObjeto()

# função para obter a rota desejada
fator_rota = rotaObjeto()

#calcular o total a pagar
total_pagar = preco_dimensoes * multiplicador_peso * fator_rota

# Calcula e exibe o total a pagar, somando o preço das dimensões, o multiplicador do peso e o fator da rota
print(f'O total a pagar é {total_pagar} (dimensoes: {preco_dimensoes}: Peso {multiplicador_peso} * rota {fator_rota}')
