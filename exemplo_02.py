# Estrutura de repetição
# Numero ate 10 
i = 1 

#while 1 <= 10:
    #print(i)
    #i += 1
# Exemplo 
n = 1
soma = 0
while n != 0:
    n = int(input('Digite um numero: '))
    soma += n

print(f'O total foi: {soma}')

# Exemplo 03
resposta = 'S'
soma = 0 
while resposta != 'N':
    n = int(input('informe um Numero: '))
    soma += n
    resposta = input('Quer continuar? [S/N]').upper().strip()

print (f'o total da soma é: {soma}')