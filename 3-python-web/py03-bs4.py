import sys, webbrowser, requests, bs4

# Executa uma query no pypi, passando uma palavra-chave vinda do terminal

url = 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])

print(url)

res = requests.get(url)

res.raise_for_status()

# Navegar pelos resultados

soup = bs4.BeautifulSoup(res.text, 'html.parser')

snippets = soup.select('.package-snippet')


# Abrir cada link de resultado em uma aba do browser
numOpen = min(5, len(snippets))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + snippets[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)


    