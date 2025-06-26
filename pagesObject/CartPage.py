from playwright.sync_api import Page, expect

from pagesObject.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    #locators
        self.shopping_cart_summary_title = page.locator('#cart_title')
        self.product_name = page.locator("td.cart_description")
        self.delete_button = page.locator(".cart_quantity_delete")
        self.cart_empty_message = page.locator(".alert")

    #methodes
    def verify_redirected_to_cart_page(self):
        self.verify_contain_text(self.shopping_cart_summary_title, "Shopping-cart summary")

    def verify_product_is_visible_in_cart(self, item):
        self.verify_contain_text(self.product_name, item)

    def click_on_delete_button(self):
        self.click_on_visible_element(self.delete_button)

    def verify_cart_is_empty(self):
        self.verify_contain_text(self.cart_empty_message, "Your shopping cart is empty.")
