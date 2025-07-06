import time

from playwright.sync_api import Page

from pagesObject.BasePage import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    #locators
        self.white_color_button = page.locator('#color_8')
        self.add_to_cart_button = page.locator('#add_to_cart')
        self.continue_shopping_button_popin = page.locator('.continue')
        self.proceed_to_checkout_button_popup = page.get_by_role('link', name="Proceed to checkout")
        self.item_name_cart_block = page.locator('.cart_block_product_name')
        self.frame = page.frame_locator(".fancybox-iframe")


    #methodes
    def verify_redirected_to_item_page(self, title):
        self.verify_title_of_page(title)

    def click_on_white_button(self):
        time.sleep(1)
        self.click_on_visible_element(self.white_color_button)
        time.sleep(1)

    def click_on_add_to_cart_button(self):
        self.click_on_visible_element(self.add_to_cart_button)

    def click_on_button_continue_shopping(self):
        self.click_on_visible_element(self.continue_shopping_button_popin)

    def verify_item_is_in_cart(self):
        self.verify_contain_text(self.item_name_cart_block, "Blouse")

    def click_on_proceed_to_checkout_popup_button(self):
        self.click_on_visible_element(self.proceed_to_checkout_button_popup)

    def add_item_on_cart_from_frame(self):
        time.sleep(2)
        self.frame.locator('#color_8').click()
        self.frame.locator('#add_to_cart').click()


