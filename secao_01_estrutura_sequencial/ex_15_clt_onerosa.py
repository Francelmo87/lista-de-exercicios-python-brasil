"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
Mostrar os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_15_clt_onerosa
    >>> numeros =['80', '55.62']
    >>> ex_15_clt_onerosa.input = lambda k: numeros.pop()
    >>> ex_15_clt_onerosa.calcular_assalto_no_salario()
    + Salário Bruto : R$ 4449.60
    - IR (11%) : R$ 489.46
    - INSS (8%) : R$ 355.97
    - Sindicato ( 5%) : R$ 222.48
    = Salário Liquido : R$ 3381.70

"""


def calcular_assalto_no_salario():
    """Escreva aqui em baixo a sua solução"""

    valor_da_hora = float(input('Digite o valor da hora trabalhada:'))
    hora = int(input('Digite quantas horas você trabalha por mês:'))
    salario_bruto = valor_da_hora * hora
    desconto_ir = salario_bruto * 0.11
    desconto_inss = salario_bruto * 0.08
    desconto_sindical = salario_bruto * 0.05
    salario_liquido_sem_ir = salario_bruto - desconto_inss - desconto_sindical
    salario_liquido = salario_bruto - desconto_ir - desconto_inss - desconto_sindical
    print(f'+ Salário Bruto : R$ {salario_bruto:.2f}\n'
          f'- IR (11%) : R$ {desconto_ir:.2f}\n'
          f'- INSS (8%) : R$ {desconto_inss:.2f}\n'
          f'- Sindicato ( 5%) : R$ {desconto_sindical:.2f}\n'
          f'= Salário Liquido : R$ {salario_liquido:.2f}'
          )