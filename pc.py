import requests
from bs4 import BeautifulSoup

except_layer = 2
layer = 0

def main():
    url = input("请输入想爬网站：")
    paChong(url)

def paChong(url):
    text = getHTMLText(url)
    lst = getURL(text)
    for u in lst:
        if lst == []:
            break
        paChong(u)

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        return ""

def getURL(text):
    global layer
    global except_layer
    if layer < except_layer:
        layer += 1
        link_lst = []
        soup = BeautifulSoup(text, 'html.parser')
        links = soup.find_all('a')
        for item in links:
            url = item.get('href')
            link_lst.append(url)
        link_lst = list(filter(lambda url_str: 'http' in url_str, link_lst))
        print(link_lst)
        return link_lst
    else:
        l = []
        return l





if __name__ == "__main__":
    main()
