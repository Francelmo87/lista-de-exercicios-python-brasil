"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    # 01/34/6789
    if len(data) == 10:
        if data[2] == '/' and data[5] == '/':
            data_fatiada = data.split('/')
            if int(data_fatiada[1]) == 2:
                if int(data_fatiada[0]) == 29:
                    if int(data_fatiada[2]) % 4 == 0 and int(data_fatiada[2]) % 100 != 0 or \
                            int(data_fatiada[2]) % 400 == 0:
                        return 'Data válida'
                elif int(data_fatiada[0]) <= 28:
                    return 'Data válida'
                return 'Data inválida'
            elif int(data_fatiada[1]) == [1, 3, 5, 7, 8, 10, 12] and int(data_fatiada[0]) <= 31:
                return 'Data válida'
            elif int(data_fatiada[1]) == [4, 6, 9, 11] and int(data_fatiada[0]) <= 30:
                return 'Data válida'
    return 'Data inválida'
