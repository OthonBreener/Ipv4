from app.main import conversion_binario_for_decimal, conversion_decimal_for_binario

from unittest.mock import Mock, patch
from pytest import mark, raises


class TestFunctionConversionDecimalForBinario:

    def testando_se_o_ip_for_nulo_deve_retornar_mensagem_esperada(self):

        params = None
        mensagem_esperada = "Sem dados para conversão de decimal para binário."

        assert conversion_decimal_for_binario(params) == mensagem_esperada

    @mark.parametrize(
        'params, resultado_esperado',
        [('1','00000001'),('0','00000000'),('5','00000101')]
    )
    def testando_se_o_ip_for_apenas_um_numero_deve_retornar_resultado_esperado(self, params, resultado_esperado):

        assert conversion_decimal_for_binario(params) == resultado_esperado


    def testando_se_o_ip_for_apenas_o_numero_zero_deve_retornar_resultado_esperado(self):

        params = '0'
        resultado_esperado = '00000000'

        assert conversion_decimal_for_binario(params) == resultado_esperado

    def testando_se_o_ip_for_composto_por_decimais_de_dois_digitos_deve_retornar_resultado_esperado(self):

        params = '10.20.12.45'
        resultado_esperado = '00001010.00010100.00001100.00101101'

        assert conversion_decimal_for_binario(params) == resultado_esperado

    @mark.task
    def testando_se_o_ip_for_composto_por_decimais_de_tres_digitos_deve_retornar_resultado_esperado(self):

        params = '177.69.128.1'
        resultado_esperado = '10110001.01000101.10000000.00000001'

        assert conversion_decimal_for_binario(params) == resultado_esperado
