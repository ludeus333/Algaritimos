# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
# Função para calcular o salário total
def calcular_salario(horas_trabalhadas, salario_por_hora):
    # Definindo a quantidade de horas regulares semanais
    horas_regulares_semanais = 40
    horas_por_mes = horas_regulares_semanais * 4  # 4 semanas no mês
    
    # Calcular o salário base para o mês
    salario_base = horas_por_mes * salario_por_hora
    
    # Calcular horas extras
    if horas_trabalhadas > horas_por_mes:
        horas_extras = horas_trabalhadas - horas_por_mes
        valor_hora_extra = salario_por_hora * 1.5  # 50% de acréscimo
        salario_extra = horas_extras * valor_hora_extra
    else:
        salario_extra = 0
    
    # Calcular o salário total
    salario_total = salario_base + salario_extra
    return salario_total

# Exemplo com números
horas_trabalhadas = 180  # número de horas trabalhadas no mês
salario_por_hora = 20    # salário por hora

# Calcular o salário total
salario_total = calcular_salario(horas_trabalhadas, salario_por_hora)

# Exibir o resultado
print(f"O salário total do funcionário é: R${salario_total:.2f}")
