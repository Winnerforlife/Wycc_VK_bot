import requests
from bs4 import BeautifulSoup as BS

proxies = {
  "http": "185.102.138.148:8080",
  "https": "195.133.238.110:3128"
}

link = 'https://www.youtube.com/channel/UCT2eHBmX3QBDlfU9xmeTxjw?view_as=subscriber'
wycclink = 'https://vk.com/official_group_by_wycc220'

r = requests.get(wycclink, proxies=proxies)
print(r.text)

# html = BS(r.content, 'html.parser')

# for el in html.select('._post'):
#     title = el.select('.wall_text')
#     print(title)