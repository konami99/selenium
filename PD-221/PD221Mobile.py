from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest
from mobile.home import HomeMobile
from mobile.payment import PaymentMobile

class PD221Mobile(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("E:\ourdeal\selenium\chromedriver")
        
    def tearDown(self):
        pass
    
    def test_credit_card_transaction_with_existing_member(self):
        driver = self.driver
        h = HomeMobile(driver,"http://richard.ourdeal.com.au/deal/parcfitness-3-month-gym-membership-bellevue-hill-rose-bay-and-gymtime-balgowlah-locations-feb")
        paymentMobile = h.clickBuy()
        
        paymentMobile.login()
        paymentMobile.selectQuantity(3)
        paymentMobile.enterDealerLocation()
        #paymentMobile.applyCredit()
        #paymentMobile.enterPhone()
        #paymentMobile.agreeTC()
        payflowMobile = paymentMobile.clickCheckOutWithCreditCard()
        payflowMobile.enterCreditCardDetail()