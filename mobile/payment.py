import time
from menu import Menu
from payflow import PayFlowMobile


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
        creditCheckbox = self._driver.find_element_by_xpath('//*[@id="formPayment"]/div[1]/div[3]/div/div[1]/div/label/span/span[2]')
        creditCheckbox.click()
    
    def applyDiscountCode(self):
        discountCodeOptions = self._driver.find_element_by_xpath('//*[@id="discCode"]/option')
        count = 0
        for option in discountCodeOptions:
            count+=1
            if(count==2):
                option.click()
    
    
    def enterPhone(self):
        elem2 = self._driver.find_element_by_xpath('//*[@id="ContactPhone"]')
        elem2.send_keys("543210")
    
    def agreeTC(self):
        tc = self._driver.find_element_by_xpath('//label[@for="iagree"]/span/span[2]')
        tc.click()
        
    def clickCheckOutWithCreditCard(self):
        elem1 = self._driver.find_element_by_link_text("Check out with Credit Card")
        elem1.click()
        return PayFlowMobile(self._driver)
    
    
    
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
                
    def enterShippingDetails(self):
        firstname = self._driver.find_element_by_xpath('//*[@id="ShippingFirstName"]')
        firstname.clear()
        firstname.send_keys("Richardx")
        
        lastname = self._driver.find_element_by_xpath('//*[@id="ShippingLastName"]')
        lastname.clear()
        lastname.send_keys("Choux")
        
        address = self._driver.find_element_by_xpath('//*[@id="ShippingAddress"]')
        address.clear()
        address.send_keys("Empress St")
        
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
                
    def enterCustomData(self):
        cutomDataOptions = self._driver.find_elements_by_xpath('//*[@id="DealCustomDataID"]/option')
        count = 0
        for option in cutomDataOptions:
            count+=1
            if(count==3):
                option.click()
                
    def tickOptInText(self, bool):
        optInCheckBox = self._driver.find_element_by_class_name('ui-checkbox')
        if(bool):
            optInCheckBox.click()