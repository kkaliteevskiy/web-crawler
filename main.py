import requests
from bs4 import BeautifulSoup

vgm_url = 'https://news.ycombinator.com/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

f = open('website.txt', 'w')
links = soup.find_all('a')
valid_links = []#create set of links leading to new websites

for link in links:
    href = link.get('href')
    print(href)
    if href.startswith('https:'):
        valid_links.append(href)



f.write('\n'.join(valid_links))
