# Conversor de Medidas em Python 🔀🐍

Programa criado para praticar os conhecimentos em Python.  
Trata-se de uma aplicação que possibilita que o usuário realize conversões _aproximadas_ de medidas de distância, peso e temperatura.  
O programa é dividido em 5 arquivos, `app.py`, `conversor.py`, `conversor_distancia.py`, `conversor_peso.py` e `conversor_temperatura.py`. Inicarei explicando os três últimos.

### Funções conversoras
Os três arquivos, `conversor_distancia.py`, `conversor_peso.py` e `conversor_temperatura.py`, são destinados a abrigar cada uma das funções conversoras do programa, sendo que todas apresentam um funcionamento e escrita bem semelhantes, de modo que explicarei detalhadamente apenas uma.

##### Conversor de distância:
```python
def conversor_distancia():
    print("""Deseja converter:
[1] - Metros para Pés
[2] - Pés para metros""")
    selecao = int(input("> "))
    if selecao != 1 and selecao != 2:
        print("Seleção inválida.")
    else:
        distancia = float(input("Qual o valor da distância? "))
        if selecao == 1:
            distancia_convertida = distancia * 3.2
            print(f"\n CONVERSÃO: {distancia}m = {distancia_convertida:.2f}ft")
        elif selecao == 2:
            distancia_convertida = distancia / 3.2
            print(f"\n CONVERSÃO: {distancia}ft = {distancia_convertida:.2f}m")
```
As funções conversoras são iniciadas exibindo ao usuário um menu instrutivo, para que seja selecionado se a conversão se dará da medida x para a y ou da y para a x.  
Uma vez informada a seleção, adentramos no bloco if, o qual verifica se foi feita uma seleção válida pelo usuário ou se foi inserido um número diverso. No caso de seleção válida, é solicitado ao usuário o valor da medida a ser convertida sendo, após, iniciado o principal bloco if.  
Neste bloco, são estabelecidas as fórmulas de conversão utilizadas, sendo exibida uma mensagem indicando o valor inicial e o valor já convertido, o qual é arredondado em duas casas decimais, para melhor leitura.  
Observação: o segundo bloco if utiliza um elif em lugar de um else para evitar possíveis erros e, ainda, para tornar o código mais claro ao leitor.

❗Importante ressaltar que são aplicados valores aproximados, não sendo um cálculo exato.

##### Conversor de pesos:
```python
def conversor_peso():
    print("""Deseja converter:
[1] - Quilogramas para Libras
[2] - Libras para Quilogramas""")
    selecao = int(input("> "))
    if selecao != 1 and selecao != 2:
        print("Seleção inválida.")
    else:
        peso = float(input("Qual o valor do peso? "))
        if selecao == 1:
            peso_convertido = peso * 2.2
            print(f"\n CONVERSÃO: {peso}Kg = {peso_convertido:.2f}Lb")
        elif selecao == 2:
            peso_convertido = peso / 2.2
            print(f"\n CONVERSÃO: {peso}Lb = {peso_convertido:.2f}Kg")
```

##### Conversor de temperatura:
```python
def conversor_temperatura ():
    print("""Deseja converter:
[1] - Celsius para Fahrenheit
[2] - Fahrenheit para Celsius""")
    selecao = int(input("> "))
    if selecao != 1 and selecao != 2:
        print("Seleção inválida.")
    else:
        temperatura = float(input("Qual o valor da temperatura? "))
        if selecao == 1:
            temperatura_convertida = (temperatura * 1.8) + 32
            print(f"\n CONVERSÃO: {temperatura}ºC = {temperatura_convertida}ºF")
        elif selecao == 2:
            temperatura_convertida = (temperatura - 32) / 1.8
            print(f"\n CONVERSÃO: {temperatura}ºF = {temperatura_convertida}ºC")
```

### Conversor.py
```python
from conversor_distancia import *
from conversor_peso import *
from conversor_temperatura import *

def conversor():
    print(""" Selecione a conversão desejada:
        [1] - Converter distância (m e ft)
        [2] - Converter peso (Kg e Lb)
        [3] - Converter temperatura (ºC e ºF)
    """)
    selecao_conversor = int(input("> "))

    if selecao_conversor == 1:
        conversor_distancia()
    elif selecao_conversor == 2:
        conversor_peso()
    elif selecao_conversor == 3:
        conversor_temperatura()
    else:
        print("Seleção inválida.")
```
No arquivo `conversor.py` iniciamos importando todas as funções conversoras anteriormente criadas. Em seguida, no escopo da função conversor(), é exibida ao usuário uma mensagem de menu para que selecione qual será a conversão realizada.  
De acordo com a seleção feita pelo usuário, será chamada a função da respectiva conversão desejada e, caso seja inserida uma seleção diversa, o programa exibe a mensagem "Seleção inválida".

## Aplicação principal
Separadas todas as funções em arquivos separados, temos um programa principal com poucas linhas no arquivo `app.py`.
```python
from conversor import *

print(f"{'*' * 10} CONVERSOR DE MEDIDAS EM PYTHON {'*' * 10}\n")
continuar = True

while continuar:
    try:
        conversor()
        print("""\nNova conversão?
        [1] - SIM
        [2] - NÃO""")
        nova_conversao = int(input("> "))
        if nova_conversao != 1:
            print("Encerrando o programa.")
            continuar = False
    except ValueError:
        print("Valor inválido.")

```
Inicialmente, é importado o inteiro teor do módulo `conversor`. A seguir, é exibida a mensagem de boas vindas do programa e definida a variável `continuar` como True.  
A mencionada variável será utilizada no loop while seguinte. Nele, será executada a função conversor() e, após seu encerramento, será exibida uma nova mensagem perguntando ao usuário se deseja fazer uma nova conversão.  
Se o usuário inserir uma opção diversa de [1], será exibida uma mensagem de encerramento e a variável `continuar` passa a ser definida como False, o que encerra o loop e, consequentemente, o programa.  
- Bloco TRY:  
    ⚠️ Um ponto muito relevante do programa é o bloco try - except. Dentro do loop while é definido o referido bloco, de modo que o programa tenta executar todas as linhas de código anteriormente descritas e, caso ocorra a exceção (erro) "ValueError", o programa não será quebrado, mas sim será exibida a mensagem "Valor inválido". Por estar definida dentro do loop while, caso ocorra a exceção, o programa não será encerrado, mas sim o loop continuará sua execução, permitindo que o usuário faça novas conversões.
    _Ou seja, o programa só é encerrado se o usuário não desejar continuar._
