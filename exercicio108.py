#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.connectplug.com.br')

except urllib.error.URLError:
    print('o site ConnectPlug não esta acessível no momento')

else:
    print('Sucesso ao acessar o site ConnectPlug')