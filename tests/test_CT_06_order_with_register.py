import time

from pagesObject.AccountPage import AccountPage
from pagesObject.CartPage import CartPage
from pagesObject.HomePage import HomePage
from pagesObject.LoginPage import LoginPage
from pagesObject.SearchPage import SearchPage
from pagesObject.ProductDetailPage import ProductDetailPage
from pagesObject.AddressPage import AddressPage

def test_order_with_register(setup, enter_email_create_account, fill_out_form, address_form):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    account_page = AccountPage(setup)
    cart_page = CartPage(setup)
    search_page = SearchPage(setup)
    productDetail_page = ProductDetailPage(setup)
    address_page = AddressPage(setup)

    # search a product
    home_page.verify_home_page_title()
    home_page.search_a_product_in_search_bar()
    home_page.click_on_search_button()
    search_page.verify_redirected_to_search_page("Search - My Shop")
    search_page.verify_search_item_is_visible("blouse")

    #add product in cart
    search_page.scroll_to_item_image()
    search_page.click_on_quick_view_button()
    productDetail_page.add_item_on_cart_from_frame()
    productDetail_page.click_on_proceed_to_checkout_popup_button()
    cart_page.verify_product_is_visible_in_cart("Blouse")

    #create account
    cart_page.click_on_proceed_to_checkout_button()
    login_page.enter_email_create_account(enter_email_create_account["email"])
    login_page.click_on_button_create_account()
    login_page.fill_form_create_account(**fill_out_form)
    login_page.click_on_register_button()

    #address page
    address_page.fill_address_form(**address_form)
    address_page.click_on_proceed_to_checkout()

    #shipping
    cart_page.verify_subtitle_page("Shipping:")
    cart_page.click_on_cgu()
    address_page.click_on_proceed_to_checkout()

    #payment
    cart_page.click_on_payment_methode_bank_wire()
    cart_page.click_on_confirm_button_order()

    #confirm Order
    cart_page.verify_subtitle_page("Order confirmation")
    cart_page.verify_success_message_order()
