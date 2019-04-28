def get_member_sience(username):
    '''
    Return since data of member connectione to Codewars.
    > Usernames: Fred, John, Michel.
    > get_member_sience (Fred)
    > Oct 2018
    >
    > get_member_sience (John)
    > Jun 2017
    >
    > get_member_sience (Michel)
    > September 2015
    '''
    #import modules
    import requests
    import bs4
    
    #get site and create tags tree
    username_path = "https://www.codewars.com/users/{}".format(username)
    site = requests.get()
    tree_site = bs4.BeautifulSoup (site.text, "html.parser")
    
    #find connection date
    stat = tree_site.select('.stat-box .stat')
    reg_date = stat[3].getText()
    
    #catch errors
    if stat == []:
        return "Username wasn't registrated."
   
    #sed answer
    answer = reg_date[13:]
    return answer
    
def main ():
    print (get_member_sience('VanillaColaKid'))
    print (get_member_sience('jhoffner'))
    print (get_member_sience('dpleshkov'))
    
if __name__ == '__main__':
    main()