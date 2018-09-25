#!/bin/env python3
# coding: utf-8   
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 0b

# Entregar por e-mail para marcoandre@ifc-araquari.edu.br
# com o assunto: prg2: lista0b.
# Envie um arquivo zip com o nome no formato seu_nome.zip.

# 1. Crie uma função que leia um endereço IP no formato a.b.c.d e retorne
# se ele é ou não um IP válido.nnn

def abrir_ips():
    abrir = open('ips.txt', 'r')
    lista_ips = abrir.readlines()
    return lista_ips


def lista_ips():
    lista_ips = abrir_ips()
    lista_ips_formatada = []
    for ip in lista_ips:
        lista_ips_formatada.append(ip.strip('\n'))
    return lista_ips_formatada


def ip_e_valido():
    ips = lista_ips()
    e_valido = True
    for ip in ips:
        ip_quebrado = ip.split('.')
        for numero in ip_quebrado:
            numero = int(numero)
            if numero >= 0 and numero <= 255:
                pass
            else:
                e_valido = False
                break
    return e_valido

# 2. Faça um programa que leia um arquivo contendo uma lista de endereços
# IP no formato a.b.c.d e gere um arquivo com os IPs válidos e outro com
# os IPs inválidos.

def listar_ips():
    ips = lista_ips()
    ips_validos = []
    ips_invalidos = []
    for ip in ips:
        if ip_e_valido() == True:
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

    print(ips_validos,ips_invalidos)

def criar_arquivo():

    invalidos = open("ips_invalidos.txt", "w")
    invalidos.write(ips_invalidos)
    invalidos.close()

    validos = open("ips_validos.txt", "w")
    validos.write(ips_validos)
    validos.close()

# 3. Faça um programa que leia os três arquivos com os IPs e crie uma
# página HTML básica, contendo a lista completa desses IPs,
# e depois a lista dos válidos e inválidos.

# 4. Faça um programa que leia o arquivo alice.txt
# (ou outro arquivo semelhante à sua escolha)
# e mostre as dez palavras que aparecem com mais frequência no texto.

def texto():
    abrir = open('alice.txt', 'r')
    texto = abrir.readlines()
    return texto

def texto_limpo():
    novo_texto = texto()
    novo_texto_listado = []
    for palavra in novo_texto:
            novo_texto_listado.append(palavra.strip('\n'))
    print(novo_texto_listado)

def contagem_de_palavras():
    texto_listado = texto()
    palavras = {}
    for palavra in sorted(texto_listado):
        palavras[palavra] = palavras.get(palavra,0) + 1

    print(palavras)