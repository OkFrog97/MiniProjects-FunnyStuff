#1/usr/bin/evn python3

'''
This programm is parser for http://www.weblancer.net
'''

#import using libs
import requests
import bs4


def get_html(url):
    '''
    Return html as text.
    '''
    return requests.get(url).text


def parser (html):
    '''
    Take html and return seatchng data.
    '''
    soup = sp4.BeautifulSoup(html)











def main ():
    pass
    
if __name__ == "__main__":
    main ()