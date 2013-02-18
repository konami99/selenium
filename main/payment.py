from selenium.common.exceptions import NoSuchElementException
from payflow import PayFlowPage

class PaymentPage:
    def __init__(self,driver):
        self._driver = driver
        
        try:
            #<h2>Purchase Information</h2>
            elem = self._driver.find_element_by_xpath('//*[@id="formPayment"]/div[1]/h2')
        except NoSuchElementException:
            raise RuntimeError("this is not PaymentPage")
        
    def clickCheckOutWithCreditCard(self):
        elem1 = self._driver.find_element_by_xpath('//*[@id="formPaymentSubmit"]')
        elem1.click()
        return PayFlowPage(self._driver)
    
    def clickCheckOutWithPaypal(self):
        elem1 = self._driver.find_element_by_xpath('//*[@id="formPayment"]/div[4]/div[8]/input[1]')
        elem1.click()
        #return PayFlowPage(self._driver)
    
    
    def registerAsNewMember(self):
        firstname = self._driver.find_element_by_xpath('//*[@id="member_firstname"]')
        firstname.send_keys("test1")
        
        lastname = self._driver.find_element_by_xpath('//*[@id="member_lastname"]')
        lastname.send_keys("test2")
        
        email = self._driver.find_element_by_xpath('//*[@id="member_email"]')
        email.send_keys("abczzzzzzzzzzzza@gmail.com")
        
        postcode = self._driver.find_element_by_xpath('//*[@id="member_postcode"]')
        postcode.send_keys("2222")
        
    def applyDiscountCode(self):
        discountCode = self._driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div/div[4]/div[2]/a')
        discountCode.click()
        
        
    def applyCredit(self):
        credit = self._driver.find_element_by_xpath('//*[@id="applyCreditBtn"]')
        credit.click()
        
    def enterPhone(self):
        ph = self._driver.find_element_by_xpath('//*[@id="ContactPhone"]')
        ph.send_keys("987654321")
        
        
    def enterShippingDetails(self):
        firstname = self._driver.find_element_by_xpath('//*[@id="ShippingFirstName"]')
        firstname.clear()
        firstname.send_keys("Richardx")
        
        lastname = self._driver.find_element_by_xpath('//*[@id="ShippingLastName"]')
        lastname.clear()
        lastname.send_keys("Choux")
        
        address = self._driver.find_element_by_xpath('//*[@id="ShippingAddress"]')
        address.clear()
        address.send_keys("POBOX Empress St")
        
        suburb = self._driver.find_element_by_xpath('//*[@id="ShippingCity"]')
        suburb.clear()
        suburb.send_keys("Kogarah")
        
        postcode = self._driver.find_element_by_xpath('//*[@id="ShippingPostcode"]')
        postcode.clear()
        postcode.send_keys("2100")
        
        stateOptions = self._driver.find_elements_by_xpath('//*[@id="ShippingStateID"]/option')
        for option in stateOptions: 
            # 1 ACT
            # 2 NSW
            # 8 NT
            # 6 QLD
            # 3 SA
            # 4 TAS
            # 5 VIC
            # 7 WA
            if(option.get_attribute("value")=='8'):
                option.click()
                
        countryOptions = self._driver.find_elements_by_xpath('//*[@id="ShippingCountryID"]/option')
        for option in countryOptions: 
            if(option.get_attribute("value")=='1'):
                option.click()
    
    def enterDealerLocation(self):
        stateOptions = self._driver.find_elements_by_xpath('//*[@id="DealerLocationStateID"]/option')
        for option in stateOptions: 
            # 1 ACT
            # 2 NSW
            # 8 NT
            # 6 QLD
            # 3 SA
            # 4 TAS
            # 5 VIC
            # 7 WA
            if(option.get_attribute("value")=='2'):
                option.click()
                
        locationOptions = self._driver.find_elements_by_xpath('//*[@id="DealerLocationID"]/option')
        count = 0
        for option in locationOptions:
            count+=1
            if(count==2):
                option.click()
      
      
      
    def enterCustomData(self):
        cutomDataOptions = self._driver.find_elements_by_xpath('//*[@id="DealCustomDataID"]/option')
        count = 0
        for option in cutomDataOptions:
            count+=1
            if(count==2):
                option.click()
                
    def enterBuyerOptIn(self):
        pass
    
    
    def enterQuantity(self, quantity):
        increaseButton = self._driver.find_element_by_id('inc')
        for count in range(1, quantity):
            increaseButton.click()
            