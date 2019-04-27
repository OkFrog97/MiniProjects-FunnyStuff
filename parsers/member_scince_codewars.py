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
   
   #catch errors
   
   #find connection date
   
   #sad answer
   
   pass