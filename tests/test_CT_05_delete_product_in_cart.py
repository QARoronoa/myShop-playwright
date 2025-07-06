import time

from pagesObject.HomePage import HomePage
from pagesObject.ProductDetailPage import ProductDetailPage
from pagesObject.SearchPage import SearchPage
from pagesObject.CartPage import CartPage


def test_delete_product_in_cart(setup):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)
    productDetail_page = ProductDetailPage(setup)
    cart_page = CartPage(setup)

    # add item on card
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
    productDetail_page.click_on_proceed_to_checkout_popup_button()


    #delete product
    cart_page.verify_redirected_to_cart_page()
    cart_page.verify_product_is_visible_in_cart("Blouse")
    cart_page.click_on_delete_button()
    cart_page.verify_cart_is_empty()
