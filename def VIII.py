def selecionaOpção(perguntar, maior, menor):
    while True:
        try:
            per=int(input(perguntar))
            if per>=maior and per<=menor:
                print('tem nas opções')
                return per
            else:
                print(f'o numero {per} não tem nas opções')
                print('tente novamente')
                continue
        except:
            print('Somente números')

def cadastraCarro(nome, modelo): #função serve para escreve no arquivo
    try:
        abrirArquivo=open(arquivo,'at')#aqui abrir o arquivo
    except:#se der algum erro ao abrir vai para essa exceção
        print('erro ao abrir o arquivo')
    else:# se tudo der certo o arquivo vai ser escrito aqui
        abrirArquivo.write(f'{nome};{modelo}')#aqui vai escreve no arquivo
    finally:
        abrirArquivo.close()#aqui vai fechar o arquivo

    


#programa principal
arquivo='listaCArros.txt'
while True:
    try:
        print('Olá, seja bem vindo!')
        print('1- Cadastra novo carro')
        print('2- Ver lista de carros cadastrados')
        print('3- sair')
        pergunta=selecionaOpção("Qual número deseja escolher\n>>> ", 1 , 3)
        print(f'vc selecioi {pergunta}')
        if pergunta==1:
            print('CADRASTRA NOVO CARRO')
            nomeCarro=input('Qual o Nome do Carro?\n>>')
            modeloCarro=input('Qual o modelo do carro?\n>>')
            cadastraCarro(nomeCarro, modeloCarro)
    finally:
        print('encerrando')


