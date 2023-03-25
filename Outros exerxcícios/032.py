import urllib.request
try:
    sate = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O sate Pudim não está acessível no momento.')
else:
    print('Conseguir acessar o site Pudim com sucesso!')
