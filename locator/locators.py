from selenium.webdriver.common.by import By

class HomeLocators:
   logo = (By.ID, "mw-logo-title")

class MarketsLocators:
   navList = (By.XPATH, '//*[@id="maincontent"]/div[1]/div[1]/div/div/div[2]/ul')
   navItem = (By.TAG_NAME, "li")


