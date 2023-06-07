#listas
#aqui é so pra mostra as diferenças entre tuplas e lista
mochila=('Machado', 'Camisa', 'bacon', 'Abacate') #tuplas fica em colcehiites
lista=['Machado', 'Camisa', 'bacon', 'Abacate'] #lista fica nisso q n sei o nome kssk
print(lista, mochila) #da pra juntar os dois
print('programa 2\n___________________________________________________________')
#as lista conseguimos alteras as variaveis que estão dentro da lista ex:
lista[2]= 'laranja'#obs trocamos o 'bacon' da lista por laranja
print(lista[2])#agr o dois vale laranja não mais bacon
print('programa 3\n___________________________________________________________')
#acrescentando mais uma variavel
lista.append('ovos') #aqui ele insere no final
print(lista)
#esse outro codigo vai inserir onde vc deterna pra ele;
lista.insert(1,'wesley') #vc pode coloar qulauer numero para deteemina a posição de onde vai fica
print(lista)

print('programa 4\n___________________________________________________________')
#aqui vc remove da lista alguma alguma varivel
del lista[0] #aqui vc consefute remove da lista indicando qual vai sair
print(lista)
#outro jeiro de remove é e espeficando a variavel;
lista.remove('ovos') #removeu ovos da lista
print(lista)

print('programa 5\n___________________________________________________________')
#aqui vc faz copia de outra variavel
x=[1,2,3,4,5,6,7,8]
y=x[:] #somente assim vc pode fazer copia de variaveis se não oq modifica em uma vai modifica na outra
y[0]=10 #aqui eu modifiquei o primeiro numero
y.insert(2,'wesley gostso') #aqui consifo colcoar sem remove o primeirp somente acrescento mais um
print(x)
print(y)