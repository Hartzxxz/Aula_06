n = 'S'
venda = 0

while n == 'S':
    venda = float(input('Digite o valor das vendas: '))

    soma = n + venda

    n  = input('Quer continuar? [S/N]').upper().strip()

    if n >= 1000:
        desconto = venda * 0.10
        
        total = soma - desconto

        print(f'O valor total com desconto foi de: {soma:.2f}')
        print(f'O desconto foi de: {desconto:.2f}')
    else:
        print(f'O valor das vendas foi de R$: {soma:.2f}')
        print(f'nao teve desconto')