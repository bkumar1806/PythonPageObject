from ApplicationPages.HomePage import HomePage
from ApplicationPages.LoginPage import LoginPage
from ApplicationTests.BaseTest import BaseTest
from Config.App_Configs import TestData

class Test_HomePage(BaseTest):

    def test_welcome_note_text(self):
        log_page = LoginPage(self.driver)
        homepage = log_page.do_login(TestData.USERNAME, TestData.PASSWORD)
        assert TestData.WELCOME_NOTE_TEXT == homepage.get_welcome_text()