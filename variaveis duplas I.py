# VAriavel "Tuplas"; é imutavel
#vc usar o indentificado "[]", para selecina a variavel ai dentro
mochila=('Machado', 'Camisa', 'bacon', 'Abacate') #tuplas fica em colcehiites
print(mochila)
print(mochila[0])
print(mochila[-1]) #sinal negativo signica que comceça pelo final
print(mochila[2:])#aqui sem digita nada pega o ultimo numero
print(mochila[0:4])
print(mochila[3])
#outro jeito de usar

print('Separa do codigo1°\n ------------------------------------------------------')
#modo facil;

for item in mochila: #aqui vc pode trocar a variavel no caso coloquei intem, ai so sair um nome por vez não todos
    print(f'na minha casa tem: {item}')


print('Separa do codigo2°\n ------------------------------------------------------')
#outro jeito de usar;

#sinceramente o primeiro modo e mais fácil
tam=len(mochila) #aqui indentifico quantos variaveis tem na variavel mochila
for i in range (0,tam,1): #aqui o tanto de vez que devo repetila
    print(f'na minha casa tem: {mochila[i]}')#a informação fica guardada no na variavel "i"

#outras funçoes junçoes de tuplas

mochila=('Machado', 'Camisa', 'bacon', 'Abacate')
upgrad=('Queijo','canivete') #aqui criou outra variavel para junto com a variavel "mochila"
tudojunto= mochila+upgrad  #aqui crio outra variavel para juntas ela duas
print(tudojunto) #aqui as duas juntas sendo printada