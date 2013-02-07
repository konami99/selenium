import time
from payment import PaymentPage

class Home:
    
    def __init__(self,driver):
        self._driver = driver
        #if (self._driver.title != 'OurDeal, great daily deals! Enjoy amazing discounts on Restaurants, Massages, Spas, Travel, Activities & More!'):
        #self._driver.get(url)
    
    def removePopup(self):
        elem0 = self._driver.find_element_by_xpath('//*[@id="cboxClose"]')
        elem0.click()
        
        
    def sleep(self,seconds):
        time.sleep(seconds)
     
    def logIn(self, email, password):
       
       # exit()
       elem = self._driver.find_element_by_link_text('Sign In')
       elem.click()
       elem1 = self._driver.find_element_by_xpath('//*[@id="email"]')
       elem1.send_keys(email)
       elem2 = self._driver.find_element_by_xpath('//*[@id="password"]')
       elem2.send_keys(password)
       elem3 = self._driver.find_element_by_xpath('//*[@id="signin"]/div[1]/a/img')
       elem3.click()
       #return LoginPage(self._driver)
   
    def clickBuy(self):
       elem1 = self._driver.find_element_by_xpath('//*[@id="buy_but_top"]/a/img')
       elem1.click()
       return PaymentPage(self._driver)
    