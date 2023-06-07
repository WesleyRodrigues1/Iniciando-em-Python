def nome ():
    nome=input('qual é seu nome? \n>>')
    idade=input('qual vc tem quantos anos? \n>>')
    return nome , idade
while True:
    try:
        print('Olá seja bem vindo')
        lista = int(input('1- Dados Pessoais Nome idade \n>>'))
        if lista == 1:
            dados = nome()
            print(dados)
            continue
        else:
            print('esse numero não existe nas opções \nSelecione um numero da lista')
    except ValueError:
        print('digite apenas numeros inteiros')
        continue


