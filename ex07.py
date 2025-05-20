dev calcular_votos
try:
    total_eleitores = float(input("Digite o número total de eleitores: "))
    votos_brancos = float(input("Digite o número de votos brancos: "))
    votos_nulos = float(input("Digite o número de votos nulos: "))
    votos_validos = float(input("Digite o número de votos válidos: "))

    
    if total_eleitores <= 0:
        print("Erro: O total de eleitores deve ser maior que zero!")
    elif votos_brancos < 0 or votos_nulos < 0 or votos_validos < 0:
        print("Erro: Os votos não podem ser negativos!")
    elif votos_brancos + votos_nulos + votos_validos != total_eleitores:
        print("Erro: A soma dos votos deve ser igual ao total de eleitores!")
    else:
        # Cálculo dos percentuais
        perc_brancos = (votos_brancos / total_eleitores) * 100
        perc_nulos = (votos_nulos / total_eleitores) * 100
        perc_validos = (votos_validos / total_eleitores) * 100

        
        print(f"Percentual de votos brancos: {perc_brancos:.2f}%")
        print(f"Percentual de votos nulos: {perc_nulos:.2f}%")
        print(f"Percentual de votos válidos: {perc_validos:.2f}%")

except ValueError:
    print("Erro: Digite apenas números válidos!")
