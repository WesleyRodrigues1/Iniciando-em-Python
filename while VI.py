while True:
    usuario=input('Qual seu nome; ')

# se der verdaeiro vai liberrar o continue
    if usuario != 'wesley':
        continue #continue serve para pular para proxima etapa sem concluir a primeira
    senha=input('Qual a sua senha')
    if senha== '1234': # se acerta a senha libera o break
        break # breal quebrar o loop (while), e vai pra proximar fazer.

print('acesso concesido')
