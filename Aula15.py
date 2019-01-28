import requests
import json
import time


requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')

cotacao = json.loads(requisicao.text)


print('###cotacao###')
print('dolar:', cotacao['valores']['USD']['valor'])
print('dolar:', cotacao['valores']['EUR']['valor'])
print('dolar:', cotacao['valores']['BTC']['valor'])
time.sleep(5)