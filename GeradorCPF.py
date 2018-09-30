#Foi reutilizado o código presente no validador de cpf, com algumas alterações nos nomes das variáveis, e foi utilizada a biblioteca random

#Código de validar cpf pode ser encontrado em:  github.com/heryanq/Prog-II/blob/master/validaCPF-fazer.py

from random import randint

def gerador_cpf():

    cpf = []
    for numero in range(9):
        cpf.append(randint(0, 9))

    dv1 = 0
    dv2 = 0

    for posicao, numero in enumerate(cpf):
        if posicao < 9:
            dv1 += int(numero) * (10 - posicao)

    dv1 *= 10
    dv1 %= 11

    if dv1 == 10:
        dv1 = 0

    cpf.append(dv1)

    for posicao, numero in enumerate(cpf):
        if posicao < 9:
            dv2 += int(numero) * (11 - posicao)

    dv2 += dv1 * 2
    dv2 *= 10
    dv2 %= 11

    if dv2 == 10:
        dv2 = 0

    cpf.append(dv2)

    cpf_formatado = ''

    for numero in cpf:
        cpf_formatado += str(numero)

    cpf = cpf_formatado

    #Caso a queira gerar o cpf com máscara
    #return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    #return cpf[:9] + '-' + cpf[9:]
    return(cpf)