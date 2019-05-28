'''
Program for taking most interesting (more 500 likes) posts from FOOD PORN vk.com group.
'''

def vk_parser(vk_group="foodporn"):
    #import modules
    import requests
    from bs4 import BeautifulSoup as bs
    
    #system vars
    token = '625109bd625109bd625109bdf2623bc2bc66251625109bd3eba4eb1c9ab68bbea9a3f17' #service key from vk.com API
    version = 5.95
    owner_id = False #id number for path to vk group. If it false - using name(domain) of vk group. 
    
    #id or domain cheker
    if vk_group[0:1] == 'id': #WARRING! ID in group name?
        owner_id = True
    
    #getting info from vk
    response = requests.get("https://api.vk.com/method/wall.get", 
                            params={"access_token":token,
                                    "version":version,
                                    "domain":vk_group})
    data = response.json()
    
    print (data)



def tests():
    pass
    


def main():
    vk_parser()
    

if __name__ == "__main__":
    main()