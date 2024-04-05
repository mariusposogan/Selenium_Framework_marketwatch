from selenium import webdriver
import path_config #Nu uita sa modifici path-ul in fisierul path_config.py cu folderul proiectului tau
import unittest
from page.markets_page import MarketsPage


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_marketsNav(self):
        marketsPage = MarketsPage(self.driver)
        marketsPage.goToMarkets()
        marketsPage.verifyNavigation()

    def test_title(self):
        marketsPage = MarketsPage(self.driver)
        marketsPage.goToMarkets()
        marketsPage.verifyTitle()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()    
