import oauth2
class Twitter:

    def __init__(self, consumerKey, consumerSecret, tokenKey, tokenSecret):
        self.conexao(self, consumerKey, consumerSecret, tokenKey, tokenSecret)

    def conexao(self, consumerKey, consumerSecret, tokenKey, tokenSecret):
        self.consumer = oauth2.Consumer(consumerKey, consumerSecret)
        self.token = oauth2.Token(tokenKey, tokenSecret)
        self.cliente = oauth2.Client(self.consumer, self.token)
        return self.cliente

