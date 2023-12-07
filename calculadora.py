from calc2 import soma, sub, div, multi

while True:
    # Apresentação
    print('\n\t\t\t -- Calculadora Simples --\n')

    # Menu
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Sair')

    # Ler a opção do usuário
    op = int(input('\nOpção: '))

    if op in [1, 2, 3, 4]:
        # Entradas
        n1 = int(input('Informe n1: '))
        n2 = int(input('Informe n2: '))

        # Processamento e Saída
        if op == 1:
            total = soma(n1, n2)
            print(f'{n1} + {n2} = {total}')
        elif op == 2:
            total = sub(n1, n2)
            print(f'{n1} - {n2} = {total}')
        elif op == 3:
            total = multi(n1, n2)
            print(f'{n1} * {n2} = {total}')
        elif op == 4:
            if n2 != 0:
                total = div(n1, n2)
                print(f'{n1} / {n2} = {total}')
            else:
                print(f'{n1} / {n2} = 0')
    elif op == 5:
        print('Até Depois!')
        break
    else:
        print(f'Opção {op} incorreta!')