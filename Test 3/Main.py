import requests

def Pri(Requests):
    filepath = "c:\\Users\\o1030\\Desktop\\work\\Python\\Test 3\\test1.txt" 
    out = open(filepath,"w",encoding = "utf-8")


    out.write(Requests)
    out.close()


if __name__ == '__main__':
    target = "http://fanyi.baidu.com"
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    Pri(req.text)
#    print(req.text)   

