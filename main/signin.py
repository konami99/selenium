from selenium.common.exceptions import NoSuchElementException
from payflow import PayFlowPage
from main.home import Home

class SigninPage:
    
    def __init__(self,driver,url):
        self._driver = driver
        self._driver.get(url)
        
    
    def signin(self, email, password):    
        #elem1 = self._driver.find_element_by_xpath('//form[@id="formSignIn"]/a[1]')
        #elem1.click()
        
        #elem2 = self._driver.find_element_by_id('//*[@id="password"]')
        #elem2.send_keys(password)
        
        #signinButton = self._driver.find_element_by_id('formSignInSubmit')
        #signinButton.click()
        
       elem = self._driver.find_element_by_link_text('Sign In')
       elem.click()
       elem1 = self._driver.find_element_by_xpath('//*[@id="email"]')
       elem1.send_keys(email)
       elem2 = self._driver.find_element_by_xpath('//*[@id="password"]')
       elem2.send_keys(password)
       elem3 = self._driver.find_element_by_xpath('//*[@id="signin"]/div[1]/a/img')
       elem3.click()
       
       #return Home(self._driver)