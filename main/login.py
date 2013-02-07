from selenium.common.exceptions import NoSuchElementException

class LoginPage:
	
	def __init__(self,driver):
		self._driver = driver
		
		elem = self._driver.find_element_by_class_name("login_links_identity")
		print(elem)