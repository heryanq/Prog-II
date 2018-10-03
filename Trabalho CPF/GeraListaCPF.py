from GeradorCPF import geradoraDeCpf #LEMBRAR DE DEIXAR NO MESMO DIRETORIO
from random import randint

def GeradorListaCPF():

    quantidade_cpf = randint(1,9) #Isso deve ser alterado para lista lista com valores maiores ou uma possivel interação do usario com input
    lista_cpf = []
    while len(lista_cpf) < quantidade_cpf:
        lista_cpf.append(geradoraDeCpf())

    arquivo = open('ListaCPF.txt', 'a')
    for cpf in lista_cpf:
        arquivo.write(cpf)
        arquivo.write('\n')


GeradorListaCPF()
