import time

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.AccountPage import AccountPage


def test_create_an_account_with_an_existing_email(setup, create_account):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    account_page = AccountPage(setup)


    #verify_home_page_title
    home_page.verify_home_page_title()

    #click on signin button
    home_page.click_on_signIn_button()

    #enter an email
    login_page.enter_email_create_account(create_account["emailAdress"])

    #cliquer sur le bouton create account
    login_page.click_on_button_create_account()

    #verify error message
    login_page.verify_error_message_is_visible("this email address has already been registered")
