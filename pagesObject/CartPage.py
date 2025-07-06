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
        self.proceed_to_checkout_button_popup = page.get_by_role('link', name="Proceed to checkout")
        self.shipping_title = page.locator('h1')
        self.cgu_radio_button = page.locator('#uniform-cgv')
        self.pay_bank_wire_methode = page.locator('.bankwire')
        self.confirmOrder_button = page.get_by_role('button', name='I confirm my order')
        self.success_order_message = page.locator('.alert-success')
    #methodes
    def verify_redirected_to_cart_page(self):
        self.verify_contain_text(self.shopping_cart_summary_title, "Shopping-cart summary")

    def verify_product_is_visible_in_cart(self, item):
        self.verify_contain_text(self.product_name, item)

    def click_on_delete_button(self):
        self.click_on_visible_element(self.delete_button)

    def verify_cart_is_empty(self):
        self.verify_contain_text(self.cart_empty_message, "Your shopping cart is empty.")

    def click_on_proceed_to_checkout_button(self):
        self.click_on_visible_element(self.proceed_to_checkout_button_popup)

    def verify_subtitle_page(self, text):
        self.verify_contain_text(self.shipping_title, text)

    def click_on_cgu(self):
        self.click_on_visible_element(self.cgu_radio_button)

    def click_on_payment_methode_bank_wire(self):
        self.click_on_visible_element(self.pay_bank_wire_methode)

    def click_on_confirm_button_order(self):
        self.click_on_visible_element(self.confirmOrder_button)

    def verify_success_message_order(self):
        self.verify_contain_text(self.success_order_message, "Your order on My Shop is complete.")