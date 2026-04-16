# Calcula média - 1 aluno

#n1 = float(input("Nota 1: "))
#n2 = float(input("Nota 2: "))
#media = (n1 + n2) / 2
#print(media)

# Estrutura de repetição (for)

#for i in range(5):
    #print('hello world:')
    
qtd = int(input('quer contar ate quanto? '))
for i in range(qtd):
    print(i,end=" ") # Imprime na mesma linha

for u in range(3):
 print(f'\nRodada {u}')
 num1 = int(input('Informe um numero: '))
 num2 = int(input('Informe um numero: '))
 soma  = num1 + num2 
 print(f'O total é {soma}')

# Variavel Acumuladora
soma = 0 
for i in range(5):
   numero = float(input('Digite um numero:' ))
   soma = soma + numero 

print(f'O total é {soma}')   


soma = 0
for v in range(5):
   venda = float(input('Informe o valor: '))
   
   if venda > 100:
      soma = soma + venda
      print('valor R$ {venda} somado')
else:
      print('valor nao computado')

print(f'\ntotal de R$')