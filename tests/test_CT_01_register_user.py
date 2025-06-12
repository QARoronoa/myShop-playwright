import time

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.AccountPage import AccountPage


def test_register_user(setup, enter_email_create_account, fill_out_form):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    account_page = AccountPage(setup)


    #verify_home_page_title
    home_page.verify_home_page_title()

    #click on signin button
    home_page.click_on_signIn_button()

    #enter email adress
    login_page.enter_email_create_account(**enter_email_create_account)

    #click on create account
    login_page.click_on_button_create_account()

    #fill formulaire and click register button
    login_page.fill_form_create_account(**fill_out_form)
    login_page.click_on_register_button()

    #verify redirection to account page
    account_page.verify_title_of_page("My account - My Shop")

    #verify success create account
    account_page.verify_sucess_message_creation_account()

    #verify user is connected
    home_page.verify_user_is_connected()
