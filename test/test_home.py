from selenium import webdriver
import path_config 
import unittest
from page.home_page import HomePage

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_logo(self):
        homePage = HomePage(self.driver)
        homePage.goToHome()
        homePage.verifyLogo()

    def test_title(self):
        homePage = HomePage(self.driver)
        homePage.goToHome()
        homePage.verifyLogo()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()    
