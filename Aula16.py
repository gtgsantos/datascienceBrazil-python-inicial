import oauth2
import json
import pprint
import urllib.parse


#python_sangz

consumerKey = 'nononon'

consumerSecretKey = 'nononon'

accessToken = 'nononon'


accessTokenSecret = 'nononon'


consumer = oauth2.Consumer(consumerKey, consumerSecretKey)
token = oauth2.Token(accessToken, accessTokenSecret)

cliente = oauth2.Client(consumer, token)
#query = input("novo tweet: ")
#queryCodificada = urllib.parse.quote(query, safe='')

req = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=bolsonaro')

decodeBytes = req[1].decode()

jsonLoad = json.loads(decodeBytes)

contador = len(jsonLoad['statuses'])

for i in jsonLoad['statuses']:
    pprint.pprint(i['text'])