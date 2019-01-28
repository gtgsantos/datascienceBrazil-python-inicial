import re
import requests

requisicao = requests.get('http://lacoxinha.com.br/contato')
print(requisicao.text)
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text)
print(padrao)

if (padrao):
    print(padrao)
else:
    print('padrao nao encontrado')