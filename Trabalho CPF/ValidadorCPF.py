def CPF_Valido(cpf):

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

def teste(resultado, esperado):
    if resultado == esperado:
        retorna = 'Tudo correto ||'
    else:
        retorna = 'Algo está errado ||'
    print ('{} obtido: {} || esperado: {}'.format(retorna, repr(resultado), repr(esperado)))

def main():
    teste(CPF_Valido("820.901.628-80"), True)
    teste(CPF_Valido("820.901.628-80"), False)
    teste(CPF_Valido("539535053-51"), True)
    teste(CPF_Valido("539535053-51"), False)
    teste(CPF_Valido("929.103.688.90"), True)
    teste(CPF_Valido("32063930007"), True)
    teste(CPF_Valido("9159308290"), False)
    teste(CPF_Valido(""), False)
    teste(CPF_Valido("00"), False)
    # Ignora erros de digitação se não forem numéricos
    teste(CPF_Valido("681Banininha01821953"), True)
    teste(CPF_Valido("681Banininha0182953"), False)
    teste(CPF_Valido("233864   X   88897"), True)
    teste(CPF_Valido("233864#@!#$@!$88897"), True)

if __name__ == '__main__':
    main()
