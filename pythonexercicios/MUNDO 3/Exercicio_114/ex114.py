try:
    import requests
    requests.get('http://www.pudim.com.br')
except:
    print('\33[31mO sate Pudim não está acessível no momento.\33[m')
else:
    print('\33[32mConseguir acessar o site Pudim com sucesso!\33[m')
