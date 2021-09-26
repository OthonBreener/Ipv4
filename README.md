# Projeto de calculo de rede Ipv4 para fins de aprendizado

Este projeto contém funções que convertem um ip de decimal para binário, binário para decimal, calcula
o ip primário e o ip de broadcast e a mascara de subrede. Para fins de aprendizado está sendo implementado
testes unitários utilizando o ward e unittest.


# Testes com o Pytest

Antes de iniciar os testes lembre de comentar as variáveis de ambiente para não
mandar nenhum teste para o banco de dados.

## Comandos para rodar os Testes

* comando para rodar os testes e mostrar o nome dos testes:
      ```
      pytest -v nome_do_arquivo.py
      ```
* comando para executar os testes e mostrar as saidas do console:
      ```
      pytest -s nome_do_arquivo.py
      ```
* comando para rodar um teste marcado com @mark.task :
      ```
      pytest -m task
      ```
* comando para rodar com o ipd:
      ```
      pytest -m task -s
      ```
* comando para executar todos os testes deste arquivo:
      ```
      pytest tests/test_tasks.py
      ```
* comando para executar todos os testes da pasta tests:
      ```
      pytest
      ```
* comando para rodar os testes e parar com o pdb assim que dê o primeiro erro:
      ```
      pytest --pdb
        ```



## Resumo significado do retorno dos testes:

    * . : Passou
    * F : Falhou
    * x : Falha esperada
    * X : Falha esperada, mas não falhou
    * s : Pulou (skiped)





## bibliotecas instaladas:
    * pytest
    * pytest-cov
    * pytest-mock

## Para exibir o html no firefox, rode:

    1. pytest --cov=.
    2. coverage html
    3. firefox htmlcov/index.html
