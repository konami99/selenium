import time
from selenium.common.exceptions import NoSuchElementException

class PayFlowMobile:
    def __init__(self,driver):
        self._driver = driver
        
    def enterCreditCardDetail(self):
        carNumberField = self._driver.find_element_by_id('cardnum')
        carNumberField.send_keys("5555555555554444")
        
        expiryDateMonthOptions = self._driver.find_elements_by_xpath('//*[@id="expmonth"]/option')
        
        for option in expiryDateMonthOptions:
            if(option.get_attribute("value")=='01'):
                option.click()
                
        expiryDateYearOptions = self._driver.find_elements_by_xpath('//*[@id="expyear"]/option')
        for option in expiryDateYearOptions: 
            if(option.get_attribute("value")=='16'):
                option.click()
                
        cardSecurityCode = self._driver.find_element_by_xpath('//*[@id="cvv2"]')
        cardSecurityCode.send_keys("123")