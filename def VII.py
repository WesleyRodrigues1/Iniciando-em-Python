#essa função foi criada para, verifica se os números que eu digitar estão corretas.
def validar_int(pergunta, nun, max):
    while True:
        try: #"perguntar" ta aqui pq ela substitui o texto que vc vai escreve
            x = int(input(pergunta))#esse opção substituir o input de sua pergunta com a variavel "pergunta'
            if nun <= x <= max: #aqui verificar se o numero foi escolhido certo
                return x #aqui retorna o valor la pra cimar
            else: #caso didite o valor invalido a p´ção vem pra car
                print('Opção inválida')
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')

def cria_Arquivo(nomeArquivo): #essa função vai criar um aquivo
    try:
        a = open(nomeArquivo, "wt+")
        a.close()
    except: #caso de algum erro de sintaxi
        print('erro na criação do arquivo!!!!!!!') #caso de algum erro  vai aparecer essa mensagem
    else:
        print(f'aquivo {nomeArquivo} criado com sucesso!!!!')# se não der vai aparece essa msg


def existe_Arquivo(nomeArquivo): #essa função foi criada para abrir o arquivo eu acho ksksksks
    try:
        a= open(nomeArquivo, 'rt') #aqui vc verifica se p arquivo existe, "r" de leitura e "t" de texto tipo de arquivo
        a.close() #fechar o arquivo
    except FileNotFoundError: #aqui se o arqui não existi vai dar erro, ai exeção ta ai pra isso, ai ele dar falso
        return False #se o arqui não exite
    else: #ele vai retorna verdadeiro se o arquivo existi
        return True #se arquivo existi

def listaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

def cadastraJogo (nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('erro de abrir o arquivo')
    else:
        a.write(f'{nomeJogo};{nomeVideogame}\n')
    finally:
        a.close()








#programa principal
arquivo='games.txt' #esse qo nome do arquivo, que vai ser criado ou não
if existe_Arquivo(arquivo): #aqui vai printa se o arquivo existe ou não
    print('arquivo localizado no computador')
else:
    print('Arquivo inexistente, criando aquivo...')
    cria_Arquivo(arquivo) #essa função vai criar o arquivo, caso ele não exista


while True:
    try:
        print('----MENU----')
        print('1 - Cadastra novo item')
        print('2 - Lista cadastro')
        print('3 - Sair')
        op= validar_int('Qual a opção desejada \n>> ', 1 , 3)

        if op == 1:
            print('opção de Cadastra novo item selecionada')
            nomeJogo= input('Qual o nome do Jogo? \n>> ')
            nomeVideogame= input('Qual o nome do Video Game? \n>> ')
            cadastraJogo (arquivo, nomeJogo, nomeVideogame)

        elif op ==2:
            print('opção de Lista cadastro selecionada')
            listaArquivo(arquivo)
        elif op == 3:
            print('encerrando programa...')
            break
    except ValueError:
        print('digite apenas números inteiros')