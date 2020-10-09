from ApplicationTests.BaseTest import BaseTest
from ApplicationPages.LoginPage import LoginPage
from Config.App_Configs import TestData


class Test_Login(BaseTest):

    def test_username_input_box_visible(self):
        loginpage = LoginPage(self.driver)
        assert loginpage.is_available(loginpage.USERNAME)


    def test_password_input_box_visible(self):
        loginpage = LoginPage(self.driver)
        assert loginpage.is_available(loginpage.PASSWORD)


    def test_login_button_visible(self):
        loginpage = LoginPage(self.driver)
        assert loginpage.is_available(loginpage.LOGIN_BUTTON)


    def test_menu_create_record_visible(self):
        loginpage = LoginPage(self.driver)
        assert loginpage.is_available(loginpage.CREATE_RECORD)


    def test_menu_view_record_visible(self):
        loginpage = LoginPage(self.driver)
        assert loginpage.is_available(loginpage.VIEW_RECORD)


    def test_menu_search_record_visible(self):
        loginpage = LoginPage(self.driver)
        assert loginpage.is_available(loginpage.SEARCH_RECORD)

    def test_logon(self):
        loginpage = LoginPage(self.driver)
        homepage = loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        assert homepage.get_welcome_text()



