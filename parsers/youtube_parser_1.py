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
    content = soup.find('div', class_='cols_table') #.find find first entry of str in tags. I have tests. It is true.
    print(content.prettify())










def main ():
    parser(get_html('http://www.weblancer.net/jobs'))
    
if __name__ == "__main__":
    main ()