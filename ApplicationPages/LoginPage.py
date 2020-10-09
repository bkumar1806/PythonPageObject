from selenium.webdriver.common.by import By
from ApplicationPages.BasePage import BasePage
from ApplicationPages.HomePage import HomePage
from Config.App_Configs import TestData


class LoginPage(BasePage):

    USERNAME = (By.NAME, "ctl00$MainContent$login$ctl03")
    PASSWORD = (By.NAME, "ctl00$MainContent$login$ctl05")
    LOGIN_BUTTON = (By.NAME, "ctl00$MainContent$login$ctl06")
    CREATE_RECORD = (By.XPATH, "//a[text()='Create Record']")
    VIEW_RECORD = (By.XPATH, "//a[text()='View My Records']")
    SEARCH_RECORD = (By.XPATH, "//a[text()='Search Records']")


    def __init__(self, driver):
        super(LoginPage,self).__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

    def is_available(self, locator):
        return self.is_visible(locator)