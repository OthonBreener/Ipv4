import numpy as np

#binario = str(input("Entre com o ip da sua rede em binário: "))
#decimal = str(input("Entre com o ip da sua rede em decimal: "))
#subrede = str(input("Digite quantos bits possuem a subrede: "))

def conversion_decimal_for_binario(decimal):
    """
    Função que converte o ip de rede de decimal para binário.
    INPUT:
        Ip de rede em decimal
        Exemplo: '10.20.12.45'
    OUTPUT:
        Ip de rede em binário
        Exemplo: '00001010.00010100.00001100.00101101'
    """

    if not decimal:
        return ("Sem dados para conversão de decimal para binário.")

    number_binario = []
    bi = decimal.split('.')

    for i in range(len(bi)):

        foo = []
        bar = True
        number = int(bi[i])

        if number == 1:
            foo.append(str(1))

        elif number == 0:
            foo.append(str(0))

        else:
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


def conversion_binario_for_decimal(binario):
    """
    Função que converte o ip de rede de binario para decimal.
    INPUT:
        Ip de rede em binario
        Exemplo: '00001010.00010100.00001100.00101101'
    OUTPUT:
        Ip de rede em decimal
        Exemplo: '10.20.12.45'
    """

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
    """
    Função que recebe o total de bits de um ip e o ip de rede em formado de string.
    Separa o ip de rede em quatro listas com cada uma contendo 8 caracteres.
    INPUT:
        Total de bits, Ip.
        Exemplo: 32, '00001010000101000000110000101101'
    OUTPUT:
        Ip de rede em lista de quatro elementos
        Exemplo: ['00001010', '00010100', '00001100', '00101101']
    """

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
    """
    Função que realiza o cálculo de subrede de um ip. Recebe o ip da rede e a
    mascara de subrede, com isso calcula quais são os hosts disponiveis no ip
    e retorna a mascara de subrede em binários e decimal.
    INPUT:
        IP da rede em binário e Mascara de Subrede
        Exemplo: '00001010.00010100.00001100.00101101', 26
    OUTPUT:
        Subrede em binário e decimal
        Exemplo: '11111111.11111111.11111111.11000000', '255.255.255.192'
    """

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
    """
    Função que calcula o número de ip da rede (ou ip primário) e o número de ip de broadcast
    (ou último ip).
    INPUT:
        Ip de rede binário, Ip de Subrede binário, Mascara de Subrede
        Exemplo: '00001010.00010100.00001100.00101101', '11111111.11111111.11111111.11000000', 26

    OUTPUT:
        Ip de rede e Ip de broadcast
        Exemplo: '00001010.00010100.00001100.00000000', '00001010.00010100.00001100.00111111'
    """

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

ip = '177.69.128.1'
ip2 = '0'

conversion = conversion_decimal_for_binario(ip2)
print(conversion)
