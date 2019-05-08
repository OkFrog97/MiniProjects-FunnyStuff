'''
test html parser
'''
from bs4 import BeautifulSoup

file = open('test.html', 'r')

soap=BeautifulSoup(file.read())

