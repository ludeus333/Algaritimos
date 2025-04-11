senha_correta = 1234
senha_digitada = ''

while senha_digitada != senha_correta:
    senha_correta = input('Digite a senha:')
if senha_digitada != senha_correta:
    print('Senha errada! Tente novamente')
    print('Acesso Permitido! Bem vindo!')
