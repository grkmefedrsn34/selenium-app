from instaInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US,tr'})
        self.browser = webdriver.Chrome('chormedriver.exe',chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        
    def sıngIn(self):
        self.browser.get("https://instagram.com/accounts/login/")
        time.sleep(2)
        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(1)
    
    def getFollowers(self):
        self.browser.get(f"https://instagram.com/{self.username}")
        
        followersLink = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click
        time.sleep(3)
        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followersCOUNT = len(dialog.find_elements_by_css_selector("li")) 
        followers = dialog.find_elements_by_css_selector("li")
        
        print(f"first count:{followersCOUNT}")
        
        action = webdriver.ActionChains(self.browser)
        
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            
            newcount = len(dialog.find_elements_by_css_selector("li")) 
            
            if followersCOUNT != newcount:
                followersCOUNT = newcount
                print(f"second count : {newcount}")
                time.sleep(2)
            else:
                break
            
        followerlist = []
        
        
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerlist.append(user)
            
        with open("followers.txt","w",encoding="UTF-8") as file:
            for item in followerlist:
                file.write(item + "\n")    
    
    def followUser(self,username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)
        
        followBtn = self.browser.find_element_by_tag_name("button")
        print(followBtn.text)
        
        if followBtn.text != "Takiptesin":
            followBtn.click()
            time.sleep(1)
        else:
            print("Zaten takiptesin")       
    
    
    def unFollow(self,username):
        self.browser.get("htpps://www.instagram.com/" + username)
        time.sleep(1)
        
        followBTN =  self.browser.find_element_by_tag_name("button")
        
        if followBTN.text == "Takiptesin":
            followBTN.click()
            time.sleep(2)
            self.browser.find_element_by_xpath("//button[text()=Unfollow']").click()
        else:
            print("zaten takip etmiyorsunuz")
        
        
instagram = Instagram(username,password)

instagram.sıngIn()

#instagram.getFollowers()

instagram.followUser("kod_evreni")


#unFollow("kod_evreni")
