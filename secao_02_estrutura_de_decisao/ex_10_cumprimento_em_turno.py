"""
Exercício 10 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

    >>> cumprimentar('M')
    'Bom dia!'
    >>> cumprimentar('m')
    'Bom dia!'
    >>> cumprimentar('V')
    'Boa tarde!'
    >>> cumprimentar('v')
    'Boa tarde!'
    >>> cumprimentar('N')
    'Boa noite!'
    >>> cumprimentar('n')
    'Boa noite!'
    >>> cumprimentar('X')
    'Valor Inválido!'

"""


def cumprimentar(turno: str):
    """Escreva aqui em baixo a sua solução"""

    if turno.upper() == 'M':
        return 'Bom dia!'
    elif turno.upper() == 'V':
        return 'Boa tarde!'
    elif turno.upper() == 'N':
        return 'Boa noite!'
    return 'Valor Inválido!'

    # msgs = {'m': 'Bom dia!', 'v': 'Boa tarde!', 'n': 'Boa noite!', }
    #     return msgs.get(turno.lower(), 'Valor Inválido!')