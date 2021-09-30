from app.main import conversion_binario_for_decimal, conversion_decimal_for_binario

from unittest.mock import Mock, patch
from pytest import mark, raises


class TestFunctionConversionDecimalForBinario:

    def test_se_o_ip_for_nulo_deve_retornar_mensagem_esperada(self):

        params = None
        mensagem_esperada = "Sem dados para conversão de decimal para binário."

        assert conversion_decimal_for_binario(params) == mensagem_esperada

    @mark.parametrize(
        'params, resultado_esperado',
        [('1','00000001'),('0','00000000'),('5','00000101')]
    )
    def test_se_o_ip_for_apenas_um_numero_deve_retornar_resultado_esperado(self, params, resultado_esperado):

        assert conversion_decimal_for_binario(params) == resultado_esperado

    def test_se_o_ip_for_apenas_o_numero_zero_deve_retornar_resultado_esperado(self):

        params = '0'
        resultado_esperado = '00000000'

        assert conversion_decimal_for_binario(params) == resultado_esperado

    def test_se_o_ip_for_composto_por_decimais_de_dois_digitos_deve_retornar_resultado_esperado(self):

        params = '10.20.12.45'
        resultado_esperado = '00001010.00010100.00001100.00101101'

        assert conversion_decimal_for_binario(params) == resultado_esperado

    def test_se_o_ip_for_composto_por_decimais_de_tres_digitos_deve_retornar_resultado_esperado(self):

        params = '177.69.128.1'
        resultado_esperado = '10110001.01000101.10000000.00000001'

        assert conversion_decimal_for_binario(params) == resultado_esperado

class TestFunctionConversionBinaroForDecimal:

    def test_se_o_ip_em_binario_for_none_deve_retornar_mensagem_esperada(self):

        params = None
        mensagem_esperada = "Sem dados para conversão de binário para decimal."

        assert conversion_binario_for_decimal(params) == mensagem_esperada

    def test_se_o_ip_for_um_unico_zero_deve_retornar_resultado_esperado(self):

        params = '0'
        resultado_esperado = '0'

        assert conversion_binario_for_decimal(params) == resultado_esperado

    def test_se_o_ip_for_um_unico_um_deve_retornar_mensagem_esperada(self):

        params = '1'
        resultado_esperado = '1'

        assert conversion_binario_for_decimal(params) == resultado_esperado

    def test_se_o_ip_for_composto_por_dois_numeros_um_zero_e_um_one_deve_retornar_resultado_esperado(self):

        params = '01'
        resultado_esperado = '1'

        assert conversion_binario_for_decimal(params) == resultado_esperado

    @mark.task
    def test_se_o_ip_for_composto_por_dois_numeros_um_one_e_um_zero_deve_retornar_resultado_esperado(self):

        # erro nesse teste

        params = '10'
        resultado_esperado = ''

        import ipdb;ipdb.set_trace()
        conversion_binario_for_decimal(params)
