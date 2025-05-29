nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M ou F): ").upper()
altura = float(input("Digite a altura (em metros): "))

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print(f"Peso ideal de {nome}: {peso_ideal:.2f} kg")
