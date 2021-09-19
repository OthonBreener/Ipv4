import numpy as np

#binario = str(input("Entre com o ip da sua rede em binário: "))
#decimal = str(input("Entre com o ip da sua rede em decimal: "))
#subrede = str(input("Digite quantos bits possuem a subrede: "))

def conversion_decimal_for_binario(decimal):

    if not decimal:
        return ("Sem dados para conversão de decimal para binário.")

    number_binario = []
    bi = decimal.split('.')

    for i in range(len(bi)):

        foo = []
        bar = True
        number = int(bi[i])

        while bar:

            foo.append(str(number % 2))
            number = int(number / 2)

            if number < 2:
                foo.append(str(1))
                bar = False

        while len(foo) < 8:

            foo.append(str(0))

        foobar = list(reversed(foo))
        number_binario.append(''.join(foobar))

    return ('.'.join(number_binario))

def calculo_de_sub_rede(binario, subrede):

    lista_binarios = binario.split('.')
    number_bits = len(lista_binarios[0]) * 4
    number_bits_disponiveis = number_bits - subrede
    hosts = 2 ** number_bits_disponiveis - 2

    total_bits = 32
    vetor_total_bits = np.arange(total_bits)
    vetor_subrede = [1 for i in range(subrede)]

    a = len(vetor_subrede)
    b = len(vetor_total_bits)

    vetor_subrede_auxiliar = vetor_subrede.copy()
    while  a < b:
        vetor_subrede_auxiliar.append(0)
        a = a + 1

    n = 4
    vetor_subrede_splited = []

    for i in range(total_bits):

        if len(vetor_subrede_splited) == 4:
            break

        start = int(i * (total_bits / n))
        end = int((i+1) * (total_bits / n))
        vetor_subrede_splited.append(vetor_subrede_auxiliar[start:end])

    vetor_subrede_splited_string = []
    for i in vetor_subrede_splited:

        vetor_subrede_splited_string.append([str(j) for j in i])

    binario_subrede = []
    for vector in range(len(vetor_subrede_splited_string)):

        a = ''.join(vetor_subrede_splited_string[vector])
        binario_subrede.append(a)

    binario_subrede = '.'.join(binario_subrede)

    ip_subrede_decimal = conversion_binario_for_decimal(binario_subrede)

    return binario_subrede, ip_subrede_decimal



def conversion_binario_for_decimal(binario):

    if not binario:
        return ("Sem dados para conversão de binário para decimal.")

    conversion_bi = []
    lista_binarios = binario.split('.')

    for i in range(len(lista_binarios)):

        lista_conversao = []
        number = lista_binarios[i]

        for i in number:
            lista_conversao.append(i)

        lista_invertida = list(reversed(lista_conversao))
        pot = np.arange(len(lista_invertida))

        decimal = []
        for i in pot:
            var = 2 ** pot[i] * int(lista_invertida[i])
            decimal.append(var)

        conversion_bi.append(str(sum(decimal)))

    return ('.'.join(conversion_bi))

binario = '00001010.00010100.00001100.00101101'
subrede = 26

#conversion = conversion_decimal_for_binario(decimal)
conversion = calculo_de_sub_rede(binario, subrede)
#conversion_bi = conversion_binario_for_decimal(binario)
print(conversion)
