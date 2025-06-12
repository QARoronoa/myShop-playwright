import time

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.AccountPage import AccountPage


def test_with_valid_credentials(setup, login_valid):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    account_page = AccountPage(setup)


    #verify_home_page_title
    home_page.verify_home_page_title()

    #click on signin button
    home_page.click_on_signIn_button()

    #enter email adress
    login_page.enter_email_and_password(login_valid["emailAdress"], login_valid["password"])
    login_page.click_on_signIn_button()

    #verify user is connected
    home_page.verify_user_is_connected()
