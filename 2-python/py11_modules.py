from utils import saldo

saldo_inic = 2000
taxa_mes = 0.01
nmeses = 12

saldo_atual = saldo(saldo_inic, taxa_mes, nmeses)

print(f"Saldo final após {nmeses} é {saldo_atual}")