from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest
#from loginmobile import LoginPageMobile
from mobile.home import HomeMobile
from mobile.payment import PaymentMobile

class PD21(unittest.TestCase):
    
    def setUp(self):
       
        self.driver = webdriver.Chrome("E:\ourdeal\selenium\chromedriver")
    
    def test_credit_card_transaction_with_existing_member(self):
        driver = self.driver
        h = HomeMobile(driver,"http://richard.ourdeal.com.au/deal/nifty-spot-adaptor-for-an-iphone-5-delivered")
        paymentMobile = h.clickBuy()
        
        paymentMobile.login()
        paymentMobile.enterPhone()
        #paymentMobile.agreeTC()
        paymentMobile.clickCheckOutWithCreditCard()
        #loginmobile.login()
        #loginmobile.clickSignIn()
       
        
    
        
    def tearDown(self):
        pass
    
    
if __name__ == "__main__":
    unittest.main()









#driver.get("http://richard.ourdeal.com.au")

