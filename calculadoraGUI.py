# Interface Gráfica
import PySimpleGUI as sg
from calc2 import soma, sub, multi, div

layout = [
    [sg.Text('Escolha a Operação:')],
    [sg.Radio('Adição', 'operacao', key='adição'), sg.Radio('Subtração', 'operacao', key='subtracao')],
    [sg.Radio('Multiplicação', 'operacao', key='multiplicacao'), sg.Radio('Divisão', 'operacao', key='divisao')],
    [sg.Text('Informe o Primeiro Número: '), sg.InputText(key='num1')],
    [sg.Text('Informe o Segundo Número: '), sg.InputText(key='num2')],
    [sg.Text('Resultado:'), sg.Text('', key='resultado')],
    [sg.Button('Calcular'), sg.Button('Limpar'), sg.Button('Sair', button_color=('white', 'red'))],
]

janela = sg.Window('Calculadora Simples', layout)

while True:
    evento, valores = janela.read()

    if evento == sg.WIN_CLOSED or evento == 'Sair':
        break
    elif evento == 'Limpar':
        for key in ['num1', 'num2', 'resultado']:
            janela[key].update('')
        janela['num1'].set_focus()
    elif evento == 'Calcular':
        num1_str = valores['num1']
        num2_str = valores['num2']

        if not num1_str or not num2_str:
            sg.popup_error("Informe valores para os dois números.")
            continue

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
        except ValueError:
            sg.popup_error("Os valores informados não são números válidos.")
            continue

        operacao = None

        for op in ['adição', 'subtracao', 'multiplicacao', 'divisao']:
            if valores[op]:
                operacao = op
                break

        if operacao is not None:
            if operacao == 'adição':
                resultado = soma(num1, num2)
                janela['resultado'].update(f'{num1} + {num2} = {resultado}')
            elif operacao == 'subtracao':
                resultado = sub(num1, num2)
                janela['resultado'].update(f'{num1} - {num2} = {resultado}')
            elif operacao == 'multiplicacao':
                resultado = multi(num1, num2)
                janela['resultado'].update(f'{num1} * {num2} = {resultado}')
            elif operacao == 'divisao':
                if num2 != 0:
                    resultado = div(num1, num2)
                    janela['resultado'].update(f'{num1} / {num2} = {resultado}')
                else:
                    janela['resultado'].update(f'{num1} / {num2} = 0')
        else:
            sg.popup_error("Escolha uma operação antes de calcular!")

janela.close()

