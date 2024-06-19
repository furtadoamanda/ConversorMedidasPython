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

