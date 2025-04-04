numero_conta = input('digite o numero da conta:')
saldo= float(input('Digite o saldo:'))
debito= float(input('Digite o debito:'))
credito= float(input('digite o credito:'))

saldo_atual= saldo - debito + credito
print('Saldo Atual:', saldo_atual)
if saldo_atual >= 0:
    print('Saldo positivo')
else:
    print('Saldo negativo')
