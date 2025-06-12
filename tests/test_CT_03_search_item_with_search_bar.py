import time

from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.AccountPage import AccountPage
from pagesObject.SearchPage import SearchPage


def test_search_item_with_search_bar(setup, login_valid):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    account_page = AccountPage(setup)
    search_page = SearchPage(setup)

    #se connecter
    home_page.verify_home_page_title()
    home_page.click_on_signIn_button()
    login_page.enter_email_and_password(login_valid["emailAdress"], login_valid["password"])
    login_page.click_on_signIn_button()
    account_page.verify_redirection_to_myAccount("My account - My Shop")

    #search a product
    home_page.search_a_product_in_search_bar()
    home_page.click_on_search_button()
    search_page.verify_redirected_to_search_page("Search - My Shop")
    search_page.verify_search_item_is_visible("blouse")
