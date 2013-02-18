import time
from menu import Menu


class PaymentMobile:
    def __init__(self,driver):
        self._driver = driver
        
        
    def login(self):
        elem3 = self._driver.find_element_by_xpath('//*[@id="account_container"]/div[1]/h3/a/span')
        elem3.click()
        
        
        elem1 = self._driver.find_element_by_xpath('//*[@id="signin_email"]')
        elem1.send_keys("konami99@gmail.com")
        
        elem2 = self._driver.find_element_by_xpath('//*[@id="signin_password"]')
        elem2.send_keys("543210")
        
        
        
        
        elem4 = self._driver.find_element_by_xpath('//*[@id="signInSubmit"]/span/span[1]')
        elem4.click()
        
    def applyCredit(self):
        pass
    
    
    def applyDiscountCode(self):
        pass
    
    
    def enterPhone(self):
        elem2 = self._driver.find_element_by_xpath('//*[@id="ContactPhone"]')
        elem2.send_keys("543210")
    
    def agreeTC(self):
        tc = self._driver.find_element_by_xpath('//label[@for="iagree"]/span/span[2]')
        tc.click()
        
    def clickCheckOutWithCreditCard(self):
        elem1 = self._driver.find_element_by_link_text("Check out with Credit Card")
        elem1.click()
        
    
    def enterDealerLocation(self):
        
        stateOptions = self._driver.find_elements_by_xpath('//*[@id="DealerLocationStateID"]/option')
        count = 0
        for option in stateOptions:
            count+=1
            if(count==1):
                option.click()
    
        count = 0
        locationOptions = self._driver.find_elements_by_xpath('//*[@id="DealerLocationID"]/option')
        for option in locationOptions: 
            count+=1
            if(count==2):
                option.click()
                
    def selectQuantity(self, quantityz):
        quantityOptions = self._driver.find_elements_by_xpath('//*[@id="quantity"]/option')
        for option in quantityOptions: 
            if(int(option.get_attribute("value"))==quantityz):
                option.click()