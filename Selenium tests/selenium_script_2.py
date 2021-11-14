from sys import maxsize
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains


class PythonOrgSearch(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        

    def test_search_in_python_org(self):
        
        driver = self.driver
        
        driver.get("http://www.google.com")
        time.sleep(2)
        self.assertIn("Google", driver.title)
        elem = driver.find_element(By.CLASS_NAME, "ktLKi")
        elem.click()
        # The ideal web selector order is: id > Name > CSSSelector > XPath.
 
        


if __name__ == "__main__":
    unittest.main()