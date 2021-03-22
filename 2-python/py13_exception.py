import sys

try: 
    x = int(input("x: "))
    y = int(input("y: "))

except ValueError:
    print("Tipo inválido!!")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Não dá pra dividir por zero!!")
    sys.exit(1)

print(f"{x} / {y} = {result}")

