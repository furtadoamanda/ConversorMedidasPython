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