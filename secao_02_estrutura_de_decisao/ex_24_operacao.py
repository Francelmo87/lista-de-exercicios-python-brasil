"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >>> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >>> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >>> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >>> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >>> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""


def fazer_operacao_e_classificar(n_1: float, n_2: float, operacao: str):
    """Escreva aqui em baixo a sua solução"""
    if operacao == "+":
        resultado = n_1 + n_2
        print(f'Resultado: {resultado:.2f}')
    elif operacao == "-":
        resultado = n_1 - n_2
        print(f'Resultado: {resultado:.2f}')
    elif operacao == "*":
        resultado = n_1 * n_2
        print(f'Resultado: {resultado:.2f}')
    elif operacao == "/":
        resultado = n_1 / n_2
        print(f'Resultado: {resultado:.2f}')

    paridade_str = positividade_str = inteireza_str = ''

    if resultado % 2 == 0:
        paridade_str = 'par'
    else:
        paridade_str = 'impar'

    if resultado == 0:
        positividade_str = 'neutro'
    elif resultado > 0:
        positividade_str = 'positivo'
    elif resultado < 0:
        positividade_str = 'negativo'

    if resultado // 1 == resultado:
        inteireza_str = 'inteiro'
    else:
        inteireza_str = 'decimal'

    if n_1 // 1 == n_1:
        print(f'Número é {paridade_str}, {positividade_str} e {inteireza_str}.')
    else:
        print(f'Número é {positividade_str} e {inteireza_str}.')
