saldo = 2000
taxa_mes = 0.01
nmeses = 12

i = 0
while i < nmeses-1:
    saldo = saldo*taxa_mes + saldo
    i+=1

print(f"Saldo final após {nmeses} é {saldo}")