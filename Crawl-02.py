import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    #req = requests.get('https://secure.e-himart.co.kr/app/login/login?')
    #html = req.text
    html = urlopen("https://secure.e-himart.co.kr/app/login/login?")
    html_2tbk = urlopen("https://secure.e-himart.co.kr/app/goods/goodsDetail?goodsNo=0001444858")
    bsObject = BeautifulSoup(html_2tbk, 'html.parser')
    print(bsObject)
    for link in bsObject.find_all('a'):
        print(link.text.strip(), link.get('href'))

if __name__ == '__main__': main()
