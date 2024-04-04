from selenium import webdriver
import path_config #Nu uita sa modifici path-ul in fisierul path_config.py cu folderul proiectului tau
import unittest
from page.about_page import MarketsPage


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_aboutNav(self):
        aboutPage = MarketsPage(self.driver)
        aboutPage.goToMarkets()
        aboutPage.verifyNavigation()

    def test_title(self):
        aboutPage = MarketsPage(self.driver)
        aboutPage.goToMarkets()
        aboutPage.verifyTitle()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()    
