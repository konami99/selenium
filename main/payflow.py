import time
from selenium.common.exceptions import NoSuchElementException

class PayFlowPage:
    def __init__(self,driver):
        self._driver = driver
        #try:
            #<h2>Payment Method</h2>
            #elem = self._driver.find_element_by_xpath('//*[@id="formPayFlow"]/div[5]/div[1]/h2')
        #except NoSuchElementException:
            #raise RuntimeError("this is not PayFlowPage")
        
    def enterCreditCardDetail(self):
        #elem1 = self._driver.find_element_by_xpath('//*[@id="cardname"]')
        #elem1.send_keys("konami99")
        
        elem2 = self._driver.find_element_by_xpath('//*[@id="cardnum"]')
        elem2.send_keys("5555555555554444")
        
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
        
        #time.sleep(5)
        
        #checkBoxi = self._driver.find_element_by_xpath('//*[@id="formPaymentSubmit"]')
        #checkBoxi.click()
        
        #checkBoxi = self._driver.find_element_by_xpath('//*[@id="iagree"]')
        #checkBoxi.click()
        #self._driver.execute_script("$('#iagree').css('display','block')")
        #c = self._driver.execute_script("return document.getElementById('iagree');")
        #self._driver.execute_script("arguments[0].setAttribute('style', 'width:10;height:10');", c)
        #c = self._driver.execute_script("return $('#iagree')[0];")
        #print(c.is_displayed())
        #self._driver.execute_script("$('#iagree').attr('checked',true)")
        #c.click()
        #
        #c.click();
        
    def confirmPayment(self):
        pass
    
    
    def cancelPayment(self):
        cancelLink = self._driver.find_element_by_xpath('//*[@id="cancelPurchase"]')
        cancelLink.click()
    
    