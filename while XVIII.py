while True:
    try: #tentar exexulta linha de baixo
        x = int(input('Por favor digite um número: '))
        break
    except ValueError: #não dogitpu numero inteiro caor aqui
        print('Oops! Número inválido. Tente novamente...')