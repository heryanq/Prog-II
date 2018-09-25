#coding: utf-8

# 08/2006 - Marco André - marcoandre@gmail.com

##Validaçao do CPF
##Os dois dígitos de verificação do CPF (constituído de 9 dígitos) são calculados através de um complicado algoritmo:
##Etapa 1: cálculo de DV1
##Soma 1: soma dos produtos de cada dígito por um peso de 2 a 10, na ordem inversa (do nono para o primeiro).
##Multiplique a soma 1 por 10 e calcule o resto da divisão do resultado por 11. Se der 10, DV1 é zero,
##caso contrário o DV1 é o próprio resto.
##Etapa 2: cálculo de DV2
##Soma 2: soma dos produtos de cada dígito por um peso de 3 a 11, também na ordem inversa.
##Adicione a Soma 2 ao dobro do DV1, multiplique por 10 e calcule o resto da divisão do resultado por 11.
##Se der 10, DV2 é zero, caso contrário o DV2 é o próprio resto.
##Etapa 3: Multiplique DV1 por 10, some com DV2 e você tem o número de controle do CPF.
##Exemplo: para o CPF 398 136 146, temos:
##Etapa 1: 2x6 + 3x4 + 4x1 + 5x6 + 6x3 + 7x1 + 8x8 + 9x9 + 10x3 = 258
##2580 mod 11 = 6, portanto, DV1 = 6
##Etapa 2: 3x6 + 4x4 + 5x1 + 6x6 + 7x3 + 8x1 + 9x8 + 10x9 + 11x3 = 299
##(299 + 6x2)x10 mod 11 = 3150 mod 11 = 8, portanto DV2 = 8
##Etapa 3: DV1x10 + DV2 = 6x10 + 8 = 68, que é o número procurado.

def CPF_Valido(cpf):
    """CPF_Valido(cpf) sendo cpf uma string, com ou sem formatação"""

    cpf_e_valido = True
    cpf_listado = []

    for numero in cpf:
        if numero.isnumeric():
            cpf_listado.append(numero)

    if len(cpf_listado) < 11:
        cpf_e_valido = False
        return cpf_e_valido

    dv1 = 0
    dv2 = 0

    for posicao, numero in enumerate(cpf_listado):
        if posicao < 9:
            dv1 += int(numero) * (10 - posicao)

    dv1 *= 10
    dv1 %= 11

    if dv1 == 10:
        dv1 = 0

    for posicao, numero in enumerate(cpf_listado):
        if posicao < 9:
            dv2 += int(numero) * (11 - posicao)

    dv2 += dv1 * 2
    dv2 *= 10
    dv2 %= 11

    if dv2 == 10:
        dv2 = 0

    for posicao, numero in enumerate(cpf_listado):
        if int(cpf_listado[9]) != dv1 or int(cpf_listado[10]) != dv2:
            cpf_e_valido = False

    return cpf_e_valido

#    return (dv == dvCalculado):                     #retorna um valor lógico

#### ----- Testes ----- ####

def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não.'
    print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
    print ('Valida CPF')
    test(CPF_Valido("93682786953"), True)
    test(CPF_Valido("936.827.869-53"), True)
    test(CPF_Valido("936827869-53"), True)
    test(CPF_Valido("93682786952"), False)
    test(CPF_Valido(""), False)
    test(CPF_Valido("1"), False)

if __name__ == '__main__': #se o módulo for chamado diretamente, executa testes
    main()
