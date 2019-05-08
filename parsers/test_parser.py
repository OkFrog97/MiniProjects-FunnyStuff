'''
test html parser
'''
from bs4 import BeautifulSoup

file = open('test.html', 'r')

soap=BeautifulSoup(file.read())

content = soap.find('div', class_='some')

print(content.prettify())
