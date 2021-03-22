import utils

saldo_inic = 2000
taxa_mes = 0.01
nmeses = 12

saldo_atual = utils.saldo(saldo_inic, taxa_mes, nmeses)

ret = utils.retirada()

print(f"Saldo final após {nmeses} é {saldo_atual}")