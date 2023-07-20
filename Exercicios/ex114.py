import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[031mERRO! SITE INDISPONÍVEL!\033[m')
else:
    print('SITE NO AR!')
    #print(site.read())
