"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    total = valor
    qtd_100 = 0
    ced_100 = 100
    qtd_50 = 0
    ced_50 = 50
    qtd_10 = 0
    ced_10 = 10
    qtd_5 = 0
    ced_5 = 5
    qtd_1 = 0
    ced_1 = 1
    str_100 = str_50 = str_10 = str_5 =str_1 = ''
    while True:
        if total >= ced_100:
            total -= ced_100
            qtd_100 += 1
            if qtd_100 == 1:
                str_100 = f'{qtd_100} nota de R$ 100'
            else:
                str_100 = f'{qtd_100} notas de R$ 100'
        elif total >= ced_50:
            total -= ced_50
            qtd_50 += 1
            if qtd_50 == 1:
                str_50 = f'{qtd_50} nota de R$ 50'
            else:
                str_50 = f'{qtd_50} notas de R$ 50'
        elif total >= ced_10:
            total -= ced_10
            qtd_10 += 1
            if qtd_10 == 1:
                str_10 = f'{qtd_10} nota de R$ 10'
            else:
                str_10 = f'{qtd_10} notas de R$ 10'
        elif total >= ced_5:
            total -= ced_5
            qtd_5 += 1
            if qtd_5 == 1:
                str_5 = f'{qtd_5} nota de R$ 5'
            else:
                str_5 = f'{qtd_5} notas de R$ 5'
        elif total >= ced_1:
            total -= ced_1
            qtd_1 += 1
            if qtd_1 == 1:
                str_1 = f'{qtd_1} nota de R$ 1'
            else:
                str_1 = f'{qtd_1} notas de R$ 1'

        else:

            if qtd_100 and qtd_50 and qtd_10 and qtd_5 and qtd_1 > 0:
                print("'"+str_100 + ', ' + str_50 + ', ' +str_10+ ', ' +str_5 + " e " +str_1 + "'")
            elif qtd_100 and qtd_50 and qtd_5 and qtd_1 > 0:
                print("'" + str_100 + ', ' + str_50 + ', ' + str_5 + " e " + str_1 + "'")
            elif qtd_10 and qtd_1 == 1:
                print("'" + str_10 + " e " + str_1 + "'")
            elif qtd_1 == 1:
                print("'" + str_1 + "'")
            elif qtd_5 >= 1:
                print("'" + str_5 + "'")
            elif qtd_10 == 1:
                print("'" + str_10 + "'")
            break
