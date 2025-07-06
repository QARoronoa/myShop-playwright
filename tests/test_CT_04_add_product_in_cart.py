import time

from pagesObject.HomePage import HomePage
from pagesObject.SearchPage import SearchPage
from pagesObject.ProductDetailPage import ProductDetailPage

def test_add_product_in_cart(setup, login_valid):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)
    productDetail_page = ProductDetailPage(setup)

    #add item on card
    home_page.verify_home_page_title()
    home_page.verify_cart_is_empty()
    home_page.search_a_product_in_search_bar()
    home_page.click_on_search_button()

    search_page.verify_search_item_is_visible("blouse")
    search_page.scroll_to_item_image()
    search_page.click_on_more_button()

    productDetail_page.verify_title_of_page("Blouse - My Shop")
    productDetail_page.click_on_white_button()
    productDetail_page.click_on_add_to_cart_button()
    productDetail_page.click_on_button_continue_shopping()
    productDetail_page.verify_item_is_in_cart()
