saldo = 2000
taxa_mes = 0.01
nmeses = 12

for i in range(nmeses-1):
    saldo = saldo*taxa_mes + saldo

print(f"Saldo final após {nmeses} é {saldo}")