from assertpy import assert_that, soft_assertions
from locator.locators import HomeLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToHome(self):
         self.driver.get("https://www.marketwatch.com/")
         self.driver.maximize_window()

    def verifyLogo(self):
        logo = self.driver.find_element(*HomeLocators.logo)
        with soft_assertions():
            assert_that(logo).is_true()

    def verifyTitle(self):
        with soft_assertions():
            assert_that(self.driver.title).contains("MarketWatch: Stock Market News - Financial News - MarketWatch")


