import requests
from bs4 import BeautifulSoup

def get_100_url(url = str('https://news.ycombinator.com/')):

    if not isinstance(url, str):
        
        raise Exception('url is not string type')

    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    f = open('website.txt', 'w')
    links = soup.find_all('a')
    valid_links = []#create set of links leading to new websites
    valid_links.append(url)
    
    i = 0

    while len(valid_links) < 100:
        new_url = valid_links[i]
        i += 1
        new_html_text = requests.get(new_url).text # open new url to gwt more links
        soup = BeautifulSoup(new_html_text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href.startswith('https:') and ~(href in valid_links): # check link validity and check if it is not already in the list
                valid_links.append(href)
            if len(valid_links) == 100: # stop when the list has 100 elements
                break

    f.write('\n'.join(valid_links))
    print('\n'.join(valid_links))

    return valid_links


get_100_url()