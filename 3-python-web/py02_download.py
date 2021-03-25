import requests

res = requests.get('https://sistemas.furg.br/sistemas/dados_abertos/arquivos/sisproj-receitas.csv')

res.raise_for_status()

receitas_file = open('receitas.csv', 'wb')

for chunk in res.iter_content(100000):
    receitas_file.write(chunk)

receitas_file.close()


