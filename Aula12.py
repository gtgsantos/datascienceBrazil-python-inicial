import sys
import time
import requests



requisicao = requests.get('https://solyd.com.br')

print(requisicao)
print(type(requisicao))
print(requisicao.status_code)