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
