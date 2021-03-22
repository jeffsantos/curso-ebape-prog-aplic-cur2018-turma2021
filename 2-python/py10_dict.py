contato1 = {"nome":"Jefferson", "endereco":"Leme", "idade":44}

meuconjunto = set() #diferente de {}

#print(contato1["nome"])

contato1["nome"] = "Jefferson Santos"

#print(contato1["nome"])

contato1["telefone"] = ["21-99999-9999", "21-2758-9696"]

#print(contato1)

contato2 = {"nome":"Joao", "endereco":"Copa", "idade":24, "telefone":["21-98888-6565"]}

agenda = [contato1, contato2]

total_tel_1 = len(agenda[0]["telefone"])
total_tel_2 = len(agenda[1]["telefone"])

print(f"Qte telefones do Contato 1: {total_tel_1}")
print(f"Qte telefones do Contato 2: {total_tel_2}")

print(agenda[1]["telefone"][0])