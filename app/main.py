import numpy as np

#binario = str(input("Entre com o ip da sua rede em binário: "))
#decimal = str(input("Entre com o ip da sua rede em decimal: "))
#subrede = str(input("Digite quantos bits possuem a subrede: "))

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


def splited_lista(total_bits, func):

    n = 4
    vetor_subrede_splited = []

    for i in range(total_bits):
        if len(vetor_subrede_splited) == 4:
            break

        start = int(i * (total_bits / n))
        end = int((i+1) * (total_bits / n))
        vetor_subrede_splited.append(func[start:end])

    return vetor_subrede_splited


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

    vetor_subrede_splited = splited_lista(total_bits, vetor_subrede_auxiliar)

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


def primary_and_broadcast_ip(ip_rede_binario, ip_subrede_binario, subrede):

    number_bits = len(ip_rede_binario.split('.')[0]) * 4
    number_bits_disponiveis = number_bits - subrede

    ip_primario = list(''.join(ip_rede_binario.split('.')))
    ip_primario_reverso = list(reversed(ip_primario))
    ip_primario_auxiliar = ip_primario_reverso[number_bits_disponiveis:]

    ip_subrede = list(''.join(ip_subrede_binario.split('.')))
    ip_subrede_reverso = list(reversed(ip_subrede))
    ip_subrede_auxiliar = ip_subrede_reverso[:number_bits_disponiveis]

    primary_ip = list(reversed(ip_primario_auxiliar)) + ip_subrede_auxiliar
    primary_ip_binario = splited_lista(32, ''.join(primary_ip))
    primary_ip_binario_final  = ('.'.join(primary_ip_binario))

    lista_auxiliar = []
    contador = subrede
    while contador < 32:
        lista_auxiliar.append(str(1))
        contador += 1

    ip_broadcast = list(reversed(ip_primario_auxiliar)) + lista_auxiliar
    ip_broadcast_binario = splited_lista(32, ''.join(ip_broadcast))
    ip_broadcast_binario_final = ('.'.join(ip_broadcast_binario))

    return (primary_ip_binario_final, ip_broadcast_binario_final)






ip_subrede_binario = '11111111.11111111.11111111.11000000'
subrede = 26
ip_rede_binario = '00001010.00010100.00001100.00101101'




conversion = calculo_de_sub_rede(ip_rede_binario, subrede)
print(conversion)
