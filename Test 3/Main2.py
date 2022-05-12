from argparse import HelpFormatter
import requests
from bs4 import BeautifulSoup

def Pri(Requests):
    filepath = "c:\\Users\\o1030\\Desktop\\work\\Python\\Test 3\\test2.txt" 
    out = open(filepath,"w",encoding = "utf-8")

    Requests = str(Requests)
    out.write(Requests)
    out.close()


if __name__ == '__main__':
    target = "https://cuijiahua.com/blog/2020/04/spider-7.html"
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html,'lxml')
    texts = bs.find('div',id = 'content')
    Pri(texts.text.strip().split('\xa0'*4))