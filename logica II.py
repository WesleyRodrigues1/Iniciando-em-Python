# dez é maior que um, porem quando boto o 'not' estou negando ou seja estou falando que esta afirmção é
# falsa;
x = 10
y = 1
res = not x>y
print(res)

#usando o 'and' agora, perceber-se que  x realmente é amior que y, aprimeira afirmação está correta, ja a segunda
#que está (==) com esse sinal que signica que ela compara os sinais pra ver se são iguais está incorreta ja
# que o resultado e falso, portanto no and quando um sinal é falso o resultado e falso tbm;
x = 10
y = 1
z = 5.5
res = x > y and z == y
print(res)