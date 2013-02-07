from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest

# driver = webdriver.Firefox()
# driver = webdriver.Ie("E:\ourdeal\selenium\IEDriverServer")
class OurDeal(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("E:\ourdeal\selenium\chromedriver")
        
    def test_ourdeal(self):
        driver = self.driver
        driver.get("http://www.ourdeal.com.au")
        elem0 = driver.find_element_by_xpath('//*[@id="popup_reg_form_container"]/div/div/div/div/div/a/span')
        elem0.click()
        
        time.sleep(5)
        # exit()
        elem = driver.find_element_by_link_text('Sign In')
        elem.click()
        
        elem1 = driver.find_element_by_xpath('//*[@id="email"]')
        elem1.send_keys("konami99@gmail.com")
        
        elem2 = driver.find_element_by_xpath('//*[@id="password"]')
        elem2.send_keys("543210")
        
        elem3 = driver.find_element_by_xpath('//*[@id="signin"]/div[1]/a/img')
        elem3.click()
        
        elem4 = driver.find_element_by_xpath('//*[@id="login"]/ul/li[5]')
    
        # assert "Python" in driver.title
        
        self.assert_(elem4.__sizeof__()>0, "test")
        # assert 
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()

#assert "Google" in driver.title
#driver.close()