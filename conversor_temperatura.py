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
