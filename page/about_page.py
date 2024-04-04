from assertpy import assert_that, soft_assertions
from locator.locators import MarketsLocators
from selenium.webdriver.common.by import By


class MarketsPage:
    def __init__(self, driver):
        self.driver = driver

    def goToMarkets(self):
        self.driver.get("https://www.marketwatch.com/markets?mod=top_nav")  
        self.driver.maximize_window() 
        
    def verifyTitle(self):
        with soft_assertions():
            assert_that(self.driver.title).contains("Stock Market News - Bond Market - Currencies Markets - MarketWatch")


    def verifyNavigation(self):
        navList = self.driver.find_element(*MarketsLocators.navList).find_elements(*MarketsLocators.navItem)
        navItems = []
        for x in navList:
            navItems.append(x.text)
        
        with soft_assertions():
            assert_that(navItems).contains("Market Data Center", "U.S. Markets", "Canada", "Europe & Middle East", "Asia", "Emerging Markets", "Latin America", "Earnings")
