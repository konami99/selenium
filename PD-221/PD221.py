from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest
from main.home import Home
from main.signin import SigninPage

class PD221(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("E:\ourdeal\selenium\chromedriver")
        
    def xtest_credit_card_transaction_with_existing_member(self):
        driver = self.driver
        
        s = SigninPage(driver, "https://richard.ourdeal.com.au/signin/")
        s.signin("konami99@gmail.com", "543210")
        
        h = Home(driver,"http://richard.ourdeal.com.au/deal/spot-shop-ivew-book-reader")
        paymentPage = h.clickBuy()
        paymentPage.enterCustomData()
        paymentPage.enterPhone()
        paymentPage.enterDealerLocation()
        paymentPage.enterShippingDetails()
        payFlowPage = paymentPage.clickCheckOutWithCreditCard()
        payFlowPage.enterCreditCardDetail()
        
    def test_discount_voucher_and_credits(self):
        
        driver = self.driver
        
        s = SigninPage(driver, "https://richard.ourdeal.com.au/signin/")
        s.signin("konami99@gmail.com", "543210")
        
        h = Home(driver,"http://richard.ourdeal.com.au/deal/spot-shop-ivew-book-reader")
        paymentPage = h.clickBuy()
        paymentPage.enterCustomData()
        paymentPage.enterPhone()
        paymentPage.enterDealerLocation()
        paymentPage.enterShippingDetails()
        paymentPage.applyDiscountCode()
        time.sleep(3)
        payFlowPage = paymentPage.clickCheckOutWithCreditCard()
        payFlowPage.enterCreditCardDetail()
        
    
    def tearDown(self):
        pass