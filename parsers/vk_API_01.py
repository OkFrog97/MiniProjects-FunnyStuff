'''
Program for taking most interesting (more 500 likes) posts from FOOD PORN vk.com group.
'''

def vk_parser(vk_group="foodporn"):
    #import modules
    import requsts
    from bs4 import beautifuleSoup as bs
    
    #system vars
    token = '625109bd625109bd625109bdf2623bc2bc66251625109bd3eba4eb1c9ab68bbea9a3f17' #service key from vk.com API
    version = 5.95
    owner_id = False #id number for path to vk group. If it false - using name(domain) of vk group. 
    
    #id or domain cheker
    if vk_group[0:1] == 'id': #WARRING! ID in group name?
        owner_id = True
    
    #getting info from vk
    response = requsts.get("https://api.vk.com/method/wall.get&access_token={0}{}".format(token, 'owner_id' if owner_id else 'domain'))
    
    
    
    
    
    
    
    
    pass


















def tests():
    pass
    


def main()
    pass
    

if __name__ == "__main__":
    main()