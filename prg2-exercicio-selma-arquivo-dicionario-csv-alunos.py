#!/bin/env python3
#coding: utf-8
'''
A Selma aponta as compras feitas na cantina em uma planilha no seu computador.
Essa planilha possui duas colunas: nome e valor.
Ela quer que você faça um programa que leia essas informações e grave um 
um novo arquivo CSV contendo o nome de cada cliente e o valor total da dívida. 
Esse arquivo deve ser ordenado pelo valor da dívida, em ordem descrescente
(da maior para a menor dívida).
A planilha pode ser exportada para o formato CSV, para facilitar o acesso.
Recomenda-se que a solução seja feita de forma modularizada, 
cada função cumprindo um objetivo. 
Carregue os dados originais em um dicionário, fazendo a soma. 
Crie um novo arquivo e salve os dados da totalização. 
'''

import operator
from decimal import *
getcontext().prec = 5

def arquivo():
    abrir_arquivo = open('selma.csv','r')
    arquivo = abrir_arquivo.readlines()
    abrir_arquivo.close()
    return arquivo

def formatar_lista():
    lista = arquivo()
    lista_formatada = []
    for item in lista[1:]:
        lista_formatada.append(item.strip('\n'))
    return lista_formatada

def criar_dicionario():
    lista = formatar_lista()
    dicionario = {}
    for item in lista:
        lista_item = item.split(';')
        nome = lista_item[0]
        valor = float(lista_item[1])

        if lista_item[0] in dicionario.keys():
            dicionario[nome] += Decimal(valor)
        else:
            dicionario[nome] = Decimal(valor)
    return dicionario

def ordenar_dicionario():
    dicionario = criar_dicionario()
    dicionario = sorted(dicionario.items(), key=operator.itemgetter(1))
    dicionario = dicionario[::-1]
    return dicionario

def criar_arquivo():
    dicionario = ordenar_dicionario()
    arquivo = open('Planilha Devedores.csv', 'a')
    for tupla in dicionario:
        nome, valor = tupla
        arquivo.write(nome + ',' + str(valor))
        arquivo.write('\n')

criar_arquivo()





