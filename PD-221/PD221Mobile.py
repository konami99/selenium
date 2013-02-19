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
    
    def xtest_credit_card_transaction_with_existing_member(self):
        driver = self.driver
        h = HomeMobile(driver,"http://richard.ourdeal.com.au/deal/parcfitness-3-month-gym-membership-bellevue-hill-rose-bay-and-gymtime-balgowlah-locations-feb")
        paymentMobile = h.clickBuy()
        
        paymentMobile.login()
        paymentMobile.selectQuantity(2)
        paymentMobile.enterDealerLocation()
        paymentMobile.applyCredit()
        #paymentMobile.enterPhone()
        #paymentMobile.agreeTC()
        #payflowMobile = paymentMobile.clickCheckOutWithCreditCard()
        #payflowMobile.enterCreditCardDetail()
        
        
    def xtest_credit(self):
        driver = self.driver
        h = HomeMobile(driver,"http://richard.ourdeal.com.au/deal/parcfitness-3-month-gym-membership-bellevue-hill-rose-bay-and-gymtime-balgowlah-locations-feb")
        paymentMobile = h.clickBuy()
        
        paymentMobile.login()
        paymentMobile.selectQuantity(2)
        paymentMobile.enterDealerLocation()
        paymentMobile.applyCredit()
        
    def xtest_discount_code(self):
        driver = self.driver
        h = HomeMobile(driver,"http://richard.ourdeal.com.au/deal/parcfitness-3-month-gym-membership-bellevue-hill-rose-bay-and-gymtime-balgowlah-locations-feb")
        paymentMobile = h.clickBuy()
        
        paymentMobile.login()
        paymentMobile.selectQuantity(3)
        paymentMobile.enterDealerLocation()
        paymentMobile.applyDiscountCode()
        
        
    def test_discount_code_plus_credit(self):
        driver = self.driver
        h = HomeMobile(driver,"http://richard.ourdeal.com.au/deal/nifty-spot-in-car-iphone--to-stereo-transmitter")
        paymentMobile = h.clickBuy()
        
        paymentMobile.login()
        paymentMobile.selectQuantity(5)
        paymentMobile.enterShippingDetails()
        paymentMobile.enterDealerLocation()
        paymentMobile.enterCustomData()
        paymentMobile.tickOptInText(0)
        #paymentMobile.applyDiscountCode()
        #paymentMobile.applyCredit()
        paymentMobile.enterPhone()
        payFlowPage = paymentMobile.clickCheckOutWithCreditCard()
        payFlowPage.enterCreditCardDetail()