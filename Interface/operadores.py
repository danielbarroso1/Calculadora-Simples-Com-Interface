def atualizar_expressao(Janela, expressao_atual, valor):
    expressao_atual.append(valor)
    Janela['Zero'].update(f' ' + ''.join(expressao_atual))


def calcular_expressao(Janela, expressao_atual):
    expressao_str = ''.join(expressao_atual).replace('x', '*')
    try:
        expressao_original = ''.join(expressao_atual).replace('*', 'x')
        resultado = eval(expressao_str)
        Janela['Resultado'].update(f'{expressao_original} = {resultado}')
    except (ZeroDivisionError):
        Janela['Resultado'].update('Erro: Divisão por zero!')
        Janela['Zero'].update('0')
        expressao_atual.clear()
    except (SyntaxError, ValueError):
        Janela['Resultado'].update('0')
