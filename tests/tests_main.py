from main import conversion_binario_for_decimal, conversion_decimal_for_binario

from unittest.mock import Mock, patch
from ward import test

@test("Testando se o ip for nulo deve retornar uma mensagem")
def _():

    params = None
    mensagem_esperada = "Sem dados para conversão de decimal para binário."

    assert conversion_decimal_for_binario(params) == mensagem_esperada
