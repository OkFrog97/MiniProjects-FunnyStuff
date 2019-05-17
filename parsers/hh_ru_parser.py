#1/usr/bin/evn python3

'''
This program for pasrsing data from hh.ru
'''

def hh_parser(vacancy):
    import requests
    from bs4 import BeautifulSoup as bs
    
    headers = {"accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.132"}
    url = "https://www.hh.ru/search/vacancy?area=72&clusters=true&enable_snippets=true&text={}&page=0".format(vacancy) #page=0 is the first page. (How parse all?)
    
    session = requests.Session()
    request = session.get(url, headers= headers)
    
    if request.status_code == 200:
        print("OK")
    else:
        print(request.status_code)
        
    


def test():
    vacancyes = ['юрист','javascript','python','sql','адвокат']
    for vacancy in vacancyes:
        hh_parser(vacancy)

def main():
    test()

if __name__ == "__main__":
    main()