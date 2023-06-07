frase=input('digite qual merda que vou mostra só a metadade da palavra: ')
#vc vai usar o comadno "len", serve para conferir quantas letra tem sua frase;
tamanho= len(frase)
print(f'seu nome tem a quantia de {tamanho} letras')
#agora vc vai dividi isto por 2 usando o comando que vc vai ver ai embaixo;
frase2= frase[:int(tamanho/2)]
print(frase2[-2:])