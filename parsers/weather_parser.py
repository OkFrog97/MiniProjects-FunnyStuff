'''
This is learning parser. It's get weather.
'''

def get_weather_perm():

    import requests
    import bs4

    site = requests.get("https://sinoptik.com.ru/погода-пермь") #get raw site text

    b = bs4.BeautifulSoup(site.text, "html.parser") #Make tags tree
    '''
    What is tegs tree. Example.
    
    import bs4 
    text = "<HTML><HEAD></HEAD><BODY></BODY></HTML>" - html code in line(without sctucture.
    magic_tails = bs4.BeautifulSoup(text)
    magic_tails.prettyfy()
    #<HTML>
    #  <HEAD>
    #  </HEAD>
    #  <BODY>
    #  </BODY>
    #<HTML>
    It is true magic!
    '''
    
    #Morning temperature
    p3 = b.select('.temperature .p3') #BeautifulSoup object. It is select tags temperature and p3
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
    returned_answer = "Погода в Перми:\nУтром:{0} {1};\nДнем: {2} {3};\n{4}".format(morinig_weather1, morinig_weather2, day_weather1, day_weather2, descript)
    print (returned_answer)

def main():
    get_weather_perm()

if __name__ == '__main__':
    main()