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
    jobs = []
    
    #make request
    session = requests.Session()
    request = session.get(url, headers= headers)
    
    #chek answer
    if request.status_code == 200:
        print("OK")
    else:
        print(request.status_code)
        
    #make vacancy tree
    soup = bs(request.content, "lxml")
    divs = soup.find_all("div", attrs={"data-qa":"vacancy-serp__vacancy"})
        
    #grab information
   
    for div in divs:
        title = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-title"}).text
        href = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-title"})["href"]
        company = div.find('a', attrs={"data-qa":"vacancy-serp__vacancy-employer"}).text
        text1 = div.find('div', attrs={"data-qa":"vacancy-serp__vacancy_snippet_responsibility"}).text
        text2 = div.find('div', attrs={"data-qa":"vacancy-serp__vacancy_snippet_requirement"}).text
        disctription = "{0}\n{1}".format(text1, text2)
        try:
            compensation = div.find('div', attrs={"data-qa":"vacancy-serp__vacancy-compensation"}).text
        except AttributeError:
            compensation = "0"       
        jobs.append({
        "title":title,
        "compensation":compensation,
        "href":href,
        "company":company,
        "content":disctription
        })
    return jobs


def test():
    vacancyes = ['python', 'javascript','юрист','sql','адвокат']
    for vacancy in vacancyes:
        print(hh_parser(vacancy)[0])

def main():
    test()

if __name__ == "__main__":
    main()