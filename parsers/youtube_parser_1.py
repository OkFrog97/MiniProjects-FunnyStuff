#1/usr/bin/evn python3

'''
This programm is parser for http://www.weblancer.net
'''

#import using libs
import requests
from bs4 import BeautifulSoup


def get_html(url):
    '''
    Return html as text.
    '''
    return requests.get(url).text


def parser (html):
    '''
    Take html and return seatchng data.
    html is raw html text.
    '''
    soup = BeautifulSoup(html)
    #print(soup)
    table = soup.find('____') # '____' is a tag in our site; class_ - tag class; ATTENTION! I must find tag and class for new weblancer interface!!!
    print(table.prettify())










def main ():
    parser(get_html('http://www.yandex.ru'))
    
if __name__ == "__main__":
    main ()