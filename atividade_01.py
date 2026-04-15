for i in range(10):
    print(f'\naluno {i+1}')
    n1= float(input("Informe a primeira nota do aluno 1: "))
    n2= float(input("Informe a segunda nota do aluno 2: "))
    n3= float(input("Informe a terceira nota do aluno 3: "))
    n4= float(input("Informe a quarta nota do aluno 4: "))

    media = (n1 + n2 + n3 + n4) / 4 
    print(f'A media do aluno é {media}')