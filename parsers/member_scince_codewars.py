def get_member_sience(username):
   '''
   Return since data of member connectione to Codewars.
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