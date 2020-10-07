import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GetData:

    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox() #Browser trigger

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/') #The website link
        time.sleep(3)
        email = bot.find_element_by_name('username') #username element to located the username entry on the page
        password = bot.find_element_by_name('password') #Password element to located the password entry on the page
        email.clear() #Clear the saved entry if there is any
        password.clear()#Clear the saved entry if there is any
        email.send_keys(self.username) #Auto-entry for the username/email
        password.send_keys(self.password) #Auto-entry for the password
        password.send_keys(Keys.RETURN) #Auto-enter button
        time.sleep(3) #Wait for 3 sec

    #followers/
    def UserData(self, user):
        bot = self.bot
        bot.get('https://www.instagram.com/' + user + '/')  # Search link
        time.sleep(3)  # Wait for 3 sec.

    def FollowersData(self):
       Get = self.bot
       element_text = "followers" 
       Get.find_element_by_xpath('//a[contains(@href, "%s")]' %element_text).click()
       #FD = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
       #Followers_count = FD.text

    def DataScrape(self, user):
      Scrapper = self.bot
      count = 50 # number of data user to scrape
      element_text = "followers" 
      x = datetime.datetime.now()
      account = user #user account name
      for i in range(1,count):
        s = Scrapper.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[%s]' % i)
        Scrapper.execute_script("arguments[0].scrollIntoView();", s)
        time.sleep(1)
        text = s.text
        list = text.encode('utf-8').split()
        dirname = os.path.dirname(os.path.abspath(__file__))
        csvfilename = os.path.join(dirname, account + "-" + element_text + ".txt")
        #file_exists = os.path.isfile(csvfilename)
        f = open(csvfilename,'a')
        f.write(str(list[0]) + "\r\n")
        f.close()
        print('{};{}'.format(i, list[0]))
        if i == (count-1):
          print(x)


def app_process():
        emailInput = '###############' # Please replace the text with you email before debugging
        passwordInput = '#############' # Please replace the text with you password before debugging
        #numOfPosts = int(3) # the number of post you would like to interact with
        userSearch = 'nzr.mutfak' # your Hashtag
        ed = GetData(emailInput, passwordInput)  # Username, Password # HTML
        ed.login()  # Account login trigger
        ed.UserData(userSearch)  # The hash-tag search # HTML
        ed.FollowersData()
        ed.DataScrape(userSearch)


app_process()