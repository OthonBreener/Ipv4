import numpy as np

#binario = str(input("Entre com o ip da sua rede em binário: "))
decimal = str(input("Entre com o ip da sua rede em decimal: "))
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
    #'00001010.00010100.00001100.00101101'


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


def calculo_de_sub_rede(subrede):

    bi = '1010.10100.1100.101101'



conversion = conversion_decimal_for_binario(decimal)
#conversion_bi = conversion_binario_for_decimal(binario)
print(conversion)
