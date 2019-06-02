'''
Program for taking most interesting (more 500 likes) posts from FOOD PORN vk.com group.
'''


def vk_parser(vk_group="fit4life_official"):
    '''
    Return posts from vk.com group.
    '''
    # import modules
    import requests
    from bs4 import BeautifulSoup as bs
    
    # system vars
    token = '625109bd625109bd625109bdf2623bc2bc66251625109bd3eba4eb1c9ab68bbea9a3f17' # service key from vk.com API
    version = 5.95
    offset = 0
    count = 100
    all_posts = []
    
    # getting data from vk
    while offset < 100:
        response = requests.get("https://api.vk.com/method/wall.get", 
                                params={"access_token":token,
                                        "version":version,
                                        "domain":vk_group,
                                        "count":count,
                                        "offset":offset})
    
        data = response.json()['response']['items']
        all_posts.extend(data)
        offset += 10
    

def tests():
    pass


def main():
    vk_parser()


if __name__ == "__main__":
    main()
