import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Osite pudim não esta disponivel no momento')
else:
    print('Consegui acessar o site pudim com sucesso')
    print(site.read())