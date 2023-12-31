from githubuserinfo import username,password
from selenium import webdriver
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    
    def sing_in(self):
        self.browser.get('https://github.com/login')
        time.sleep(2)
        
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        
        
        time.sleep(1)
        
        self.browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[13]').click()
    
    def getFOLLOWERS(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        
        items = self.browser.find_elements_by_css_selector('.d-table.table-fixed')
        
        for i in items:
            self.followers.append(i.find_elements_by_css_selector('.link-gray.pl-1').text)
        
        while True:
            links = self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")
            
            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)

                items = self.browser.find_elements_by_css_selector('.d-table.table-fixed')
                
                for i in items:
                    self.followers.append(i.find_elements_by_css_selector('.link-gray.pl-1').text)
            else:
                break
        else:
            for link in links:
                if link.text == "Next":
                    link.click()
                    time.sleep(2)
                    
                    İitems = self.browser.find_elements_by_css_selector('.d-table.table-fixed')
                
                    for i in items:
                        self.followers.append(i.find_elements_by_css_selector('.link-gray.pl-1').text)
                else:
                    continue      
                    
                    
                    
                    
github = Github(username,password)
github.sing_in()  
github.followers()
print(github.followers)      