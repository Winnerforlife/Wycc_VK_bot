import requests
from bs4 import BeautifulSoup as BS

link = 'https://spys.one/proxys/RU/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

def ip_pars():
    
    r = requests.get(link, headers=headers) 

    if r.status_code == 200:
        soup = BS(r.content, "lxml")

        # table = soup.find('tr', attrs={'class': 'spy1xx'})
        x = soup.find('td', attrs={'colspan': '1'})
        ip_info = x.find_all('font', attrs={'class': 'spy14'})
        
        for ip in ip_info:
            data = {
                'ip': ip.text
            }

            print(data)
    else:
        print("ОШИБКА, ДЕБИЛ!!!!!" + " " + r.status_code)
        
ip_pars()