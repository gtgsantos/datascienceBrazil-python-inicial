import requests
import json

def getFilme(filme):
    requisicao = None
    try:
        #www.omdbapi.com
        requisicao = requests.get('http://www.omdbapi.com/?t=' + filme)
        return json.loads(requisicao.text)
    except:
        print ('erro na conexao')
        exit(1)
        return None


dicionario = getFilme('interestellar')
print(dicionario['Response'])
print(dicionario['Error'])