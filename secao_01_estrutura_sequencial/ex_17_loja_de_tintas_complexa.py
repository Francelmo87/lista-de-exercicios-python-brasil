"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 galões de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 galões de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""

import math

def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""

    area = int(input('Digite a área em m² a ser Pintada: '))
    area_com_folga = area * 1.1
    litros_por_m2 = 6
    litros_a_serem_usados = math.ceil(area_com_folga / litros_por_m2)
    print(f'Você deve comprar {litros_a_serem_usados} litros de tinta.')

    litros_por_latas = 18
    numero_de_latas = math.ceil(litros_a_serem_usados / litros_por_latas)
    sobra_da_lata = float(numero_de_latas * litros_por_latas - litros_a_serem_usados)
    valor_da_lata = 80
    valor_com_apenas_latas = numero_de_latas * valor_da_lata
    print(f'Você pode comprar {numero_de_latas} lata(s) de 18 litros a um custo de R$ {valor_com_apenas_latas}. Vão sobrar {sobra_da_lata} litro(s) de tinta.')

    litros_por_galao = 3.6
    numero_de_galoes = math.ceil(litros_a_serem_usados / litros_por_galao)
    sobra_do_galao = float(numero_de_galoes * litros_por_galao - litros_a_serem_usados)
    valor_do_galao = 25
    valor_com_apenas_galoes = numero_de_galoes * valor_do_galao
    print(f'Você pode comprar {numero_de_galoes} galões de 3.6 litros a um custo de R$ {valor_com_apenas_galoes}. Vão sobrar {sobra_do_galao:.1f} litro(s) de tinta.')

    # valor da compra otimizada
    numero_de_latas = math.floor(litros_a_serem_usados / litros_por_latas)
    valor_da_lata = 80
    valor_de_latas = numero_de_latas * valor_da_lata
    litros_faltantes = litros_a_serem_usados % litros_por_latas
    numero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)
    valor_do_galao = 25
    valor_com_galoes = numero_de_galoes * valor_do_galao

    valor_total = valor_de_latas + valor_com_galoes

    print(f'Para menor custo, você pode comprar {numero_de_latas} lata(s) de 18 litros e {numero_de_galoes} galão(ões) de 3.6 litros a um custo de R$ {valor_total}. '
          f'Vão sobrar 2.6 litro(s) de tinta.')



