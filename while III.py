soma= 0
cont= 1
while (cont<=5):
    x = float(input(f'digite a sua {cont}, nota'))
    soma = soma+x
    cont = cont + 1
    print(soma)
media= soma / 5
print(f'a media final e de {media}')

