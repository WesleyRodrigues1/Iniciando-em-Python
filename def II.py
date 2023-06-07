def borda (s1):
    tam= len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

nome=input('qual nome')
nome2=input('qual nome')
    # Programa Principal
borda(nome)
borda(nome2)