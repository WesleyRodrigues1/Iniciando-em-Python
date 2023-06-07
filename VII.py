nome=input('qual o nome do funcionario: ')
ano1=int(input('qual ano que entrou na empresa: '))
ano2=int(input('qual ano estamos: '))
salario=int(input('qual o seu salario: '))
s=ano2-ano1
if s>=5:
    re= salario*0.2
else:
    re= salario*0.1
print(f'voce tem {s} anos, na empresa')
print(f'seu salario é de R${salario}')
print(f'sua bonificação é de RS{re:.0f}')
print(f'{nome} seu salario final e de R${salario+re:.2f}')