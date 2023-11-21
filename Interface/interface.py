import PySimpleGUI as sg
from operadores import *

sg.theme('BlueMono')

# Inicializa uma lista para armazenar os valores
expressao_atual = []

# Interface da aplicação
def main():
    layout = [
              [sg.Text('0', font='Arial', size=(30), justification='right', key='Zero')],
              [sg.Button('⌫', size=6)],
              [sg.Button('1', size=6), sg.Button('2', size=6), sg.Button('3', size=6), sg.Button('+', size=6)],
              [sg.Button('4', size=6), sg.Button('5', size=6), sg.Button('6', size=6), sg.Button('-', size=6)],
              [sg.Button('7', size=6), sg.Button('8', size=6), sg.Button('9', size=6), sg.Button('x', size=6)],
              [sg.Button('0', size=6), sg.Button('/', size=6), sg.Button('C', size=6), sg.Button('=', size=6)],
              [sg.Text('0', font='Arial', size=30, key='Resultado')],
              [sg.Button('Sair', font='Arial', size=27)]
    ]

    Janela = sg.Window('Calculadora', layout, resizable=True, return_keyboard_events=True)

    # Eventos como cliques em botões, funções para calcular e exibir valores.
    while True:
        evento, valores = Janela.read()

        if evento == sg.WIN_CLOSED or evento == 'Sair':
            break

        if evento in '\r':
            calcular_expressao(Janela, expressao_atual)

        if evento in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            atualizar_expressao(Janela, expressao_atual, evento)

        elif evento in ('+', '-', 'x', '/'):
            atualizar_expressao(Janela, expressao_atual, ' ' + evento + ' ')

        elif evento in '=':
            calcular_expressao(Janela, expressao_atual)

        elif evento in 'C':
            expressao_atual.clear()
            Janela['Zero'].update('0')
            Janela['Resultado'].update('0')

        elif evento in ('⌫'):
            if expressao_atual:
                expressao_atual.pop()
                Janela['Zero'].update(''.join(expressao_atual) or '0')

    # Fecha o software após a condicional ser executada
    Janela.close()

# Executar o programa
if __name__ == '__main__':
    main()