#dev custo_fabrica
custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

percentual_distribuidor = 0.28  # 28%
percentual_impostos = 0.45     # 45%

# Cálculo dos valores
valor_distribuidor = custo_fabrica * percentual_distribuidor
valor_impostos = custo_fabrica * percentual_impostos
custo_final = custo_fabrica + valor_distribuidor + valor_impostos

print(f"O custo final ao consumidor é: R$ {custo_final:.2f}")
