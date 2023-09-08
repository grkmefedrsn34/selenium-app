from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languaesd':'en,en_US,tr'})
        self.browser = webdriver.Chrome('chromedriver.exe',chrome_options = self.browserProfile)
        self.username = username
        self.password = password
        
    def singIN(self):
        self.browser.get("https://Twitter.com/login")   
        time.sleep(2)
        
        usernameInput =  self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]") 
        
        passwordInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")       
        
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        
        btnSubmit = self.browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')   
        
        time.sleep(1)
    
    def search(self,hashtag):
        searchInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        
        searchInput.send_keys(hashtag)
        time.sleep(1)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        loopCounter =  0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight ")
        
        while True :
            if loopCounter > 7:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            
            loopCounter+=1
        
        
        list = self.browser.find_elements_by_xpath('//div[@data-testid="tweet"]/div[2]')
        
        for item in list:
            print("*************************")
            print(item.text)
        print(len(list))
# login

twitter = Twitter(username,password)

twitter.singIN()     
twitter.search("Okul açık")  