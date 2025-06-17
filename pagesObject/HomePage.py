from pagesObject.BasePage import BasePage
from playwright.sync_api import Page, expect


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    #locators
        self.signIn_button = page.locator(".login")
        self.userAccount_link = page.locator('.account')
        self.search_bar_field = page.locator('#search_query_top')
        self.search_button = page.locator('button.btn.btn-default.button-search')
        self.message_card_empty = page.locator('.ajax_cart_no_product')


    #methodes
    def verify_home_page_title(self):
        self.verify_title_of_page("My Shop")

    def click_on_signIn_button(self):
        self.click_on_visible_element(self.signIn_button)

    def verify_user_is_connected(self):
        expect(self.userAccount_link).to_be_visible()

    def search_a_product_in_search_bar(self):
        self.fill_input_field(self.search_bar_field, "blouse")

    def click_on_search_button(self):
        self.click_on_visible_element(self.search_button)

    def verify_cart_is_empty(self):
        self.verify_element_is_visible(self.message_card_empty)
        self.verify_contain_text(self.message_card_empty, "(empty)")


