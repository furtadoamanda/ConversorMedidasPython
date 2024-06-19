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
