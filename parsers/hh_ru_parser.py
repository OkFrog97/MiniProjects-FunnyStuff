#1/usr/bin/evn python3

'''
This program for pasrsing data from hh.ru
'''

def hh_parser(vacancy):
    #import modules
    import requests
    from bs4 import BeautifulSoup as bs
    
    
    headers = {"accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.132"}
    url = "https://perm.hh.ru/search/vacancy?area=72&clusters=true&enable_snippets=true&text={}&page=0".format(vacancy) #page=0 is the first page. (How parse all?)
    
    #make request
    session = requests.Session()
    request = session.get(url, headers= headers)
    
    #chek answer
    if request.status_code == 200:
        print("OK")
    else:
        print(request.status_code)
        
    #make vacancy tree
    soup = bs(request.content, "html.parser")
    divs = soup.find_all("div", attrs={"data-qa":"vacancy-serp__vacancy"})
        
    #grab information
    jobs = []
    for div in divs:
        title = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-title"}).text
        href = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-title"})["href"]
        company = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-employer"}).text
        text1 = div.find('div', attrs={"data-qa":"vacancy-serp__vacancy_snippet__resposibility"}).text
        text2 = div.find('div', attrs={"data-qa":"vacancy-serp__vacancy_snippet__requirement"}).text
        disctription = "{0}\n{1}".format(text1, text2)
        jobs.append = ({
        "Название":title,
        "Ссылка":href,
        "Компания":company,
        "Описнаие вакансии":disctription})


def test():
    vacancyes = ['python'] #'javascript','юрист','sql','адвокат']
    for vacancy in vacancyes:
        hh_parser(vacancy)

def main():
    test()

if __name__ == "__main__":
    main()