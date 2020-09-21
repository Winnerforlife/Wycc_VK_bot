import requests
from bs4 import BeautifulSoup as BS

link = 'http://foxtools.ru/Proxy?country=RU&al=True&am=True&ah=True&ahs=True&http=True&https=True'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

def ip_pars():
    
    r = requests.get(link, headers=headers) 

    if r.status_code == 200:
        soup = BS(r.content, "lxml")
        
        for ip in soup.find_all('input', attrs={'class': 'ch'}):
            
            list_ip = {
                'ip': ip.get('value')
            }

            print(list_ip)

    else:
        print("ОШИБКА, ДЕБИЛ!!!!!" + " " + r.status_code)
        
ip_pars()