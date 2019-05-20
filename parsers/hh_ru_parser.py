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
    urls = []
    urls.append(url)
    #make first request
    session = requests.Session()
    request = session.get(url, headers=headers)
    
    #chek answer
    if request.status_code == 200:
        print("{}: OK".format(vacancy))
    else:
        return request.status_code
        
    #Found count of pages with our vacancy.
    soup = bs(request.content, "lxml")
    try:
        pagination = soup.find_all('a', attrs={"data-qa":"pager-page"}) #try to find all page_switch elements.
        count = int(pagination[-1].text)
        for i in range (count+1):
            url = "https://perm.hh.ru/search/vacancy?area=72&clusters=true&enable_snippets=true&text={0}&page={1}".format(vacancy,i)
            urls.append(url)
    except IndexError:
        pass
    
    #make soup again for all pages
    for url in urls:
        session = requests.Session()
        request = session.get(url, headers=headers)
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
    
def files_writer(jobs):
    '''
    write our vacancies in file.
    '''
    import csv
    with open ("hh_ru_parsed_jobs.csv","w") as file:
        a_pen=csv.writer(file)
        a_pen.writerow(("Название вакансии","Компания","Ссылка","Оплата труда","Описание вакансии"))
        for job in jobs:
            a_pen.writerow((job["title"],job["company"],job["href"],job["compensation"],job["content"]))


def test():
    '''
    Simple non-unit tests.
    '''
    
    #Test case 1: parsing difference vacancies.
    print ("__TEST CASE: FIND VECANCIES__")
    vacancyes = ['python', 'javascript','юрист','sql','адвокат']
    for vacancy in vacancyes:
        print(len(hh_parser(vacancy)))
    
    #Test case 2: write information about vacancies in file.
    print("__TEST CASE: WRITE INFO IN FILE__")
    files_writer(hh_parser("python"))
    

def main():
    test()

if __name__ == "__main__":
    main()