senha_correta = 1234
senha_digitada = ''

while senha_digitada != senha_correta:
    senha_correta = input('Digite a senha:')
if senha_digitada != senha_correta:
    print('Senha errada! Tente novamente')
    print('Acesso Permitido! Bem vindo!')

salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor total das vendas: "))

if vendas <= 1500:
    comissao = vendas * 0.03
else:
    comissao = 1500 * 0.03 + (vendas - 1500) * 0.05

salario_total = salario_fixo + comissao

print(f"Salário total: R$ {salario_total:.2f}")
