import time
from pagesObject.ProductDetailPage import ProductDetailPage
from pagesObject.HomePage import HomePage
from pagesObject.CartPage import CartPage
from pagesObject.SearchPage import SearchPage


def test_make_an_order_without_being_loggeg_in(setup):
    home_page = HomePage(setup)
    productDetail_page = ProductDetailPage(setup)
    search_page = SearchPage(setup)
    cart_page = CartPage(setup)


    #verify_home_page_title
    home_page.verify_home_page_title()

    #add item in cart
    home_page.search_a_product_in_search_bar()
    home_page.click_on_search_button()
    search_page.verify_redirected_to_search_page("Search - My Shop")
    search_page.verify_search_item_is_visible("blouse")
    search_page.scroll_to_item_image()
    search_page.click_on_more_button()
    productDetail_page.click_on_white_button()
    productDetail_page.click_on_add_to_cart_button()
    productDetail_page.click_on_proceed_to_checkout_popup_button()

    #Verify login page is visible
    cart_page.verify_redirected_to_cart_page()
    cart_page.verify_product_is_visible_in_cart("Blouse")
    cart_page.click_on_proceed_to_checkout_button()
    cart_page.verify_subtitle_page("Authentication")



