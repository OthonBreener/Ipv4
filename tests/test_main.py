from app.main import conversion_binario_for_decimal, conversion_decimal_for_binario

from unittest.mock import Mock, patch
from pytest import mark, raises


class TestFunctionConversionDecimalForBinario:

    @mark.task
    def testando_se_o_ip_for_nulo_deve_retornar_mensagem_esperada(self):

        params = None
        mensagem_esperada = "Sem dados para conversão de decimal para binário."

        assert conversion_decimal_for_binario(params) == mensagem_esperada

    def testando_se_o_ip_nao_for_nulo(self):

        params = '10.20.12.45'

        import ipdb; ipdb.set_trace()
        conversion_decimal_for_binario(params)
