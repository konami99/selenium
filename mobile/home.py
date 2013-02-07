import time
from menu import Menu
from payment import PaymentMobile

class HomeMobile:
    
        
    def __init__(self,driver,url):
        self._driver = driver
        #if (self._driver.title != 'OurDeal, great daily deals! Enjoy amazing discounts on Restaurants, Massages, Spas, Travel, Activities & More!'):
        self._driver.get(url)
    
    
        
	def sleep(self,seconds):
		time.sleep(seconds)
     
	def clickMenu(self):
       
		elem1 = self._driver.find_element_by_xpath('//*[@id="nav_menu"]/span/span/img')
		elem1.click()
		
		return Menu(self._driver)
       
    
    def clickBuy(self):
        elem1 = self._driver.find_element_by_xpath('//*[@id="buy_buttons_top"]/div[2]/a/span')
        elem1.click()
        return PaymentMobile(self._driver)
    