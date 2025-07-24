from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.AccountPage import AccountPage


def test_connect_with_an_wrong_password(setup, wrong_password):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    account_page = AccountPage(setup)


    #verify_home_page_title
    home_page.verify_home_page_title()

    #click on signin button
    home_page.click_on_signIn_button()

    #enter email adress
    login_page.enter_email_and_password(wrong_password["emailAdress"], wrong_password["password"])
    login_page.click_on_signIn_button()

    #verify error message is visible
    login_page.verify_error_message_is_visible("There is 1 error")
