from selenium.webdriver.common.by import By
from ApplicationPages.BasePage import BasePage


class HomePage(BasePage):

    WELCOME_NOTE = (By.XPATH,"//div[@class='main']/h2")
    SETUP_TEAM_REMINDERS = (By.XPATH, "//a[text()='Setup Team Reminders']")
    HOW_TO_REPORT_TESTING_DATA = (By.XPATH, "//a[text()='How To Report Testing Data']")
    CALCULATE_RELIABILITY = (By.XPATH, "//a[text()='Calculate Reliability']")
    VIEW_REPORTED_BUGS_N_HOURS = (By.XPATH, "//a[text()='View Reported Bugs & Hours']")
    ABT_RELIABILITY_CALC = (By.XPATH, "//a[text()='About Reliability Calculations']")
    ADMIN_SETTINGS = (By.XPATH, "//a[text()='Admin Settings']")


    def __init__(self,driver):
        super(HomePage,self).__init__(driver)

    def get_welcome_text(self):
        element = self.element_text(self.WELCOME_NOTE)
        return element
