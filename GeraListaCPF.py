from GeradorCPF import geradoraDeCpf #LEMBRA DE DEIXA NO MESMO DIRETORIO
from random import randint

def GeradorListaCPF():

    quantidade_cpf = randint(1,9) #ARRUMA ISSO DAQUI VELHOOOOOOOOOO SAM BRABA
    lista_cpf = []
    while len(lista_cpf) < quantidade_cpf:
        lista_cpf.append(geradoraDeCpf())

    arquivo = open('ListaCPF.txt', 'a')
    for cpf in lista_cpf:
        arquivo.write(cpf)
        arquivo.write('\n')


GeradorListaCPF()
