print('Bem-vindo à Bao controle de estoque da bicicletaria do Wesley Rodrigues Gama')

def cadastrarPeca():
    # Função para cadastrar uma nova peça.
    # Solicita ao usuário informações como nome, fabricante e valor da peça.
    # Retorna um dicionário com as informações da peça.
    peca = {
        'nome': input('Por favor, entre com o NOME da peça: '),
        'fabricante': input('Por favor, entre com o FABRICANTE da peça: '),
        'valor': float(input('Por favor, entre com o VALOR (R$) da peça: ')),
    }
    return peca


def consultarPeca(pecas):
    # Função para consultar peças.
    # Exibe um menu com opções de consulta e chama as funções correspondentes de acordo com a escolha do usuário.
    # Recebe a lista de peças cadastradas como parâmetro.
    while True:
        print('\nMENU DE CONSULTA')
        print('1 - Consultar Todas as Peças')
        print('2 - Consultar Peças por Código')
        print('3 - Consultar Peças por Fabricante')
        print('4 - Retornar')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            consultarTodasPecas(pecas)
        elif opcao == '2':
            consultarPecasPorCodigo(pecas)
        elif opcao == '3':
            consultarPecasPorFabricante(pecas)
        elif opcao == '4':
            break
        else:
            print('Opção inválida! Digite novamente.')


def consultarTodasPecas(pecas):
    # Função para exibir todas as peças cadastradas.
    # Recebe a lista de peças cadastradas como parâmetro.
    print('\nTODAS AS PEÇAS CADASTRADAS:')
    for peca in pecas:
        info_peca = f'Código: {peca["codigo"]}\nNome: {peca["nome"]}\nFabricante: {peca["fabricante"]}\nValor: R$ {peca["valor"]:.2f}\n'
        print(info_peca)


def consultarPecasPorCodigo(pecas):
    # Função para consultar peças por código.
    # Recebe a lista de peças cadastradas como parâmetro.
    # Solicita ao usuário o código da peça a ser consultada.
    # Se a peça for encontrada, exibe suas informações.
    # Caso contrário, exibe uma mensagem informando que a peça não foi encontrada.
    codigo = input('\nDigite o código da peça: ')
    for peca in pecas:
        if peca['codigo'] == codigo:
            print(f'Código: {peca["codigo"]}')
            print(f'Nome: {peca["nome"]}')
            print(f'Fabricante: {peca["fabricante"]}')
            print(f'Valor: R$ {peca["valor"]:.2f}')
            break
    else:
        print('Peça não encontrada.')


def consultarPecasPorFabricante(pecas):
    # Função para consultar peças por fabricante.
    # Recebe a lista de peças cadastradas como parâmetro.
    # Solicita ao usuário o fabricante da peça a ser consultada.
    # Exibe as informações das peças encontradas pelo fabricante.
    fabricante = input('\nDigite o fabricante da peça: ')
    for peca in pecas:
        if peca['fabricante'] == fabricante:
            print(f'Código: {peca["codigo"]}')
            print(f'Nome: {peca["nome"]}')
            print(f'Fabricante: {peca["fabricante"]}')
            print(f'Valor: R$ {peca["valor"]:.2f}')


def removerPeca(pecas):
    # Função para remover uma peça da lista de peças cadastradas.
    # Recebe a lista de peças cadastradas como parâmetro.
    # Solicita ao usuário o código da peça a ser removida.
    # Se a peça for encontrada, remove-a da lista.
    # Caso contrário, exibe uma mensagem informando que a peça não foi encontrada.
    codigo = input('Digite o código da peça que deseja remover: ')
    for i, peca in enumerate(pecas):
        if peca['codigo'] == codigo:
            del pecas[i]
            print('Peça removida com sucesso.')
            break
    else:
        print('Peça não encontrada.')


def main():
    # Função principal do programa.
    # Exibe um menu com opções e chama as funções correspondentes de acordo com a escolha do usuário.
    pecas = []
    contador = 1

    while True:
        print('\nEscolha a opção desejada:')
        print('1-Cadastrar Peças')
        print('2-Consultar Peças')
        print('3-Remover Peças')
        print('4-Sair')

        opcao = input('>> ')

        if opcao == '1':
            peca = cadastrarPeca()
            peca['codigo'] = str(contador)
            pecas.append(peca)
            contador += 1
            print('Peça cadastrada com sucesso.')
        elif opcao == '2':
            consultarPeca(pecas)
        elif opcao == '3':
            removerPeca(pecas)
        elif opcao == '4':
            break
        else:
            print('Opção inválida! Digite novamente.')

    print('Programa encerrado.')


main()
