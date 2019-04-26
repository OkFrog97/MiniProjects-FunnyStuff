'''
This il learning parser.
'''

import requests

import bs4

site = requests.gets("https://sinoptik.com.ru/погода-пермь")

b = bs4.BeautifulSoup(site.text, "html.parser")

#Morning temperature

p3 = b.select('.temperature .p3')

morinig_weather1 = p3[0].getText()

p4 = b.select('.temperature .p4')

morinig_weather2 = p4[0].getText()

#Day temperature

p5 = b.select('.temperature .p5')

day_weather1 = p5[0].getText()

p6 = b.select('.temperature .p6')

day_weather2 = p6[0].getText()

#Weather description

tmp_dsc = b.select('.rSide .description')
descript = (tmp_dsc[0].getText()).strip()

#Return answer
returned_answer = "Погода в Перми:\nУтром:{0}-{1};\nДнем: {2}{3};\n{4}".format(morinig_weather1, morinig_weather2, day_weather1, day_weather2, descript)
print (returned_answer)
