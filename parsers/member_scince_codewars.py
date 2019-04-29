def get_member_since(username):
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
    site = requests.get(username_path)
    tree_site = bs4.BeautifulSoup (site.text, "html.parser")
    
    #find information and catch errors
    stat = tree_site.select('.stat-box .stat')
    if stat == []:
        return "Username wasn't registrated."
    
    #find connection date
    for i in range (len(stat)):
        string_stat = stat[i].getText()
        if 'Member' in string_stat:
           reg_date = string_stat

    return reg_date[13:] #Return answer without "Member since:"


def main ():
    print (get_member_since('VanillaColaKid'))
    print (get_member_since('jhoffner'))
    print (get_member_since('dpleshkov'))


if __name__ == '__main__':
    main()
