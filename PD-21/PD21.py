from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import unittest
from main.home import Home
from main.signin import SigninPage

class PD21(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome("E:\ourdeal\selenium\chromedriver")
    
    def xtest_credit_card_transaction_with_existing_member(self):
        driver = self.driver
        #h = Home(driver, "http://richard.ourdeal.com.au/deal/byrontrader-silver-yoga-exercise-ball-with-pump")
        #h.removePopup()
        #h.sleep(3)
        #
        #h.logIn("konami99@gmail.com","543210")
        
        #paymentPage = h.clickBuy()
        
        #payFlowPage = paymentPage.clickCheckOutWithCreditCard()
        #payFlowPage.enterCreditCardDetail()
        s = SigninPage(driver, "https://richard.ourdeal.com.au/signin/")
        s.signin("konami99@gmail.com", "543210")
        
    def test_credit_card_transaction_with_new_member(self):
        driver = self.driver
        #h = Home(driver)
        #h.removePopup()
        #h.sleep(3)
        s = SigninPage(driver, "https://richard.ourdeal.com.au/signin/")
        h = s.signin("konami99@gmail.com", "543210")
        
        paymentPage = h.clickBuy()
        paymentPage.registerAsNewMember()
        payFlowPage = paymentPage.clickCheckOutWithCreditCard()
        payFlowPage.enterCreditCardDetail()
        
    def xtest_credit_card_transaction_using_Discount_code(self):
        driver = self.driver
        h = Home(driver,"http://richard.ourdeal.com.au/deal/byrontrader-silver-yoga-exercise-ball-with-pump")
        h.removePopup()
        h.sleep(3)
        #
        h.logIn("konami99@gmail.com","543210")
        
        paymentPage = h.clickBuy()
        paymentPage.applyDiscountCode()
        paymentPage.applyCredit()
        h.sleep(5)
        paymentPage.enterDealerLocation()
        paymentPage.enterCustomData()
        paymentPage.enterPhone()
        payFlowPage = paymentPage.clickCheckOutWithCreditCard()
        payFlowPage.enterCreditCardDetail()
    
    def xtest_Credit_card_transaction_and_then_cancelling_payment_on_credit_payment_screen(self):
        
        driver = self.driver
        h = Home(driver,"http://richard.ourdeal.com.au/deal/quit-cigarettes-forever-hypnotherapy-session")
        h.removePopup()
        h.sleep(3)
        #
        h.logIn("konami99@gmail.com","543210")
        
        paymentPage = h.clickBuy()
        
        payFlowPage = paymentPage.clickCheckOutWithCreditCard()
        payFlowPage.enterCreditCardDetail()
        payFlowPage.cancelPayment()
        
    def xtest_Credit_card_transaction_using_OD_Credit(self):
        driver = self.driver
        h = Home(driver,"http://richard.ourdeal.com.au/deal/four-seasons-tennis-school-three-hours-of-group-tennis-lessons")
        h.removePopup()
        h.sleep(3)
        h.logIn("konami99@gmail.com","543210")
        paymentPage = h.clickBuy()
        paymentPage.applyCredit()
        h.sleep(3)
        paymentPage.enterDealerLocation()
        paymentPage.enterCustomData()
        payFlowPage = paymentPage.clickCheckOutWithCreditCard()
        payFlowPage.enterCreditCardDetail()
    
    
    def xtest_Custom_Fields(self):
        driver = self.driver
        h = Home(driver,"http://richard.ourdeal.com.au/deal/quit-cigarettes-forever-hypnotherapy-session")
        h.removePopup()
        h.sleep(3)
        h.logIn("konami99@gmail.com","543210")
        paymentPage = h.clickBuy()
        paymentPage.enterShippingDetails()
        paymentPage.enterPhone()
        paymentPage.enterDealerLocation()
        paymentPage.enterCustomData()
        payFlowPage = paymentPage.clickCheckOutWithCreditCard()
        payFlowPage.enterCreditCardDetail()
        
    def xtest_Paypal(self):
        driver = self.driver
        h = Home(driver,"http://richard.ourdeal.com.au/deal/quit-cigarettes-forever-hypnotherapy-session")
        h.removePopup()
        h.sleep(3)
        h.logIn("konami99@gmail.com","543210")
        paymentPage = h.clickBuy()
        paymentPage.enterShippingDetails()
        paymentPage.enterPhone()
        paymentPage.enterDealerLocation()
        paymentPage.enterCustomData()
        payPalPage = paymentPage.clickCheckOutWithPaypal()
        
    def tearDown(self):
        pass
    
    
if __name__ == "__main__":
    unittest.main()









#driver.get("http://richard.ourdeal.com.au")

