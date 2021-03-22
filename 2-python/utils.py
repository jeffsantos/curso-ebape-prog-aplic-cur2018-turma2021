def saldo(saldo, taxa, meses):
    i = 0
    while i < meses:
        saldo = saldo*taxa + saldo
        i+=1
        
    return saldo

def retirada():
    return 0